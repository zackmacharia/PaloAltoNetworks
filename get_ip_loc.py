import requests
import socket
# from requests.packages.urllib3.exceptions import InsecureRequestWarning
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# This is where you should write your Python code to get the IP information
#
# use ipinfo.com to query for ip information
# IPInfo is a freemium service (allow the service for free but with some limitation)
# which allow you to query information regarding IPs.
# This can be done by either their website, or a resultEntriesT API.
# In the developers section, You can find info on how it can be used via resultEntriesT API:
# https://ipinfo.io/developers
#
# for formating, use Markdown to provide the user with table of the IP information
# Markdown is a formatting script, to create text with visual attributes using standard text. A simple common example is wrapping an object in *bold*, which will write bold.
# The format is commonly used in sites like Wikipedia, Github and others.
# Wikipedia - https://en.wikipedia.org/wiki/Markdown
# Github documentation - https://guides.github.com/featuresultEntries/mastering-markdown/
# Tutorial - http://www.markdowntutorial.com/
# Markdown online - http://dillinger.io/
#
# Notes:
# - You may use as many inner functions as you wish, but eventually one function should get the ip input and return the table markdown.
# - Make sure You handle errors and edge cases gracefully .
# - Test Your code in your Playground. Just run !EscapeRoomGetCountryForIP ip=8.8.8.8 and see the resultEntriesults
#
# Output should include 2 tables - one for Location (Country, Region, City) and one for Coordinates (Long, Lat)

#country = "somewhere"
# ip = demisto.args()["ip"]
# md = '## ipinfo information on IP addresultEntriess ' + ip + '\n'
# loc = [{'county': 'val', 'region': 1, 'city': 'val', 'loc': 'val'}] # return a list of dictionaries
# main function to return a list of dictionaries
# child functions to return a dictionary that gets appended to the main dict

#THIS CODE WORKS
# def get_ip_info(ip):
#     """Takes IP AddresultEntriess as input and returns it's location and coordinates """
#
#     def validate_ip(ip):
#         """Check if passed argument is a valid IP AddresultEntriess"""
#         try:
#             socket.inet_aton(ip)
#             return str(ip)
#         except socket.error:
#             return 'Invalid IP addresultEntriess'
#
#     def get_all_data():
#         """Retrieves data in a string format from ipinfo.io"""
#
#         access_token = '8272095ceec8fb'
#         source = 'https://ipinfo.io/'
#         url = source + ip + '?' + 'token=' + access_token
#         ip_data = requests.get(url, verify=False).json()
#         return ip_data
#
#     def get_loc_data():
#         static_keys = ['country', 'region', 'city', 'loc']
#         static_key_values = [all_data['country'],
#                              all_data['region'],
#                              all_data['city'],
#                              all_data['loc']]
#         phy_loc_dict = dict(zip(static_keys, static_key_values))
#         phy_loc = [phy_loc_dict]
#         return phy_loc
#
#     ipaddr = validate_ip(ip)
#
#     try:
#         if type(ipaddr) is str:
#             all_data = get_all_data()
#             loc = get_loc_data()
#             return loc
#
#     except:
#         return 'Invalid IP. Please check your entry.'
#
#
# if __name__ == '__main__':
#     print(get_ip_info('4.84.4.59'))

resultEntries = [{'country': 'US', 'region': 'Georgia', 'city': 'Atlanta', 'loc': '33.7490,-84.3880'}]
resultEntries_dict = resultEntries[0]
coord_values = resultEntries_dict.pop('loc')
coord_list = coord_values.split(',')
static_coord_values = ['Latitude', 'Longitude']
coord_dict = dict(zip(static_coord_values, coord_list))
resultEntries1 = []
for x in range(1):
    resultEntries1.append(coord_dict)
# print(resultEntries1)

loc_values = []
static_loc_values = ['country', 'region', 'city']
for k, v in resultEntries_dict.items():
    if k in static_loc_values:
        loc_values.append(v)
loc_dict = dict(zip(static_loc_values, loc_values))
resultEntries2 = []
for x in range(1):
    resultEntries2.append(loc_dict)
print(resultEntries2)

resultEntries = res
try:
    if isError(resultEntries[0]):
        if 'failed with status 404 NOT FOUND' in resultEntries[0]['Contents']:
            demisto.resultEntriesults({'Type': entryTypes['error'], 'ContentsFormat': formats['text'], 'Contents': 'Received HTTP Error 404 from Session API. Please ensure that you do not already have an active session with that sensor, and if not - report to the sysadmin.'})
        else:
            demisto.resultEntriesults(resultEntries)
    else:
        demisto.resultEntriesults({'ContentsFormat': formats['markdown'], 'Type': entryTypes['note'], 'Contents': md})
        demisto.resultEntriesults({'ContentsFormat': formats['table'], 'Type': entryTypes['note'], 'Contents': resultEntries1})
        demisto.resultEntriesults({'ContentsFormat': formats['table'], 'Type': entryTypes['note'], 'Contents': resultEntries2})
except Exception as ex:
    demisto.resultEntriesults( { 'Type' : entryTypes['error'], 'Contentmat' : formats['text'], 'Contents' : 'Error occurred while parsing output from command. Exception info:\n' + str(ex) + '\n\nInvalid output:\n' + str( resultEntries ) } )


# try:
#     if isError(resultEntries[0]):
#         if 'failed with status 404 NOT FOUND' in resultEntries[0]['Contents']:
#             demisto.results({'Type': entryTypes['error'], 'ContentsFormat': formats['text'], 'Contents': 'Received HTTP Error 404 from Session API. Please ensure that you do not already have an active session with that sensor, and if not - report to the sysadmin.'})
#         else:
#             demisto.results(resultEntries)
#     else:
#         demisto.results({'ContentsFormat': formats['markdown'], 'Type': entryTypes['note'], 'Contents': md})
#         demisto.results({'ContentsFormat': formats['table'], 'Type': entryTypes['note'], 'Contents': res1})
#         demisto.results({'ContentsFormat': formats['table'], 'Type': entryTypes['note'], 'Contents': res2})
# except Exception as ex:
#     demisto.results( { 'Type' : entryTypes['error'], 'Contentmat' : formats['text'], 'Contents' : 'Error occurred while parsing output from command. Exception info:\n' + str(ex) + '\n\nInvalid output:\n' + str( resultEntries ) } )

# try:
#     if isError(res[0]):
#         if 'failed with status 404 NOT FOUND' in res[0]['Contents']:
#             demisto.results({'Type': entryTypes['error'], 'ContentsFormat': formats['text'], 'Contents': 'Received HTTP Error 404 from Session API. Please ensure that you do not already have an active session with that sensor, and if not - report to the sysadmin.'})
#         else:
#             demisto.results(get_ip_info(ip))
#     else:
#         demisto.results({'ContentsFormat': formats['markdown'], 'Type': entryTypes['note'], 'Contents': md})
#         demisto.results({'ContentsFormat': formats['table'], 'Type': entryTypes['note'], 'Contents': res1})
#         demisto.results({'ContentsFormat': formats['table'], 'Type': entryTypes['note'], 'Contents': res2})
# except Exception as ex:
#     demisto.results( { 'Type' : entryTypes['error'], 'Contentmat' : formats['text'], 'Contents' : 'Error occurred while parsing output from command. Exception info:\n' + str(ex) + '\n\nInvalid output:\n' + str( res ) } )

