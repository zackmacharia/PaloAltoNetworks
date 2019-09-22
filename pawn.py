import re
import xml.etree.cElementTree as ET

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

from Keys import keys

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class pawn():
    """Base class for firewall and Panorama class"""

    def __init__(self,ip):
        """PAWN class instantiation"""

        self.ip = ip
        self.fw_key = keys.pa_vm_key()
        self.pan_key = keys.pan_vm_key()

    def commit_force(self):
        """Issues a commit to firewall"""

        xpath = 'https://' + self.ip + '/api/?type=commit&'
        xpath += 'cmd=<commit><force></force></commit>&key='
        fw_api_call = xpath + self.fw_key
        pan_api_call = xpath + self.pan_key
        response = requests.get(fw_api_call, verify=False)
        if response.status_code == 200:
            print(f'Commit for Firewall ', self.ip, 'successful')
        else:
            response = requests.get(pan_api_call, verify=False)
            print(f'Commit for Panorama ', self.ip, 'successful')

        # cf = requests.get('https://' + self.ip + '/api/?type=commit&' + \
        #                   'cmd=<commit><force></force></commit>&key=' + \
        #                    keys.pan_vm_key(), verify=False)
        # if cf.status_code == 200:
        #     print(f'Commit to {self.ip} successful!')
        # else:
        #     cf = requests.get('https://' + self.ip + '/api/?type=commit&' + \
        #                       'cmd=<commit><force></force></commit>&key=' + \
        #                        keys.pa_vm_key(), verify=False)
        #     print(f'Commit to {self.ip} successful')

    def get_api_key(self):
        """Request API KEY from Palo Alto Netowrks Firewall or Panorama
        Important: change the user and password values in the lines below"""

        req_key = 'https://' + self.ip + \
            '/api/?type=keygen&user=' + self.username + '&password=' + self.password  # creds
        data = requests.get(req_key, verify=False)
        data_string = data.text
        pattern = re.compile(r"<key>(.*?)</key>")
        search = re.search(pattern, data_string)
        key = search.group(1) # targeting group with API key information
        print(key)

    def generate_tsf(self):
        xpath = 'https://' + self.ip + '/api/?type=op&cmd=<request>'
        xpath += '<tech-support><dump></dump></tech-support></request>&key='
        fw_api_call = xpath + self.fw_key
        pan_api_call = xpath + self.pan_key
        response = requests.get(fw_api_call, verify=False)
        if response.status_code == 200:
            print(f'TSF for Firewall ', self.ip, 'generated')
        else:
            response = requests.get(pan_api_call, verify=False)
            print(f'TSF for Panorama ', self.ip, 'generated')


class Panorama(pawn):

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


class Firewall(pawn):
    pass


if __name__ == '__main__':
    main()
