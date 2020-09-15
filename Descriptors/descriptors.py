import keys
import datetime
import logging
import xml.etree.cElementTree as ET
import argparse

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def main():
    # Set up logging
    logger = logging.Logger('catch_all')

    args = parse_args()
    try:
        if args.ip_address and args.hour:
            hour_resource_monitor(args.ip_address, args.hour, args.output_file)
    except ValueError as e:
        logger.error(e, exc_info=True)


def parse_args():
    # Command line arguments

    parser = argparse.ArgumentParser(prog='Packet Descriptors Monitor',
                                     description="Retrieves packet descriptors on-chip utilization.",
                                     epilog='Please report any issues at'
                                            'https://github.com/zackmacharia/PaloAltoNetworks/tree/master/Descriptors')
    parser.add_argument('--ip-address', '-ip',
                        help='Firewall IP Address')
    parser.add_argument('--hour', '-hr',
                        help='Interval')
    parser.add_argument('--output-file', '-o',
                        help='Name of your output file.')
    return parser.parse_args()


def hour_resource_monitor(ip_address, hour, output_file):
    """
    Gets dataplane CPU statistics for the last hour and prints output to a file.
    """
    output = requests.get('https://' + ip_address + '/api/?type=op&cmd=<show>'
                          f'<running><resource-monitor><hour><last>{hour}</last>'
                          '</hour></resource-monitor></running></show>'
                          '&key=' + keys.firewall_api_key(), verify=False)
    data = output.text
    root = ET.fromstring(data)
    utc_time = datetime.datetime.utcnow()

    with open(output_file, mode='a+') as f:
        f.write('*****************************************' + '\n')
        f.write(str(utc_time) + ':' + ' Time is in UTC' + '\n')
        f.write('*****************************************' + '\n')
        for elem in root.iter():
            if elem.tag == 'resource-utilization':
                stats_node = elem
                for child in stats_node:
                    for item in child:
                        tag = item.tag
                        text = item.text
                        stats = tag + ' ' + ':' + ' ' + text + ' ' + '\n'
                        f.write(stats)


if __name__ == '__main__':
    main()
