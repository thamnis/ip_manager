"""
Author  : @thamnis
License : MIT
GitHub  : https://github.com/thamnis/ip_manager
"""
import math
import re

reg = r"(\b25[0-5]|\b2[0-4][0-9]|\b[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}?(/\b([1-9]|[12][0-9]|3[0-2])\b)?"

class ValidationIpError(BaseException):
    pass

class Ip:
    """ IP class
        Attributes:
            - ip : gives the IP address
            - cidr : gives the CIDR (digits after '/' if CIDR found | gives the calculated CIDR if not found)
            - ip_bytes : gives a list of bytes of the IP address
            - ip_bin : gives the binary of IP
            - mask_bin : gives the binary mask of the couple IP/CIDR
            - mask_dec : gives the decimal mask of the couple IP/CIDR
            - addr_able : gives the number of address-able hosts
            - broadcast_bin : gives the binary broadcast IP of the network
            - broadcast_bin : gives the decimal broadcast IP of the network
            - addr_range : gives a tuple of the network IP range

        Methods:
            - optimize_network()
            - __get_ip_range()
            - __get_net_ip()
            - __to_dec()
            - __add_pts()
    """
    def __init__(self, ip_cidr: str) -> None:
        """
        Args:
            ip_cidr: Takes the network ip/[cidr] single/[couple].
                Examples: 192.168.1.0 ; 192.168.1.0/24.
        """
        self.cidr = 24
        self.ip_class = ''
        self.ip_bytes = []
        if ip_cidr:
            match = re.match(reg, ip_cidr)
            if match:
                if '/' in ip_cidr:
                    ip_divided = ip_cidr.split('/')
                    self.ip = ip_divided[0]
                    if ip_divided[-1].isdigit():
                        self.cidr = int(ip_divided[-1])
                    self.ip_bytes = self.ip.split('.')
                else:
                    self.ip = match[0]

                    self.ip_bytes = self.ip.split('.')

                    first_byte = int(self.ip_bytes[0])
                    if 1 <= first_byte <= 126:
                        self.cidr = 8
                        self.ip_class = 'A'
                    elif 127 <= first_byte <= 191:
                        self.cidr = 16
                        self.ip_class = 'B'
                    elif 192 <= first_byte <= 223:
                        self.cidr = 24
                        self.ip_class = 'C'
                    elif 224 <= first_byte <= 239:
                        raise ValidationIpError("This IP is reserved for multicast.")
                    elif 240 <= first_byte <= 255:
                        raise ValidationIpError("This IP is reserved for research purposes and future use.")
                    elif first_byte == 127:
                        raise ValidationIpError("This IP is reserved for multicast.")
                    elif first_byte == 255:
                        raise ValidationIpError("It seams to be a mask.")
            else:
                raise ValidationIpError("Invalid IP!")
        else:
            raise ValidationIpError("No IP found!")


        self.ip_bin = '.'.join([bin(int(o))[2:].zfill(8) for o in self.ip_bytes])
        self.mask_bin = self.ip_bin[:self.__add_pts(self.cidr)].replace('0', '1') + \
                        self.ip_bin[self.__add_pts(self.cidr):].replace('1', '0')
        self.mask_dec = self.__to_dec(self.mask_bin)

        self.usable_ips = 2 ** (32 - self.cidr) - 2

        self.broadcast_bin = self.ip_bin[:-(32 - self.cidr)] + self.mask_bin[self.__add_pts(self.cidr):].replace('0', '1')
        self.broadcast_dec = self.__to_dec(self.broadcast_bin)

        self.net_ip = self.__get_net_ip()
        self.ip_range = self.__get_ip_range()

    def optimize_network(self, host_number: int) -> dict:
        """ Optimize the network by splitting the network in the smallest version according to the number of host.

        Args:
            host_number: Number of hosts expected in the network.

        Returns:
            [dict] :  Optimal number of host, number of subnet, decimal subnet mask, binary subnet mask,
                      subnet IPs and their ranges, number of address-able host.

        """
        optimal_host_number = 2 ** math.ceil(math.log2(host_number))
        addr_able_host = optimal_host_number - 2
        host_bits_nbr = int(math.log2(optimal_host_number))

        subnet_bits_nbr = (32 - self.cidr) - host_bits_nbr
        subnet_number = 2 ** (32 - self.cidr - host_bits_nbr)
        subnet_mask_bin = self.mask_bin[:self.__add_pts(self.cidr)] + \
                          self.mask_bin[self.__add_pts(self.cidr):self.__add_pts(self.cidr) + \
                                                                  subnet_bits_nbr].replace('0', '1') + self.mask_bin[self.__add_pts(self.cidr) \
                                                                                                                     + self.__add_pts(subnet_bits_nbr):]

        subnet_mask_dec = self.__to_dec(subnet_mask_bin)

        subnet_ips = [{f"{'.'.join(self.ip.split('.')[:-1])}.{i * optimal_host_number}": (
            f"{'.'.join(self.ip.split('.')[:-1])}.{i * optimal_host_number + 1}",
            f"{'.'.join(self.ip.split('.')[:-1])}.{i * optimal_host_number + optimal_host_number - 2}",
            f"{'.'.join(self.ip.split('.')[:-1])}.{i * optimal_host_number + optimal_host_number - 1}")} for i in
            range(subnet_number)]

        return {"optimal_host_number": optimal_host_number, "subnet_number": subnet_number,
                "subnet_mask_dec": subnet_mask_dec, "subnet_mask_bin": subnet_mask_bin, "subnet_ips": subnet_ips,
                "number_host": addr_able_host}

    def __get_ip_range(self) -> tuple:
        """ IP range giver.

        Returns: Tuple of the range network IP (start, end).
            Examples: (192.168.1.1, 192.168.1.254).
        """
        net_ip_bytes = self.net_ip.split('.')
        start = '.'.join(['.'.join(net_ip_bytes[:-1]), str(int(net_ip_bytes[-1]) + 1)])
        end = '.'.join(['.'.join(self.broadcast_dec.split('.')[:-1]), str(int(self.broadcast_dec.split('.')[-1]) - 1)])
        return start, end

    def __get_net_ip(self) -> str:
        """ Calculate network IP.

        Returns:
            Network IP.
        """
        net_ip = []
        for byt_m, byt_i in zip(self.mask_dec.split('.'), self.ip_bytes):
            net_ip.append(str(int(byt_i) & int(byt_m)))
        return '.'.join(net_ip)

    @staticmethod
    def __to_dec(binary_ip: str) -> str:
        """ Binary to decimal IP converter.

        Args:
            binary_ip: The binary IP to turn into decimal.

        Returns: The decimal of the provided binary IP.
        """
        return '.'.join([str(int(e, 2)) for e in binary_ip.split('.')])

    @staticmethod
    def __add_pts(val: int) -> int:
        """ Add points to the count.

        Args:
            val: Val to add points.

        Returns:
            New value of val including possibly separator points in IP addresses according to the length of a byte.
        """
        return val + val // 8
