import unittest
from lib.IP_utils import Ip, ValidationIpError

class TestIp(unittest.TestCase):

    def test_valid_ip(self):
        ip = Ip("192.168.1.0")
        self.assertEqual(ip.ip, "192.168.1.0")
        self.assertEqual(ip.cidr, 24)
        self.assertEqual(ip.usable_ips, 254)  # 2^(32-24) - 2 = 254

    def test_invalid_ip(self):
        with self.assertRaises(ValidationIpError):
            Ip("256.256.256.256")  # IP invalide

    def test_reserved_ip(self):
        with self.assertRaises(ValidationIpError):
            Ip("224.0.0.0")  # IP réservée

    def test_missing_ip(self):
        with self.assertRaises(ValidationIpError):
            Ip("")  # IP vide

    def test_broadcast_and_range(self):
        ip = Ip("192.168.1.0")
        self.assertEqual(ip.broadcast_dec, "192.168.1.255")
        self.assertEqual(ip.usable_ips, ("192.168.1.1", "192.168.1.254"))

    def test_ip_to_bin(self):
        ip = Ip("192.168.1.0")
        self.assertEqual(ip.ip_bin, "11000000.10101000.00000001.00000000")

    def test_mask_dec(self):
        ip = Ip("192.168.1.0")
        self.assertEqual(ip.mask_dec, "255.255.255.0")

    def test_split_network(self):
        ip = Ip("192.168.1.0")
        self.assertEqual(ip.optimize_network(55),{'subnet_mask_dec': '255.255.255.192',
                          'subnet_mask_bin': '11111111.11111111.11111111.11000000',
                          'subnet_ips': [{'192.168.1.0': ('192.168.1.1', '192.168.1.62', '192.168.1.63')},
                                         {'192.168.1.64': ('192.168.1.65', '192.168.1.126', '192.168.1.127')},
                                         {'192.168.1.128': ('192.168.1.129', '192.168.1.190', '192.168.1.191')},
                                         {'192.168.1.192': ('192.168.1.193', '192.168.1.254', '192.168.1.255')}]})

if __name__ == "__main__":
    unittest.main()
