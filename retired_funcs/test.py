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
# num = []
# #
# for x in range(1000):
#     if x % 3 == 0 or x % 5 == 0:
#         num.append(x)
#
# print(sum(num))
#
#
# numbers = sum([x for x in range(1000) if x % 3 == 0 or x % 5 == 0])
# print(numbers)

# seq = [1, 2]
# even_seq = []
#
# while seq[-1] <= 4_000_000:
#     next_num = seq[-2] + seq[-1]
#     seq.append(next_num)
#
# even_seq = [x for x in seq if x % 2 == 0]
# print(sum(even_seq))


# prime_numbers = []

# for x in reversed(range(600_851_475_143)):
#     if 600_851_475_143 % x == 0:
#         print(x)
#         break
# for x in range(2, 600_851_475_143):
#     if 600_851_475_143 % x == 0:
#         print(x)
#         break
# print('Done')
# num = 600_851_475_143 / x
# print(num)


import xml.etree.cElementTree as ET
import xlsxwriter


filename = input('Enter a configuration file name: ')

if len(filename) <= 0:
    filename = '02152020testfile.xml'

root = ET.parse(filename).getroot()

service_node = root.findall('./shared/service/')

shared_svc_names = []
shared_svc_values = []

for values in service_node:
    name = values.attrib['name']
    protocol = values[0][0].tag
    port = values[0][0][0].text
    port_number = protocol + '/' + port
    # print(name)
    # print(port_number)
    # print(protocol)
    shared_svc_names.append(name)
    shared_svc_values.append(port_number)

# print(shared_svc_names)
# print(shared_svc_values)
# test_dup_list = ['one', 'two', 'one']


def dups_in_list(listname):
    """Check for duplicates entries in a list"""

    if len(listname) == len(set(listname)):
        return False
    else:
        print('Error: Duplicates service names found!')


def shared_svcs_dict():
    """Create a dictionary of shared services if no duplicate names exists"""
    
    if dups_in_list(shared_svc_names) is False:
        shared_svcs = dict(zip(shared_svc_names, shared_svc_values))
        # print(shared_svcs)
        return shared_svcs


# print(type(shared_svcs_dict()))

track_v = []
dup_list = []

for k, v in shared_svcs_dict().items():
    # print("printing v's", v)
    if v not in track_v:
        track_v.append(v)
    else:
        dup_list.append(v)
# print(track_v)
# for k, v in shared_svcs_dict().items():
#     if v in dup_list:
#         print(k, ':', v)


workbook = xlsxwriter.Workbook('example2.xlsx')
worksheet = workbook.add_worksheet()

dict1 = {'web': 'tcp/80',
         'sql': 'tcp/1433',
         'sip': 'tcp/5060',
         'ike': 'udp/4500'
          }

row = 0
for key in dict1.keys():
    worksheet.write(row, 0, key)
    worksheet.write_string(row, 1, dict1[key])
    row += 1


workbook.close()





