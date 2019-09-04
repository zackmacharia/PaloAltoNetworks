import os
import ssl
import keys # not a standard library
import requests
import xml.etree.cElementTree as ET
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# supresses SSL warnings on console output
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

host = 'panorama_ip_address'

def all_connected_fws():
    """Gets all firewalls connected to panorama.
    Formats the XML data returned writes the firewall ip-addresses
    to a file named 'fwips.txt'
    """

    output = requests.get('https://' + host + '/api/?type=op&cmd=<show>'
                          '<devices><all></all></devices></show>&key='
                          + keys.pan_vm_key(), verify=False)
    data = output.text
    root = ET.fromstring(data)
    with open('fwips.txt', mode='a+') as f:
        for elem in root.iter():
            if elem.tag == 'ip-address':
                node = elem
                for item in node.iter():
                    fw_ip = item.text + '\n'
                    f.write(fw_ip)

def export_device_state():
    """Retrieve firewall device state file"""

    if not os.path.exists('DS_Folder'):
        os.makedirs('DS_Folder')
        # os.chdir('DeviceStateFolder')
    with open('fwips.txt', mode='r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.rstrip()
            data = requests.get('https://' + line + '/api/?type=export&'
                         'category=device-state&key=' + \
                          keys.pa_vm_a(), verify=False)
            os.chdir('DS_Folder')
            with open(line+'_device_state_cfg.tgz', mode='wb') as f:
                f.write(data.content)


if __name__ == '__main__':
    # all_connected_fws()
    export_device_state()
