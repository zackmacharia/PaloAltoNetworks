import datetime
import requests
import xml.etree.cElementTree as ET

key = 'APIKEY'
host = input("Enter firewall IP Address: ")


def resource_monitor():
    output = requests.get('https://'+host+'/api/?type=op&cmd=<show>'
                          '<running><resource-monitor><hour><last>1</last>'
                          '</hour></resource-monitor></running></show>'
                          '&key='+key, verify=False)
    return output.text


data = resource_monitor()
root = ET.fromstring(data)
date = datetime.datetime.now()
utc_time = datetime.datetime.utcnow()

with open('packet_descriptors.txt', mode='a+') as f:
    f.write('*****************************************' + '\n')
    f.write(str(utc_time) + ':' + ' Time is in UTC' + '\n')
    f.write('*****************************************' + '\n')
    for elem in root.iter():
        if elem.tag == 'resource-utilization':
            stats_node = elem
            for child in stats_node:
                for item in child:
                    tag = item.tag
                    text = item.text
                    stats = tag + ' ' + ':' + ' ' + text + ' ' + '\n'
                    f.write(stats)
