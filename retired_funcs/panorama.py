import re
import xml.etree.cElementTree as ET

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

from Keys import keys

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class Panorama:
    """Class contains methods to administer a Panorama"""

    def __init__(self,ip, username, password):
        """Panorama class instantiation"""

        self.ip = ip
        self.username = username
        self.password = password

    def all_connected_fws(self):
        """Gets all firewalls connected to panorama.
        Formats the XML data returned writes the firewall ip-addresses
        to a file named 'fwips.txt'
        """

        output = requests.get('https://' + self.ip + '/api/?type=op&cmd=<show>'
                              '<devices><all></all></devices></show>&key='
                              + keys.pan_vm_key(), verify=False)
        data = output.text
        root = ET.fromstring(data)
        fwips = []
        for elem in root.iter():
            if elem.tag == 'ip-address':
                node = elem
                fwip = node.text # Retrieve string format
                fwips.append(fwip)
        # return fwips
        print(fwips)

    def all_connected_fws_to_file(self):
        """Gets all firewalls connected to panorama.
        Retrieves the firewall ip-addresses and writes
        to a file named 'fwips.txt'"""

        output = requests.get('https://' + self.ip + '/api/?type=op&cmd=<show>'
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

    def commit_force(self):
        """Issues a commit to firewall"""

        cf = requests.get('https://' + self.ip + '/api/?type=commit&' + \
                          'cmd=<commit><force></force></commit>&key=' + \
                           keys.pan_vm_key(), verify=False)
        if cf.status_code == 200:
            print(f'Commit to {self.ip} successful!')


if __name__ == '__main__':
    main()
