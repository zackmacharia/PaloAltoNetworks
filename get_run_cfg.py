import xml.etree.ElementTree as ET
import requests
import keys


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


local_run_cfg()
