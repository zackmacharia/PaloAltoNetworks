"""
Prisma Access IP Retriever

This script make API calls to Palo Alto Networks GlobalProtect Cloud Service and provides an option to print out 
the results on console or write results to a file.

For security purposes the API Key is not hardcoded in the script rather it is stored in a different file named
"secrets.py" which contains a simple function that returns an API key. You will want to have the secrets.py file
be on the same location as this script. Otherwise you will have to tweak the code referencing the full path to the
secrets.py file.

Instructions on creating secrets.py file:
Using your editor of choice create a new file and name it "secrets.py"
Create a new function by entering the following lines of code.
def prisma_api_key():
    return 'YOUR_API_KEY_GOES_HERE_BETWEEN_THE_SINGLE_QUOTES'
Save your changes.

This script requires that `requests` be installed within the Python environment you are running this script in.
**pip3 install requests.

usage: prismaAccessIPRetriever.py [-h] [-spl] [-wpl] [-sgl] [-wgl] [-sa] [-wa]

Retrieve Prisma Access IP Addresses

optional arguments:
  -h, --help               show this help message and exit
  -spl, --show-portal-lb   display portal loopback ips
  -wpl, --write-portal-lb  write portal ips to file
  -sgl, --show-gw-lb       display gateway loopback ips
  -wgl, --write-gw-lb      write gateway ips to file
  -sa, --show-all          display all prisma access ips
  -wa, --write-all         write all prisma access ips

Author: Zack Macharia
Email: zmacharia@paloaltonetworks.com

© 2020 Palo Alto Networks, Inc.  All rights reserved.

Licensed under SCRIPT SOFTWARE AGREEMENT, Palo Alto Networks, Inc.,
at https://www.paloaltonetworks.com/legal/script-software-license-1-0.pdf
"""

# TODO
# Support all other IP Types
import sys
import argparse
import requests
from pathlib import Path
from secrets import prisma_api_key

requests.packages.urllib3.disable_warnings()


class PrismaGp:

    portal_endpoint = 'https://api.gpcloudservice.com/getAddrList/latest?fwType=gpcs_gp_portal&addrType=loopback_ip'
    gw_endpoint = 'https://api.gpcloudservice.com/getAddrList/latest?fwType=gpcs_gp_gw&addrType=loopback_ip'
    all = 'https://api.gpcloudservice.com/getAddrList/latest?get_egress_ip_all=yes'
    headers = {'header-api-key': prisma_api_key()}

    def show_portal_loopback_ips(self):
        """Returns portal loopback IP addresses as a list of strings. Formatted as 'Region:IP Addresses"""

        api_call = requests.get(self.portal_endpoint, headers=self.headers, verify=False)
        data = api_call.json()
        ips_list = data['result']['addrList']
        ip_list = []
        for ip in ips_list:
            ip_list.append(ip)
        return ip_list

    def write_portal_loopback_ips(self):
        """writes portal loopback IP addresses to a file"""

        api_call = requests.get(self.portal_endpoint, headers=self.headers, verify=False)
        data = api_call.json()
        ips_list = data['result']['addrList']
        fname = Path('portal_loopback_ips.txt')
        if fname.is_file():
            fname.unlink()
        with open(fname, mode='a') as f:
            for item in ips_list:
                split_item = item.split(':')
                ip = split_item[1]
                f.write(ip + '\n')
        result = f'successfully created {fname.name} file'
        return result

    def show_gateway_loopback_ips(self):
        """Returns gateway loopback IP addresses as a list of strings. Formatted as 'Region:IP Addresses"""

        api_call = requests.get(self.gw_endpoint, headers=self.headers, verify=False)
        data = api_call.json()
        ips_list = data['result']['addrList']
        ip_list = []
        for ip in ips_list:
            ip_list.append(ip)
        return ip_list

    def write_gateway_loopback_ips(self):
        """writes gateway loopback IP addresses to a file"""

        api_call = requests.get(self.gw_endpoint, headers=self.headers, verify=False)
        data = api_call.json()
        ips_list = data['result']['addrList']
        fname = Path('gateway_loopback_ips.txt')
        if fname.is_file():
            fname.unlink()
        with open(fname, mode='a') as f:
            for item in ips_list:
                split_item = item.split(':')
                ip = split_item[1]
                f.write(ip + '\n')
        result = f'successfully created {fname.name} file'
        return result

    def show_all_ips(self):
        """Returns all IP addresses as a list of strings."""

        api_call = requests.get(self.all, headers=self.headers, verify=False)
        data = api_call.json()
        ips_list = data['result']['addrList']
        ip_list = []
        for ip in ips_list:
            ip_list.append(ip)
        return ip_list

    def write_all_ips(self):
        """writes all Prisma Access IP addresses to a file"""

        api_call = requests.get(self.all, headers=self.headers, verify=False)
        data = api_call.json()
        ips_list = data['result']['addrList']
        fname = Path('prisma_access_ips.txt')
        if fname.is_file():
            fname.unlink()
        with open(fname, mode='a') as f:
            for ip in ips_list:
                f.write(ip + '\n')
        result = f'successfully created {fname.name} file'
        return result


def parse_args():
    parser = argparse.ArgumentParser(description='Retrieve Prisma Access IP Addresses')
    parser.add_argument('-spl', '--show-portal-lb',
                        action='store_true',
                        help='display portal loopback ips')
    parser.add_argument('-wpl', '--write-portal-lb',
                        action='store_true',
                        help='write portal ips to file')
    parser.add_argument('-sgl', '--show-gw-lb',
                        action='store_true',
                        help='display gateway loopback ips')
    parser.add_argument('-wgl', '--write-gw-lb',
                        action='store_true',
                        help='write gateway ips to file')
    parser.add_argument('-sa', '--show-all',
                        action='store_true',
                        help='display all prisma access ips')
    parser.add_argument('-wa', '--write-all',
                        action='store_true',
                        help='write all prisma access ips')
    return parser.parse_args()


def main():
    prisma_gp = PrismaGp()
    args = parse_args()
    if args.show_portal_lb:
        print('\nPortal Loopback IPs:\n')
        result_list = prisma_gp.show_portal_loopback_ips()
        print(*result_list, sep='\n')
        print('')
    elif args.show_gw_lb:
        print('\nGateway Loopback IPs:\n')
        result_list = prisma_gp.show_gateway_loopback_ips()
        print(*result_list, sep='\n')
        print('')
    elif args.show_all:
        print('\nAll Prisma Access IPs:\n')
        result_list = prisma_gp.show_all_ips()
        print(*result_list, sep='\n')
        print('')
    elif args.write_portal_lb:
        print('\nWriting to file...')
        print(prisma_gp.write_portal_loopback_ips())
    elif args.write_gw_lb:
        print('\nWriting to file...')
        print(prisma_gp.write_gateway_loopback_ips())
    elif args.write_all:
        print('\nWriting to file...')
        print(prisma_gp.write_all_ips())


if __name__ == '__main__':
    main()
