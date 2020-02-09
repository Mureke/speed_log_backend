import socket
import nmap
from netaddr import IPNetwork


def check_if_scan_available(device_names_to_avoid=()):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    s = s.getsockname()[0]
    ip = str(IPNetwork(str(f'{s}/255.255.255.0')).cidr)
    nm = nmap.PortScanner()
    scan = nm.scan(ip, arguments="-sn")
    for host in scan.get('scan'):
        device = scan['scan'][host]
        if len(device['hostnames']) > 0:
            if device['hostnames'][0]['name'] != '' and device['hostnames'][0]['name'] in device_names_to_avoid:
                return False
    return True


if __name__ == '__main__':
    allowed = check_if_scan_available()
