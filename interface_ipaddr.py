import xml.etree.ElementTree as ET
import ipaddress
import requests
import keys


while True:
    try:
        host = input("Enter Firewall's IP Address: ")
        ipaddress.ip_address(host) # validate user input is a valid IP Address
        break
    except:
        print('Error! Please enter a valid IP Address.')

int_no = input("Enter Firewall's Ethernet Port Number: ")


def sub_int_ipaddr():
    """Get Subinterfac IP Address from Palo Alto Firewall"""
    interface = "\'" +  'ethernet1/' + int_no + "\'" # sub-interface with single quotes per API
    split_int = interface.split('.')
    main_int = split_int[0] + "\'"  # physical interface with single quote per API
    # apikey = keys.homefw2_key
    apikey = keys.pa_vm_a()
    xpath = "/api/?type=config&action=get&xpath=/config/devices/entry[@name="\
                 "'localhost.localdomain']/network/interface/ethernet/entry[@name=" + main_int + \
                 "]/layer3/units/entry[@name=" + interface + "]/ip&key=" + apikey
    url = 'https://' + host + xpath
    get_cfg = requests.get(url, verify=False)
    data = str(get_cfg.text)
    tree = ET.fromstring(data)
    status = tree.attrib
    status_code = status['code']
    if status['code'] != '19':
        print('No IP Address Assigned')
    else:
        for elem in tree.iter('entry'):
            ipaddr = elem.attrib
            int_ipaddr= ipaddr['name']
            print(int_ipaddr)


def int_ipaddr():
    """Get Physical Interfac IP Address from Palo Alto Firewall"""
    interface = "\'" +  'ethernet1/' + int_no + "\'"
    # apikey = keys.homefw2_key
    apikey = keys.pa_vm_a()
    xpath = "/api/?type=config&action=get&xpath=/config/devices/entry[@name="\
                 "'localhost.localdomain']/network/interface/ethernet/entry[@name=" + interface + "]/layer3/ip" \
                "&key="+ apikey
    url = 'https://' + host + xpath
    get_cfg = requests.get(url, verify=False)
    data = str(get_cfg.text)
    tree = ET.fromstring(data)
    status = tree.attrib
    status_code = status['code']
    if status['code'] != '19':
        print('No IP Address Assigned')
    else:
        for elem in tree.iter('entry'):
            ipaddr = elem.attrib
            int_ipaddr= ipaddr['name']
            print(int_ipaddr)


def main():
    if '.' in int_no:
        sub_int_ipaddr()
    else:
        int_ipaddr()


main()
