import xml.etree.cElementTree as ET
from itertools import islice

import requests

from pawn import Panorama
from pawn import Firewall
from Keys import keys

pan_vm = Panorama('10.46.164.193')

panorama_connected_fws = pan_vm.all_connected_fws()

#
# ha_fw_list = []
# for fw in panorama_connected_fws:
#     pafw = Firewall(fw)
#     if pafw.get_ha_status() == 'HA is enabled':
#         ha_fw_list.append(fw)
#
#
# for fw in ha_fw_list:
#     pawfw = Firewall(fw)
#     if pawfw.check_link_monitoring_enabled() == 'Link monitoring is enabled':
#         print(fw)


# fw = '10.46.160.233'
# fw = '10.46.160.34'


def get_link_mon_group_element():
        """Check if link monitoring is enabled Run function on HA enabled fiewalls.
         Use the 'get_ha_status' to query if needed. """

        config_data = requests.get('https://' + '10.46.160.219' + '/api/?type=op&cmd=<show>'
                       '<high-availability><link-monitoring></link-monitoring>'
                      '</high-availability></show>&key=' +\
                       keys.pa_vm_key(),verify=False)
        config_data_string = config_data.text
        config_data_xml = ET.fromstring(config_data_string)

        for element in config_data_xml.iter('name'):
            if 'ethernet' not in element.text:
                print('Interface not configured')



print('\nStarting function call\n')
get_link_mon_group_element()
# check_link_mon_interfaces_in_group()
