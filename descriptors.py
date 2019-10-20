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
from pawn import Firewall

fw = Firewall('47.190.134.39:7443')
if __name__ == '__main__':
    fw.descriptors_on_chip_to_file()
