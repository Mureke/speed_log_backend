import nmap


def check_if_scan_available(ip='192.168.10.0/24', device_names_to_avoid=()):
    nm = nmap.PortScanner()
    scan = nm.scan(ip, arguments="-sn")
    for host in scan.get('scan'):
        device = scan['scan'][host]
        if len(device['hostnames']) > 0:
            print(device['hostnames'][0]['name'])
            if device['hostnames'][0]['name'] in device_names_to_avoid:
                print(f'Found {device["hostnames"][0]["name"]}')
                return False
    return True


if __name__ == '__main__':
    alled = check_if_scan_available()
    print(alled)
