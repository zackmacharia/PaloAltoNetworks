import os
import ssl
import keys # python file with API Keys
import requests
import xml.etree.cElementTree as ET
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# supresses SSL warnings on console output
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Pseudo Code
# Verify there is a console connection to each device (panorama and firewalls)
# Connect to panorama
# Export Panorama and device config bundle
# Get IP Address for all the firewalls
# Connect to each firewall and export the device device device state
# Issue a commit force on each firewall
# Change master key on panorama
# Change master key on firewall

# host = input("Enter Panorama's IP Address: ")

def all_connected_fws_to_file():
    """Gets all firewalls connected to panorama.
    Retrieves the firewall ip-addresses and writes
    to a file named 'fwips.txt'"""

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

def commit_force():
    """Reads a text file containing firewall IP Addresses and issues a
    commit to each firewall"""

    with open('fwips.txt', mode='r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.rstrip()
            commit_f = requests.get('https://' + line + '/api/?type=commit&' + \
                                    'cmd=<commit><force></force></commit>' + \
                                     keys.pa_vm_a(), verify=False)

def export_device_state():
    """Retrieve firewall device state file"""

    if not os.path.exists('Device_State'):
        os.makedirs('Device_State')
    with open('fwips.txt', mode='r') as f:
        lines = f.readlines()
        os.chdir('Device_State') # change directory to store device state files
        for line in lines:
            line = line.rstrip()
            data = requests.get('https://' + line + '/api/?type=export&'
                         'category=device-state&key=' + \
                          keys.pa_vm_a(), verify=False)
            with open(line+'_device_state_cfg.tgz', mode='wb') as f:
                f.write(data.content)


if __name__ == '__main__':
    all_connected_fws()
    commit_force()
    # export_device_state()
