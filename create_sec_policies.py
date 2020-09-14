import xml.etree.ElementTree as ET
from pandevice import panorama
from pandevice import policies

pano = panorama.Panorama('10.46.164.193', 'zmacharia', 'paloalto')


def display_process_id(process_name):
    output_bytes = pano.op('show system software status', xml=True)
    output_str = output_bytes.decode('utf-8')
    output_lines = output_str.split('\n')
    for line in output_lines:
        if process_name in line:
            return line


display_process_id('configd')

test_dg = panorama.DeviceGroup('Test2')  # creating device group object
pano.add(test_dg)  # adding device group to the panorama object

rulebase = policies.PreRulebase()  # this is a PreRulebase container
test_dg.add(rulebase)  # adding the container object to the device group

for rule_number in range(1,1801):
    rule_parameters = ['test'+str(rule_number), 'L3-Trust', 'L3-Untrust', 'allow']
    new_rule = policies.SecurityRule(name=rule_parameters[0],
                                     fromzone=rule_parameters[1],
                                     tozone=rule_parameters[2],
                                     action=rule_parameters[3])
    rulebase.add(new_rule)
    new_rule.create()

