from urllib import request
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def get_api_key():
    """Request API KEY from Palo Alto Netowrks Firewall or Panorama"""
    host = input('Enter hostname or IP: ')
    req_key = 'https://' + host + \
        '/api/?type=keygen&user=zm_api&password=Nairobi1Mombasa1!'  # creds
    # print(req_key)
    fh = request.urlopen(req_key, context=ctx)
    data = fh.read().decode()
    print(host, data)


get_api_key()
