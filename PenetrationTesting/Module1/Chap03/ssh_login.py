#!/usr/bin/env python3
import sys
try:
    import nmap
except:
    sys.exit("[!] Install the nmap library: pip install python-nmap")
try:
    import netifaces
except:
    sys.exit("[!] Install the netifaces library: pip install netifaces")


# Arguments Validator
if len(sys.argv) != 5:
    sys.exit("[!] Please provide four arguments, the first being the target,
             the second the ports, the third the username, and the fourth
             the password")

password = str(sys.argv[4])
username = str(sys.argv[3])
ports = str(sys.argv[2])
hosts = str(sys.argv[1])

home_dir="/root"
gateways = {}
network_ifaces = {}




def get_interfaces():
    interfaces = netiface.interfaces()
    return interfaces


def get_gateways():
    gateway_dict = {}
    gws = netifaces.gateways()

    for gw in gws:
        try:
            gateway_iface = gws[gw][netifaces.AF_INET]
            gateway_ip, iface = gateway_iface[0], gateway_iface[1]
            gw_list = [gateway_ip, iface]
            gateway_dict[gw] = gw_list
        except:
            pass
        return gateway_dict


def get_addresses(interface):
    addrs = netifaces.ifaddresses(interface)
    link_addr = addrs[netifaces.AF_LINK]
    iface_addrs = addrs[netifaces.AF_INET]
    iface_dict = iface_addrs[0]
    link_dict = link_addr[0]
    hwaddr = link_dict.get('addr')
    iface_addr = iface_dict.get('addr')
    iface_broadcast = iface_dict.get('broadcast')
    iface_netmask = iface_dict.get('netmask')

    return hwaddr, iface_addr, iface_broadcast, iface_netmask


def get_networks(gateway_dict):
    networks_dict = {}
    gateway_ip = iface = ""

    for key, value in gateways.items():
        gateway_ip, iface = value[0], value[1]
        hwaddress, addr, broadcast, netmask = get_addresses(iface)
        network = {'gateway': gateway_ip, 'hwaddr': hwaddress,
            'addr': addr, 'broadcast': broadcast, 'netmask': netmask }

        networks_dict[iface] = network

    return networks_dict


def  resource_file_builder(dir_, user, passwd, ips, port_num, hosts_file):
    ssh_login_rc = "%s/ssh_login.rc" %(dir_)
    bufsize = 0
    set_module = "use auxiliary/scanner/ssh/ssh_login \n"
    set_user = "set username " + username + "\n"
    set_pass = "set password " + password + "\n"
    set_rhosts = "set rhosts file: " + hosts_file + "\n"
    set_rport = "set rport " + ports + "\n"
    execute = "run\n"

    f = open(ssh_login_rc, "w", bufsize)
    f.write(set_module)
    f.write(set_user)
    f.write(set_pass)
    f.write(set_rhosts)
    f.write(set_rport)
    f.write(execute)
    f.close()


def target_identifier(dir_, user, passwd, ips, port, port_num, ifaces):
    bufsize = 0
    ssh_host = "%s / ssh_hosts" %(dir_)
    scanner = nmap.PortScanner()
    scanner.scan(ips, port_num)
    open(ssh_hosts, "w").close()

    if scanner.all_hosts():
        e = open(ssh_hosts, "a", bufsize)
    else:
        sys.exit()

    for host in scanner.all_hosts():
        for k, v in ifaces.items():
            if v['addr'] == host:
                print("[-] Removing %s from target list since it belongs\
                      belongs to your interface!" %(host))
                host = None
            if host != None:
                home_dir = "/root"
                ssh_hosts = "%s / ssh_hosts" %(host)
                bufsize = 0

                e = open(ssh_hosts, "a", bufsize)
                if 'ssh' in scanner[host]['tcp'][int(port_num)]['name']:
                    if 'open' in scanner[host]['tcp'][int(port_num)]['state']:
                        print("[+] Adding host %s to %s since the service is
                              active on %s" %(host, ssh_hosts, port_num))
                        hostdata = host + '\n'
                        e.write(hostdata)

    if not scanner.all_hosts():
        e.close()
    if ssh_hosts:
        return ssh_hosts


if __name__ == '__main__':
    gateways = get_gateways()
    network_ifaces = get_networks(gateways)
    hosts_file = target_identifier(home_dir, username, password,
                                   hosts, ports, network_ifaces)
    resource_file_builder(home_dir, username, password, hosts,
                          ports, hosts_file)
