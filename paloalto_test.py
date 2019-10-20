"""This is a test file for TESTING ONLY!!!"""

import re
import xml.etree.cElementTree as ET

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

from Keys import keys

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def platform_info(host):
    api_call = 'https://' + host + '/api/?type=op&cmd=<show><system><info></info>'
    api_call += '</system></show>&key=' + keys.pa_vm_key()
    response = requests.get(api_call, verify=False)
    if response.status_code == 200:
        apikey = keys.pa_vm_key()
        return apikey
    else:
        apikey = keys.pan_vm_key()
        return apikey

@platform_info
def commit_force(self):
    """Issues a commit to firewall"""

    cf = requests.get('https://' + self.ip + '/api/?type=commit&' + \
                      'cmd=<commit><force></force></commit>&key=' + \
                       keys.pan_vm_key(), verify=False)
    if cf.status_code == 200:
        print(f'Commit to {self.ip} successful!')
    else:
        cf = requests.get('https://' + self.ip + '/api/?type=commit&' + \
                          'cmd=<commit><force></force></commit>&key=' + \
                           keys.pa_vm_key(), verify=False)
        print(f'Commit to {self.ip} successful')


platform_info('10.46.160.82')
# platform_info('10.46.164.193')
