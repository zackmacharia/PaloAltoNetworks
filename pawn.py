import datetime
import getpass
import re
import time
import xml.etree.cElementTree as ET

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

from Keys import keys

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class Pawn():
    """Base class for Firewall and Panorama class"""

    def __init__(self, ip):
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

    def get_api_key(self):
        """Request API KEY from Palo Alto Netowrks Firewall or Panorama
        Important: change the user and password values in the lines below"""

        username = input('Username:')
        password = getpass.getpass(prompt='Password: ')
        req_key = 'https://' + self.ip + '/api/?type=keygen&user='
        req_key += username + '&password=' + password  # creds
        data = requests.get(req_key, verify=False)
        data_string = data.text
        pattern = re.compile(r"<key>(.*?)</key>")
        search = re.search(pattern, data_string)
        key = search.group(1) # targeting group with API key information
        print(key)

    def generate_tsf(self):
        """Generate Tech Support File"""

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


class Panorama(Pawn):
    """Panorama class"""

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
        return fwips
        # print(fwips)

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


class Firewall(Pawn):
    """Firewall class"""

    def descriptors_on_chip_to_file(self, interval='12'):
        """Get Packet Descriptors on Chip CPU percentage and writes output
        to a text file name *packet_descriptors.txt*; default interval
        value is 12 hours. NICE TO HAVE: Print only the average numbers"""

        self.interval = interval

        output = requests.get('https://'+self.ip+'/api/?type=op&cmd=<show>'\
                              '<running><resource-monitor><hour><last>' + \
                              self.interval + '</last></hour></resource-monitor>'\
                              '</running></show>&key='+keys.sg_pa_200_key(), \
                              verify=False)
        if output.status_code == 200:
            print('Succesfully Connected to', self.ip)
            data = output.text
            root = ET.fromstring(data)
            date = datetime.datetime.now()
            utc_time = datetime.datetime.utcnow()
            time.sleep(1)
            print('Writing data to file')
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
        else:
            print('Failed to connect to' + self.ip + '. No files written.')

        # data = output.text
        # print(data)
        # root = ET.fromstring(data)
        # date = datetime.datetime.now()
        # utc_time = datetime.datetime.utcnow()

        # with open('packet_descriptors.txt', mode='a+') as f:
        #     f.write('*****************************************' + '\n')
        #     f.write(str(utc_time) + ':' + ' Time is in UTC' + '\n')
        #     f.write('*****************************************' + '\n')
        #     for elem in root.iter():
        #         if elem.tag == 'resource-utilization':
        #             stats_node = elem
        #             for child in stats_node:
        #                 for item in child:
        #                     tag = item.tag
        #                     text = item.text
        #                     stats = tag + ' ' + ':' + ' ' + text + ' ' + '\n'
        #                     f.write(stats)


# fw = Firewall('47.190.134.39')
#
# fw.descriptors_on_chip_to_file()
