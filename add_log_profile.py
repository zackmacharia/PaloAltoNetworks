import time
import datetime
from pandevice import panorama
from pandevice import policies


def display_process_id(process_name):
    output_bytes = pano.op('show system software status', xml=True)
    output_str = output_bytes.decode('utf-8')
    output_lines = output_str.split('\n')
    for line in output_lines:
        if process_name in line:
            return line


pano = panorama.Panorama('10.46.164.193', 'zmacharia', 'paloalto')

dallas_dg = panorama.DeviceGroup('Test')  # creating device group object
pano.add(dallas_dg)  # adding device group to the panorama object

rulebase = policies.PreRulebase()
dallas_dg.add(rulebase)

rules = policies.SecurityRule.refreshall(rulebase, add=False)

print(f'Before loop: {display_process_id("configd")}')
print(f'Starting timestamp: {datetime.datetime.now()}')
t1_start = time.process_time()
for rule in rules:
    if rule.log_setting is None:
        rulebase.add(policies.SecurityRule(rule.name, log_setting='default')).create()
    rule.log_setting = None
    rule.tozone = 'L3-Untrust'
    rule.fromzone = 'L3-Trust'
    rule.apply()

t1_stop = time.process_time()
print(f'After loop: {display_process_id("configd")}')
print(f'Stopping timestamp: {datetime.datetime.now()}')
print(f'Elapsed time: {t1_stop-t1_start}')





