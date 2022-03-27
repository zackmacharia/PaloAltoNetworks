from time import sleep

from pawn import Panorama, Firewall


pavma = Firewall('fw_ip_address')
sgpa200 = Firewall('fw_ip_address')
panvm = Panorama('pano_ip_address')

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
