from urllib import request
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def get_api_key():
    """Request API KEY from Palo Alto Netowrks Firewall or Panorama
    Important: change the user and password values in the lines below"""
    host = input('Enter hostname or IP: ')
    username = input('Enter username: ')
    password = input('Enter password: ')
    req_key = 'https://' + host + \
        '/api/?type=keygen&user=' + username + '&password=' + password  # creds
    # print(req_key)
    fh = request.urlopen(req_key, context=ctx)
    data = fh.read().decode()
    print(host, data)


get_api_key()
