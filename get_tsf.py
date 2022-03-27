import requests
from Keys import keys

url = 'fw_ip_address'
api_path = '/api/?type=op&cmd=<request><tech-support><dump></dump>'\
    '</tech-support></request>'
full_url = 'https://' + url + api_path + '&key=' + keys.pa_vm_key()
response = (requests.get(full_url, verify=False))
print(response.status_code)
print(full_url)


def generate_tsf(host):
    api_call = 'https://' + host + '/api/?type=op&cmd=<request>'
    api_call += '<tech-support><dump></dump></tech-support></request>'
    api_call += '&key=' + key.apikey.pa
    response = requests.get(api_call, verify=False)
    if response.status_code == '200':
        print('TSF genereted')
    print(api_call)


generate_tsf('fw_ip_address')

# def from_file_extract_ips():
#     """Reads a file with ip addresses and returns a list of IPs"""
#
#     ip_dict = {}
#     text_file = input('Enter the name of the text file: ')
#     # # print('Source File as is', source_file)
#     if '.txt' not in text_file:
#         source_file = text_file + '.txt'
#     #     print('Source File: ', source_file)
#         # print('Source File Modified', source_file)
#     # source_file == source_file or source_file + '.txt'
#     with open(source_file, mode='r') as f:
#         for line in f.readlines():
#             ip_address = line.rstrip()
#             ip_name = 'addr-' + line.split('/')[0]
#             ip_dict[ip_name] = ip_address
#     print(ip_dict)
#
# from_file_extract_ips()
