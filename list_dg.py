import xml.etree.cElementTree as ET

import requests
from pandevice import panorama
from pandevice import policies
from Keys import keys

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


host = '10.46.164.193'
key = '&key=' + keys.pan_vm_key()


def dg_hierarchy_xpath():
    xpath = '/api/?type=op&cmd=<show><dg-hierarchy></'
    xpath += 'dg-hierarchy></show>'
    return xpath


def dg_api_call():
    api_xpath = 'https://' + host + dg_hierarchy_xpath() + key
    api_call = requests.get(api_xpath, verify=False)
    return api_call.text


def list_dg():
    dg_list = []
    root = ET.fromstring(dg_api_call())
    for item in root.iter():
        if 'name' in item.attrib:
            dg = item.attrib['name']
            dg_list.append(dg)
    print(dg_list)
    # return dg_list


# xpath = "/api/?type=config&action=get&xpath=/config/devices/entry[@name='localhost.localdomain']"
# xpath += "/device-group/entry[@name='"
# xpath2 = "']/pre-rulebase/security/rules"


# for device_group in list_dg():
#     api_xpath = 'https://' + host + xpath + device_group + xpath2 + key
#     api_call = requests.get(api_xpath, verify=False)
#     rules = api_call.text
#     rules_as_xml = ET.fromstring(rules)
#     # interested_data = {}
#     for item in rules_as_xml.iter():
#         # print(item.tag)
#         if item.tag == 'entry':
#             # print(item.attrib)
#         if item.tag == "log-start":
#             print('Printing', device_group, 'policies.')
#             print(item.attrib['entry'])
#         #     print(item.tag, item.attrib)

# list_dg()


if __name__ == '__main__':
    list_dg()



