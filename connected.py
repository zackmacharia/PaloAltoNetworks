import key
import requests
import xml.etree.cElementTree as ET

#Goal: Create a script to check for HA best practice configuration
# link monitoring, keepalives, ha1 backup, priority
# How do we scale the RE offering?

host = 'fw_ip_address'


def all_connected_fws():
    """Gets all firewalls connected to panorama.
    Formats the XML data returned writes the firewall ip-addresses
    to a file named 'fwips.txt'
    """
    output = requests.get('https://'+ host + '/api/?type=op&cmd=<show>'\
                          '<devices><all></all></devices></show>&key='\
                          + key.pan_vm_key, verify=False)
    data = output.text
    root = ET.fromstring(data)
    with open('fwips.txt', mode='a+') as f:
        for elem in root.iter():
            if elem.tag == 'ip-address':
                node = elem
                for item in node.iter():
                    fw_ip = item.text + '\n'
                    f.write(fw_ip)


def access_fws():
    with open('fwips.txt', mode='r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.rstrip()
            # print(line)
            output = requests.get('https://'+ host + '/api/?type=op&cmd='\
                                   '<show><high-availability><link-monitoring>'\
                                   '</link-monitoring></high-availability>'\
                                   '</show>&key='+ key.pa_vm_a_key, verify=False)
            print(output.text)


# all_connected_fws()
access_fws()
