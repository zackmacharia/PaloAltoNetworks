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

def from_file_extract_ips():
    """Reads a file with ip addresses and returns a list of IPs"""

    ip_list = []
    with open('ip_list.txt') as f:
        for line in f.readlines():
            ip_address = line.rstrip()
            ip_list.append(ip_address)
    return ip_list

def from_file_create_address_name():
    """Reads a file with ip addresses and returns a list of IPs"""

    address_names = []
    for address in from_file_extract_ips():
        format_name = 'addr-' + address.split('/')[0]
        address_names.append(format_name)
    return address_names

def create_name_and_ipaddr_dict():
    """Takes two lists, one with address name and another with the IP address
    value and returns one dictionary where names are the key and ip the value"""

    keys = from_file_create_address_name()
    values = from_file_extract_ips()
    name_ipaddr_dict = dict(zip(keys, values))
    return name_ipaddr_dict

def main():

    address_group_xpath = new_addrgrp_xpath()
    panorama.set(xpath=address_group_xpath,
                 element=addrgrp_static_xpath_element())
    from_file_create_address_name()
    from_file_extract_ips()
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
