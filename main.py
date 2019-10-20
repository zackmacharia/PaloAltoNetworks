from time import sleep

from pawn import Panorama, Firewall

# pavma = Firewall('10.46.160.82', 'admin', 'paloalto')
# panvm = Panorama('10.46.164.193', 'admin', 'paloalto')
pavma = Firewall('10.46.160.82')
sgpa200 = Firewall('47.190.134.39:7443')
panvm = Panorama('10.46.164.193')

test_option = input('Enter 1 to test PAN and 2 to test FW: ')

if test_option == '1':
    print('Starting Panorama Test...')
    sleep(2)
    # panvm.all_connected_fws()
    # panvm.commit_force()
    # panvm.all_connected_fws_to_file()
    # panvm.generate_tsf()
elif test_option == '2':
    print('Starting Firewall Test...')
    sleep(2)
    # pavma.get_api_key()
    sgpa200.descriptors_on_chip_to_file()
    # pavma.commit_force()
    # pavma.generate_tsf()
else:
    print('No Tests Run')
