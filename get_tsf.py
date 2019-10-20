import requests
import key

# url = '10.200.200.1'
api_path = '/api/?type=op&cmd=<request><tech-support><dump></dump>'\
    '</tech-support></request>'
full_url = 'https://' + url + api_path + '&key=' + key.key
response = (requests.get(full_url, verify=False))
print(response.status_code)
print(full_url)

def generate_tsf(host):
    api_call = 'https://' + host + '/api/?type=op&cmd=<request>'
    api_call += '<tech-support><dump></dump></tech-support></request>'
    api_call += '&key=' + key.apikey.# IDEA:
    response = requests.get(api_call, verify=False)
    if response.status_code == '200':
        print('TSF for ' host, 'genereted')
    print(api_call)


generate_tsf('23.3.3.3')
