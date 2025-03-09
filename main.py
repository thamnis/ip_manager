from lib.IP_utils import Ip

if __name__ == '__main__':
    print("This' to test the module features.")
    ip_input = input("Please give the IP[/CIDR] : ")
    My_IP = Ip(ip_input)

    print(f"""
    @IP = {My_IP.ip}
    @IP(0b) = {My_IP.ip_bin}
    CIDR = {My_IP.cidr}
    
    Network IP : {My_IP.net_ip}
    
    Mask = {My_IP.mask_dec}
    Mask (0b) = {My_IP.mask_bin}
    
    Usable IPs : {My_IP.usable_ips}
    
    @IP broadcast (Od) = {My_IP.broadcast_dec}
    @IP broadcast (Ob) = {My_IP.broadcast_bin}
    
    Address range : {My_IP.ip_range}
    """)

    desire = input("Would you like to optimize your network ? [o/n] : ").lower()
    if desire == 'o':
        host_len = int(input("How many host in the network : "))
        subnet = My_IP.optimize_network(host_len)

        print(f"""
        Subnetting --- 
        
        Subnet mask (0d) = {subnet["subnet_mask_dec"]}
        Subnet mask (0b) = {subnet["subnet_mask_bin"]}
        
        Subnets : """)

        for element in subnet["subnet_ips"]:
            for sn_ip, sn_range in zip(element.keys(), element.values()):
                print(f"\t\t{sn_ip} : \n\t\t\t- Range : {sn_range[0]} - {sn_range[1]}\n\t\t\t- Broadcast : {sn_range[2]}")
        print(f"""
            Number of subnet : {subnet["subnet_number"]}
            Subnet optimal number of host : {subnet["optimal_host_number"]}
            Subnet mask : {subnet["subnet_mask_dec"]}
            Subnet mask (0b): {subnet["subnet_mask_bin"]} 
            Number of address-able host : {subnet["number_host"]}
            """)
    else:
        print("Okay...")
        print("Exit.")