
# Instructions on how to run script in pswd
# cd to EC/utils - verify you can access the location where the py script exists by typing "ls /pwd"

import subprocess
import socket

task = input('Enter (1) to audit or (2) to edit configuration file: ')
config_file = input('Enter the configuration file name: ')
device_group = input('Enter target Device Group: ')
while True:
    module = input('Working on addresses or services? Enter (a) for addresses and (s) for services: ').lower()
    if module == 'a' or module == 's':
        break
output_file = input('Provide a name for your output file: ')


def get_container_id():
    return socket.gethostname()


def output_file_to_excel():
    """Makes sure output is in Excel format"""

    if '.xlsx' in output_file:
        return output_file
    else:
        xlsx_file = output_file + '.xlsx'
        return xlsx_file


def output_file_to_xml():
    """Makes sure output is in XML format"""

    if '.xml' in output_file:
        return output_file
    else:
        xml_file = output_file + '.xml'
        return xml_file


def copy_excel_file_from_container_to_host():
    """Copy file from Docker container to host mount"""
    
    container_path = get_container_id() + ':/Expedition-Converter/utils/' + output_file_to_excel()
    subprocess.run(['docker', 'cp', container_path, '/pwd/'])


def copy_xml_file_from_container_to_host():
    """Copy file from Docker container to host mount"""

    container_path = get_container_id() + ':/Expedition-Converter/utils/' + output_file_to_xml()
    subprocess.run(['docker', 'cp', container_path, '/pwd/'])
    

def write_to_excel_unused_svcs():
    """Retries all unused services and service-groups from Panorama Configuration File"""

    if len(device_group) <= 0:
        subprocess.run(['php', 'service-edit.php', 'in=/pwd/' + config_file, 'location=any',
                        "filter='(object is.unused.recursive)’", 'actions=exportToExcel:' + output_file_to_excel()])
    else:
        subprocess.run(['php', 'service-edit.php', 'in=/pwd/' + config_file, 'location=' + device_group,
                        "filter='(object is.unused.recursive)’", 'actions=exportToExcel:' + output_file_to_excel()])


def write_to_excel_unused_addr():
    """Retrieve all unused addresses and address-groups from Panorama Configuration File"""

    if len(device_group) <= 0:
        subprocess.run(['php', 'address-edit.php', 'in=/pwd/' + config_file, 'location=any',
                        "filter='(object is.unused.recursive)’", 'actions=exportToExcel:' + output_file_to_excel()])
    else:
        subprocess.run(['php', 'address-edit.php', 'in=/pwd/' + config_file, 'location=' + device_group,
                        "filter='(object is.unused.recursive)’", 'actions=exportToExcel:' + output_file_to_excel()])
        
        
def delete_unused_services():
    """Delete unused services and service-groups from Panorama Configuration File. Recursive is used to accommodate
    address being used in an address group e.g within a range or part of larger block"""

    if len(device_group) <= 0:
        subprocess.run(['php', 'service-edit.php', 'in=/pwd/' + config_file, 'location=any',
                        "filter='(object is.unused.recursive)’", 'actions=delete', 'out=' + output_file_to_xml()])
    else:
        subprocess.run(['php', 'service-edit.php', 'in=/pwd/' + config_file, 'location=' + device_group,
                        "filter='(object is.unused.recursive)’", 'actions=delete', 'out=' + output_file_to_xml()])
    

def delete_unused_addresses():
    """Delete unused services and service-groups from Panorama Configuration File"""

    if len(device_group) <= 0:
        subprocess.run(['php', 'address-edit.php', 'in=/pwd/' + config_file, 'location=any',
                        "filter='(object is.unused.recursive)’", 'actions=delete', 'out=' + output_file_to_xml()])
    else:
        subprocess.run(['php', 'address-edit.php', 'in=/pwd/' + config_file, 'location=' + device_group,
                        "filter='(object is.unused.recursive)’", 'actions=delete', 'out=' + output_file_to_xml()])


def export_excel_unused_services():
    write_to_excel_unused_svcs()
    copy_excel_file_from_container_to_host()


def export_excel_unused_addresses():
    write_to_excel_unused_addr()
    copy_excel_file_from_container_to_host()
        
        
def export_xml_no_unused_services():
    delete_unused_services()
    copy_xml_file_from_container_to_host()
    
    
def export_xml_no_unused_addresses():
    delete_unused_addresses()
    copy_xml_file_from_container_to_host()


def unused_objects_audit_functions():
    if module == 's':
        export_excel_unused_services()
    elif module == 'a':
        export_excel_unused_addresses()


def unused_objects_delete_functions():
    if module == 's':
        export_xml_no_unused_services()
    elif module == 'a':
        export_xml_no_unused_addresses()


if __name__ == '__main__':
    if task == '1':
        unused_objects_audit_functions()
    elif task == '2':
        unused_objects_delete_functions()
