import re
import xml.etree.cElementTree as ET

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

from Keys import keys

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class Firewall:
    """Class contains methods to administer a Firewall"""

    def __init__(self, ip, username, password):
        """Firewall class instantiation"""

        self.ip = ip
        self.username = username
        self.password = password

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

    def commit_force(self):
        """Issues a commit to firewall"""
        cf = requests.get('https://' + self.ip + '/api/?type=commit&' + \
                          'cmd=<commit><force></force></commit>&key=' + \
                           keys.pa_vm_key(), verify=False)
        if cf.status_code == 200:
            print(f'Commit to {self.ip} successful!')


if __name__ == '__main__':
    main()
