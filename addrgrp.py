"""You wiil need to pip install 'pan-python' before using this script"""

import getpass

import pan.xapi


panorama = pan.xapi.PanXapi(hostname=input('Panorama IP Address: '),
                            api_username=input('Username: '),
                            api_password=getpass.getpass(prompt='Password: '))

def addr_xpath(address_name):
    """Adress Object XPATH"""

    return "/config/shared/address/entry[@name='" +\
    address_name + "']"

def addr_netmask_xpath(ip_address):
    """Address Netmask XPATH"""

    return "<ip-netmask>"+ip_address+"</ip-netmask>"

def new_addrgrp_xpath():
    """Create Adress Group XPATH"""

    address_group_name = input('Enter Address Group Name: ')
    return "/config/shared/address-group/entry[@name='" +\
    address_group_name + "']"

def addrgrp_static_xpath_element():
    """Adress Group Type"""

    return "<static />"

def source_file():
    "Allows user to enter filename with or without the '.txt' extension"

    source_file = input('Enter the name of the text file: ')
    if '.txt' not in source_file:
        source_file = source_file + '.txt'
    return source_file

def create_name_and_ipaddr_dict():
    """Reads a text file with IP Addreses and returns a dictionary with
    key=ip address name and value=ipv4 address"""

    ip_dict = {}
    with open(source_file(), mode='r') as f:
        for line in f.readlines():
            ip_address = line.rstrip()
            ip_name = 'addr-' + line.split('/')[0]
            ip_dict[ip_name] = ip_address
    return ip_dict

def main():

    address_group_xpath = new_addrgrp_xpath()
    panorama.set(xpath=address_group_xpath,
                 element=addrgrp_static_xpath_element())
    dictionary = create_name_and_ipaddr_dict()
    count = 0
    for k,v in dictionary.items():
        count+=1
        panorama.set(xpath=addr_xpath(k), element=addr_netmask_xpath(v))
        panorama.set(xpath=address_group_xpath,
                     element='<static><member>' + k + '</member></static>')
    print('Ran', count, 'api calls')


if __name__ == '__main__':
    main()
