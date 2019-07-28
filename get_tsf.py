import requests
import key

url = '10.200.200.1'
api_path = '/api/?type=op&cmd=<request><tech-support><dump></dump>'\
    '</tech-support></request>'
full_url = 'https://' + url + api_path + '&key=' + key.key
response = (requests.get(full_url, verify=False))
print(response.status_code)
# print(full_url)
