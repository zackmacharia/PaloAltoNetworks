import json
import xml.etree.ElementTree as ET
import requests
from Keys import keys


def local_run_cfg():
    """
    Request running configuration from Palo Alto Netowrks Firewall. This is only
    for the "LOCAL RUNNING" configuration not pushed from PANORAMA
    """

    host = input('Enter hostname or IP: ')
    apikey = keys.homefw2_key.strip()
    xpath = '/api/?type=op&cmd=<show><config><running></running></config></show>'\
                '&key=' + apikey
    url = 'https://' + host + xpath
    get_cfg = requests.get(url, verify=False)
    data = str(get_cfg.text)
    with open('fw_cfg.xml', mode='w') as f:
        f.write(data)

def fw_sec_rule_names(host):
    """Takes Firewall IP address as a string input. Makes an API call to
    Fireall and returns security policy names as a string."""

    # apikey = keys.sg_pa_200_key()
    apikey = keys.pa_vm_key()
    xpath = 'https://' + host + "/api/?type=config&action=get&xpath=/config/"
    xpath += "devices/entry[@name='localhost.localdomain']/vsys/entry[@name="
    xpath += "'vsys1']/rulebase/security/rules&key=" + apikey
    output = requests.get(xpath, verify=False)
    data = output.text # converts requests response into a string
    xml_data = ET.fromstring(data)
    rulenames = []
    for element in xml_data.iter('entry'):
        rulename = element.attrib
        rulenames.append(rulename['name'])
    return rulenames

def log_at_start(host):
    """Enter a DOCSTRING"""

    # apikey = keys.sg_pa_200_key()
    apikey = keys.pa_vm_key()
    rules = fw_sec_rule_names('fw_ip_address')
    for rule in rules:
    # for rule in fw_sec_rule_names('fw_ip_address'):
        xpath = "https://" + host + "/api/?type=config&action=show&xpath=/config/"
        xpath += "devices/entry[@name='localhost.localdomain']/vsys/entry[@name="
        xpath += "'vsys1']/rulebase/security/rules/entry[@name='" + rule + "']"
        xpath += "&key=" + apikey
        print(xpath)
        # output = requests.get(xpath, verify=False)
        # raw_output = output.content
        # print(raw_output) # contains log-end text 'yes'
        # data = output.text
        # xml_data = ET.fromstring(data)
        # for element in xml_data.iter('action'):
            # print(element.tag, element.attrib)
            # for subelem in element:
            #     print(subelem.tag, subelem.attrib)


        # for element in xml_data:
            # print(element.tag, element.attrib)
        # print(str_data)
        # print(type(str_data))

        # print(output)
        # data = output.text
        # data = json.l11oads(data)
        # data = output.text # requests method converts response object to string
        # print(type(data))
        # print(data)
        # print(type(data))
        # json_data = json.dumps(data)
        # print(json_data)
        # print(type(json_data))
        # print(output.content)
        # xml_data = ET.fromstring(data)
        # print(xml_data)
        # print(dir(xml_data))
        # for element in xml_data:
            # print(element.attrib)



# local_run_cfg()
# fw_sec_rule_names('fw_ip_address')
# log_at_start('fw_ip_address')
log_at_start('fw_ip_address')
