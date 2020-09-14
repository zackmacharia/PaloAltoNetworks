import keys
import datetime
import xml.etree.cElementTree as ET
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

host = 'fw_ip_address'  # replace this value with your firewall IP address


def hour_resource_monitor():
    """
    Gets dataplane CPU statistics for the last hour and prints output to a file.
    """
    output = requests.get('https://'+ host + '/api/?type=op&cmd=<show>'
                          '<running><resource-monitor><hour><last>1</last>'
                          '</hour></resource-monitor></running></show>'
                          '&key=' + keys.firewall_api_key(), verify=False)
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


if __name__ == '__main__':
    hour_resource_monitor()
