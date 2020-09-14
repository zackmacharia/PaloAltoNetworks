# import datetime
# import requests
# import xml.etree.cElementTree as ET
#
# from Keys import keys
#
# key = keys.sg_pa_200_key()
# host = input("Enter firewall IP Address: ")


# def descriptors_on_chip_to_file(host):
#     """Get Packet Descriptors on Chip CPU percentage; default value is 12 hours.
#     Change the interval to the desired interval in hours """
#
#     interval = input('Enter interval in hours: ')
#     if len(interval) <= 0:
#         interval = '12'
#     output = requests.get('https://'+host+'/api/?type=op&cmd=<show><running>'
#                           '<resource-monitor><hour><last>' + interval +\
#                           '</last></hour></resource-monitor></running></show>'
#                           '&key='+key, verify=False)
#     data = output.text
#     root = ET.fromstring(data)
#     date = datetime.datetime.now()
#     utc_time = datetime.datetime.utcnow()
#
#     with open('packet_descriptors.txt', mode='a+') as f:
#         f.write('*****************************************' + '\n')
#         f.write(str(utc_time) + ':' + ' Time is in UTC' + '\n')
#         f.write('*****************************************' + '\n')
#         for elem in root.iter():
#             if elem.tag == 'resource-utilization':
#                 stats_node = elem
#                 for child in stats_node:
#                     for item in child:
#                         tag = item.tag
#                         text = item.text
#                         stats = tag + ' ' + ':' + ' ' + text + ' ' + '\n'
#                         f.write(stats)

#
# descriptors_on_chip_to_file('47.190.134.39:7443')
# from pawn import Firewall
#
# fw = Firewall('47.190.134.39:7443')
# if __name__ == '__main__':
#     fw.descriptors_on_chip_to_fi

#
# import socket
#
#
# def validate_ip(ip):
#     """Check if passed argument is a valid IP Address"""
#     try:
#         socket.inet_aton(ip)
#         return str(ip)
#     except socket.error:
#         return 'OSError: Invalid IP address'
#
#
# if __name__ == '__main__':
#     print(validate_ip('484.4.3.2'))


# main_dict = {
#   "ip": "216.239.36.21",
#   "hostname": "any-in-2415.1e100.net",
#   "city": "Mountain View",
#   "region": "California",
#   "country": "US",
#   "loc": "37.3860,-122.0838",
#   "org": "AS15169 Google LLC",
#   "postal": "94035",
#   "timezone": "America/Los_Angeles"
# }
#
#
# def get_location():
#     """Parses information from 'get_all_data()' function and only prints location information"""
#
#     scope_keys = ['country', 'region', 'city', 'loc']
#     loc_dict = {}
#     for k, v in main_dict.items():
#         if k in scope_keys:
#             loc_dict[k] = v
#     print(loc_dict)
#
# get_location()


import requests
import socket
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# This is where you should write your Python code to get the IP information
#
# use ipinfo.com to query for ip information
# IPInfo is a freemium service (allow the service for free but with some limitation)
# which allow you to query information regarding IPs.
# This can be done by either their website, or a REST API.
# In the developers section, You can find info on how it can be used via REST API:
# https://ipinfo.io/developers
#
# for formating, use Markdown to provide the user with table of the IP information
# Markdown is a formatting script, to create text with visual attributes using standard text. A simple common example is wrapping an object in *bold*, which will write bold.
# The format is commonly used in sites like Wikipedia, Github and others.
# Wikipedia - https://en.wikipedia.org/wiki/Markdown
# Github documentation - https://guides.github.com/features/mastering-markdown/
# Tutorial - http://www.markdowntutorial.com/
# Markdown online - http://dillinger.io/
#
# Notes:
# - You may use as many inner functions as you wish, but eventually one function should get the ip input and return the table markdown.
# - Make sure You handle errors and edge cases gracefully .
# - Test Your code in your Playground. Just run !EscapeRoomGetCountryForIP ip=8.8.8.8 and see the results
#
# Output should include 2 tables - one for Location (Country, Region, City) and one for Coordinates (Long, Lat)


Working Code - DO NOT DELETE
#country = "somewhere"
ip = demisto.args()["ip"]
md = '## ipinfo information on IP address ' + ip + '\n'

def get_ip_info(ip):
    """Takes IP Address as input and returns it's location and coordinates """

    def validate_ip(ip):
        """Check if passed argument is a valid IP Address"""
        try:
            socket.inet_aton(ip)
            return str(ip)
        except socket.error:
            return 'Invalid IP address'

    def get_all_data():
        """Retrieves data in a string format from ipinfo.io"""

        access_token = '8272095ceec8fb'
        source = 'https://ipinfo.io/'
        url = source + ip + '?' + 'token=' + access_token
        ip_data = requests.get(url, verify=False).json()
        return ip_data

    def get_location():
        """Parses information from 'get_all_data()' function and only prints location information"""

        keys_scope = ['country', 'region', 'city', 'loc']
        loc_dict = {}
        for k, v in all_data.items():
            if k in keys_scope:
                loc_dict[k] = v
        return loc_dict
        # location = (all_data['country'],
        #             all_data['region'],
        #             all_data['city'])
        # return location

    # def get_coordinates():
    #     """Parses information from 'get_all_data()' function and only prints coordinates information"""

    #     coordinates_raw = (all_data['loc']).split(',')
    #     longi = coordinates_raw[0]
    #     lat = coordinates_raw[1]
    #     coordinates = (longi, lat)
    #     return coordinates

    ipaddr = validate_ip(ip)

    try:
        if type(ipaddr) is str:
            all_data = get_all_data()
            location1 = get_location()
            # coordinates1 = get_coordinates()
            # return location1, coordinates1
            return location1
    except:
        return 'Invalid IP. Please check your entry.'




# the next statement will simply create an entry in the incident with the markdown text you have created in the md variable
# you do not need to touch this line
#
demisto.results({'ContentsFormat': formats['markdown'], 'Type': entryTypes['note'], 'Contents': md})
demisto.results(get_ip_info(ip))
res = demisto.results(get_ip_info(ip))
res = [ {"country" : "IR", "region" : "Fars", "city": "Shiraz"} ]
# res.append( {"col1" : "val2", "col2" : 2} )
demisto.results( {'ContentsFormat': formats['table'], 'Type': entryTypes['note'], 'Contents': res} )


