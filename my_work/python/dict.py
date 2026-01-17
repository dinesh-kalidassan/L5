#!/usr/bin/python3

devices = {
    'leaf1': '192.168.1.1',
    'leaf2': '192.168.1.2',
    'spine1': '192.168.1.10'
}

# Print all devices and their IPs
for hostname, ip in devices.items():
    print(f'IP address of {hostname} is {ip}')
