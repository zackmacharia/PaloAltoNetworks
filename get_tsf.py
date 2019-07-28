import requests

url = '10.200.200.1'
api_path = '/api/?type=op&cmd=<request><tech-support><dump></dump></tech-support></request>'
key = 'LUFRPT10VGJKTEV6a0R4L1JXd0ZmbmNvdUEwa25wMlU9d0N'\
    '5d292d2FXNXBBeEFBUW5pV2xoZz09'
full_url = 'https://' + url + api_path + '&key=' + key
response = (requests.get(full_url, verify=False))
print(response.status_code)
# print(full_url)
