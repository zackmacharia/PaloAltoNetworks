import xml.etree.cElementTree as ET
import logging

filename = input('Enter a configuration file name: ')
tree = ET.parse(filename)


def enumerate_sec_rules():
    "Function enumerates the security policies configured\
    on a Palo Alto Networks Firewall"
    
    logging.info('Enumerating security policies -- started')
    for security in tree.iter('security'):  # starts loop at the security tag
        for rules in security.iter('rules'):
            for entry in rules.iter('entry'):
                print(entry.tag, entry.attrib)
    logging.info('Enumerating security policies -- finished')


def enumerate_nat_rules():
    "Function enumerates the nat policies configured\
    on a Palo Alto Networks Firewall"
    logging.info('Enumerating nat policies -- started')
    for nat in tree.iter('nat'):  # starts loop at the nat tag
        for rules in nat.iter('rules'):
            for entry in rules.iter('entry'):
                print(entry.tag, entry.attrib)
    logging.info('Enumerating nat policies -- ended')


if __name__ == '__main__':
    # print('Security Policies')
    enumerate_sec_rules()
    # print('\n', 'Nat Policies')
    enumerate_nat_rules()
