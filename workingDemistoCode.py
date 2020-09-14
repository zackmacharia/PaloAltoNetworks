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

#country = "somewhere"
ip = demisto.args()["ip"]
md = '## ipinfo information on IP address ' + ip + '\n'

# def get_ip_info(ip):
#     """Takes IP Address as input and returns it's location and coordinates """

#     def validate_ip(ip):
#         """Check if passed argument is a valid IP Address"""
#         try:
#             socket.inet_aton(ip)
#             return str(ip)
#         except socket.error:
#             return 'Invalid IP address'

#     def get_all_data():
#         """Retrieves data in a string format from ipinfo.io"""

#         access_token = '8272095ceec8fb'
#         source = 'https://ipinfo.io/'
#         url = source + ip + '?' + 'token=' + access_token
#         ip_data = requests.get(url, verify=False).json()
#         return ip_data

#     def get_location():
#         """Parses information from 'get_all_data()' function and only prints location information"""

#         keys_scope = ['country', 'region', 'city', 'loc']
#         loc_dict = {}
#         for k, v in all_data.items():
#             if k in keys_scope:
#                 loc_dict[k] = v
#         return loc_dict

#     ipaddr = validate_ip(ip)

#     try:
#         if type(ipaddr) is str:
#             all_data = get_all_data()
#             location1 = get_location()
#             # coordinates1 = get_coordinates()
#             # return location1, coordinates1
#             return location1
#     except:
#         return 'Invalid IP. Please check your entry.'


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

    def get_loc_data():
        static_keys = ['country', 'region', 'city', 'loc']
        static_key_values = [all_data['country'],
                             all_data['region'],
                             all_data['city'],
                             all_data['loc']]
        phy_loc_dict = dict(zip(static_keys, static_key_values))
        phy_loc = [phy_loc_dict]
        return phy_loc

    ipaddr = validate_ip(ip)

    try:
        if type(ipaddr) is str:
            all_data = get_all_data()
            loc = get_loc_data()
            return loc

    except:
        return 'Invalid IP. Please check your entry.'

res = get_ip_info(ip)
# str_res = str(res).strip('[').strip(']')
# pos = str_res.find('loc')  # find index where 'loc' appears in string
# cords_start_pos = pos - 1  # starting slicing index for 'loc'
# cords_raw = str_res[cords_start_pos:-1]

# cords_digits = cords_raw.strip("'loc': '")
# cords_split = cords_digits.split(',')
# cords_keys = ['longitude', 'latitude']
# cords_dict = dict(zip(cords_keys, cords_split))
# cords_list = []
# cords_list.append(cords_dict)
# res1 = cords_list

# end_pos = cords_start_pos - 2
# location = str_res[:end_pos]
# loc_strip = location.strip('{')
# loc_split = loc_strip.split(',')
# loc_keys = ['county', 'region', 'city']
# loc_values = []
# for item in loc_split:
#     item_strip = item.split(':')
#     item_split = item_strip[1].strip()
#     item_value = item_split[1:-1]
#     loc_values.append(item_value)
# loc_dict = dict(zip(loc_keys, loc_values))
# loc_list = []
# loc_list.append(loc_dict)
# res2 = loc_list

str_res = str(res).strip('[').strip(']')
pos = str_res.find('loc')  # find index where 'loc' appears in string
cords_start_pos = pos - 1  # starting slicing index for 'loc'
cords_raw = str_res[cords_start_pos:-1]

cords_digits = cords_raw.strip("'loc': '")
cords_split = cords_digits.split(',')
cords_keys = ['longitude', 'latitude']
cords_dict = dict(zip(cords_keys, cords_split))
cords_list = []
cords_list.append(cords_dict)
res1 = cords_list


end_pos = cords_start_pos - 2
location = str_res[:end_pos]
loc_strip = location.strip('{')
loc_split = loc_strip.split(',')
loc_keys = ['county', 'region', 'city']
loc_values = []
for item in loc_split:
    item_strip = item.split(':')
    item_split = item_strip[1].strip()
    item_value = item_split[1:-1]
    loc_values.append(item_value)
loc_dict = dict(zip(loc_keys, loc_values))
loc_list = []
loc_list.append(loc_dict)
res2 = loc_list

# the next statement will simply create an entry in the incident with the markdown text you have created in the md variable
# you do not need to touch this line
#
demisto.results({'ContentsFormat': formats['markdown'], 'Type': entryTypes['note'], 'Contents': md})
demisto.results( {'ContentsFormat': formats['table'], 'Type': entryTypes['note'], 'Contents': res} )
demisto.results( {'ContentsFormat': formats['table'], 'Type': entryTypes['note'], 'Contents': res2} )
demisto.results( {'ContentsFormat': formats['table'], 'Type': entryTypes['note'], 'Contents': res1} )