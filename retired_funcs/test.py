# import os
# import ssl
# import keys # python file with API Keys
# import requests
# import xml.etree.cElementTree as ET
# from requests.packages.urllib3.exceptions import InsecureRequestWarning
#
# from Keys import keys
# supresses SSL warnings on console output
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

#
# def all_connected_fws():
#     """Gets all firewalls connected to panorama.
#     Formats the XML data returned writes the firewall ip-addresses
#     to a file named 'fwips.txt'
#     """
#
#     output = requests.get('https://' + host + '/api/?type=op&cmd=<show>'
#                           '<devices><all></all></devices></show>&key='
#                           + keys.pan_vm_key(), verify=False)
#     data = output.text
#     root = ET.fromstring(data)
#     fwips = []
#     for elem in root.iter():
#         if elem.tag == 'ip-address':
#             node = elem
#             fwip = node.text # Retrieve string format
#             fwips.append(fwip)
#     return fwips

# def commit_force():
#     """Issues a commit to firewall"""
#
#     for fw in all_connected_fws():
#         cf = requests.get('https://' + fw + '/api/?type=commit&' + \
#                           'cmd=<commit><force></force></commit>&key=' + \
#                            keys.pa_vm_key(), verify=False)
#         if cf.status_code == 200:
#             print(f'Commit to {fw} successful!')


# if __name__ == '__main__':
#     host = input("Enter Panorama's IP Address: ")
#     if len(host) == 0:
#         host = '10.46.164.193'
#     all_connected_fws()
#     commit_force()

# 
# def null_decorator(func):
#     return func
#
# def greet():
#     print('Hello!')
#
# greet = null_decorator(greet)
#
# print(greet())
