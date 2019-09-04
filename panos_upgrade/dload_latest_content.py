from urllib import request
import ssl
from api_key import pa220key

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def get_latest_content(host):
    """Request latest content from Palo Alto Netowrks content server"""
    
    host = input('Enter hostname or IP: ')
    if len(host) < 1:
        host = '192.168.1.1'
    host_api_url = 'https://' + host + '/api/'
    op_task = '?/type=op&'
    cmd = 'cmd=<request><content><upgrade><download><latest/>'\
        '</download></upgrade></content></request>'
    key = '&key=' + pa220key()
    dl_latest_c = host_api_url + op_task + cmd + key
    fh = request.urlopen(dl_latest_c, context=ctx)
    data = fh.read().decode()
    # return data
    print(host, data)
