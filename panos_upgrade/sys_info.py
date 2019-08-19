from urllib import request
import ssl
import api_key

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def get_sys_info(host):
    """Request System Info from Palo Alto Netowrks Firewall or Panorama"""
    host = input('Enter hostname or IP: ')
    sysinfo = 'https://' + host + \
        '/api/?type=op&cmd=<show><system><info></info></system></show>&key=' +\
              api_key.pa220key()
    fh = request.urlopen(sysinfo, context=ctx)
    data = fh.read().decode()
    print(host, data)


get_sys_info('192.168.1.1')
