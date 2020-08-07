import key # API Key stored on a different file
import datetime
import requests
import xml.etree.cElementTree as ET

host = 'fw_ip_address'


def hour_resource_monitor():
    """
    Gets dataplane CPU statistics for the last hour and prints output to a file.
    """
    output = requests.get('https://'+ host + '/api/?type=op&cmd=<show>'
                          '<running><resource-monitor><hour><last>1</last>'
                          '</hour></resource-monitor></running></show>'
                          '&key='+key.pa_vm_a_key, verify=False)
    data = output.text
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


hour_resource_monitor()
