import requests
import re


def get_api_key():
    """Request API KEY from Palo Alto Netowrks Firewall or Panorama
    Important: change the user and password values in the lines below"""
    host = input('Enter hostname or IP: ')
    username = input('Enter username: ')
    password = input('Enter password: ')
    req_key = 'https://' + host + \
        '/api/?type=keygen&user=' + username + '&password=' + password  # creds
    data = requests.get(req_key, verify=False)
    data_string = data.text
    pattern = re.compile(r"<key>(.*?)</key>") 
    search = re.search(pattern, data_string)
    key = search.group(1) # targeting group with API key information
    print(key)


get_api_key()
