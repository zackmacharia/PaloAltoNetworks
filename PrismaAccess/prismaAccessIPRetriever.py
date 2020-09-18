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
import json
import argparse
import subprocess
from pathlib import Path
from secrets import prisma_api_key


class PrismaGp:

    portal_endpoint = ['https://api.gpcloudservice.com/getAddrList/latest?fwType=gpcs_gp_portal&addrType=loopback_ip']
    gw_endpoint = ['https://api.gpcloudservice.com/getAddrList/latest?fwType=gpcs_gp_gw&addrType=loopback_ip']
    all_endpoint = ['https://api.gpcloudservice.com/getAddrList/latest?get_egress_ip_all=yes']
    args = ['curl', '-sk', '-H', 'header-api-key:' + prisma_api_key()]

    def __create_ip_list(self, api_call):
        output = api_call.communicate()
        data = json.loads(output[0])
        ips_list = data['result']['addrList']
        return ips_list

    def __display_ip_list(self, api_call):
        output = api_call.communicate()
        data = json.loads(output[0])
        ips_list = data['result']['addrList']
        return ips_list

    def __write_to_file(self, fname, ip_list):
        with open(fname, mode='a') as f:
            for item in ip_list:
                split_item = item.split(':')
                ip = split_item[1]
                f.write(ip + '\n')
        result = f'successfully created {fname.name} file'
        return result

    def show_portal_loopback_ips(self):
        """Returns portal loopback IP addresses as a list of strings. Formatted as 'Region:IP Addresses"""

        curl_portal_setup = self.args + self.portal_endpoint
        api_call = subprocess.Popen(curl_portal_setup, stdout=subprocess.PIPE)
        ip_list = self.__display_ip_list(api_call)
        return ip_list

    def show_gateway_loopback_ips(self):
        """Returns gateway loopback IP addresses as a list of strings. Formatted as 'Region:IP Addresses"""

        curl_gw_setup = self.args + self.gw_endpoint
        api_call = subprocess.Popen(curl_gw_setup, stdout=subprocess.PIPE)
        ip_list = self.__display_ip_list(api_call)
        return ip_list

    def show_all_ips(self):
        """Returns all IP addresses as a list of strings."""

        curl_all_setup = self.args + self.all_endpoint
        api_call = subprocess.Popen(curl_all_setup, stdout=subprocess.PIPE)
        ip_list = self.__display_ip_list(api_call)
        return ip_list

    def write_portal_loopback_ips(self):
        """writes portal loopback IP addresses to a file"""

        curl_portal_setup = self.args + self.portal_endpoint
        api_call = subprocess.Popen(curl_portal_setup, stdout=subprocess.PIPE)
        ip_list = self.__create_ip_list(api_call)
        fname = Path('portal_loopback_ips.txt')
        if fname.is_file():
            fname.unlink()
        result = self.__write_to_file(fname, ip_list)
        return result

    def write_gateway_loopback_ips(self):
        """writes gateway loopback IP addresses to a file"""

        curl_gw_setup = self.args + self.gw_endpoint
        api_call = subprocess.Popen(curl_gw_setup, stdout=subprocess.PIPE)
        ip_list = self.__create_ip_list(api_call)
        fname = Path('gateway_loopback_ips.txt')
        if fname.is_file():
            fname.unlink()
        result = self.__write_to_file(fname, ip_list)
        return result

    def write_all_ips(self):
        """writes all Prisma Access IP addresses to a file"""

        curl_all_setup = self.args + self.all_endpoint
        api_call = subprocess.Popen(curl_all_setup, stdout=subprocess.PIPE)
        ip_list = self.__create_ip_list(api_call)
        fname = Path('prisma_ips.txt')
        if fname.is_file():
            fname.unlink()
        with open(fname, mode='a') as f:
            for ip in ip_list:
                f.write(ip + '\n')
        result = f'successfully created {fname.name} file'
        return result


def parse_args():
    parser = argparse.ArgumentParser(description='Retrieve Prisma Access IP Addresses',
                                     epilog='Please report any iss'
                                            'https://github.com/zackmacharia/PaloAltoNetworks/tree/master/PrismaAccess')
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
