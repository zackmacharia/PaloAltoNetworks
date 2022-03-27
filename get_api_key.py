import requests
import getpass
import re


class Firewall:

    def __init__(self, ip):
        """Class instantiation"""
        
        self.ip = ip
        # self.username = 'admin'
        self.username = 'zmacharia'
        self.password = 'paloalto'

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


pavma = Firewall('fw_ip_address')
pavma.get_api_key()
