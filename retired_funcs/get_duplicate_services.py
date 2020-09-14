import xml.etree.cElementTree as ET
import xlsxwriter

filename = input('Enter a configuration file name: ')
output_file = input('Output file name: ')
device_group = input('Device Group: ')

if len(filename) <= 0:
    filename = '02152020testfile.xml'

if len(device_group) <= 0:
    device_group = 'shared'

config = ET.parse(filename).getroot()


def shared_service_node():
    """Access xpath for shared service node"""

    return config.findall('./shared/service/')


def dg_service_node():
    """Access xpath for a device group service node. Device group name is provided by user input"""

    dg_service_xpath = "./devices/entry[@name='localhost.localdomain']/device-group/entry[@name='" + device_group + \
                       "']/service/"
    return config.findall(dg_service_xpath)


def get_shared_service_names():
    """Retrieves the name of all services in shared"""

    shared_svc_names = []
    for values in shared_service_node():
        name = values.attrib['name']
        shared_svc_names.append(name)
    return shared_svc_names


def get_dg_service_names():
    """Retrieves the name of all services in a device group"""

    dg_svc_names = []
    for values in dg_service_node():
        name = values.attrib['name']
        dg_svc_names.append(name)
    return dg_svc_names


def get_shared_service_values():
    """Retrieves the name of all service values in shared"""

    shared_svc_values = []
    for values in shared_service_node():
        protocol, port = values[0][0].tag, values[0][0][0].text
        port_number = protocol + '/' + port
        shared_svc_values.append(port_number)
    return shared_svc_values


def get_dg_service_values():
    """Retrieves the name of all service values in a device group"""

    dg_svc_values = []
    for values in dg_service_node():
        protocol, port = values[0][0].tag, values[0][0][0].text
        port_number = protocol + '/' + port
        dg_svc_values.append(port_number)
    return dg_svc_values


def check_dups_in_list(list_name):
    """Check for duplicates entries in a list"""

    if len(list_name) == len(set(list_name)):
        return False
    else:
        print('Error: Duplicates service names found!')


def create_shared_service_dict():
    """Create a dictionary of shared services if no duplicate names exists."""

    if check_dups_in_list(get_shared_service_names()) is False:
        shared_service_dict = dict(zip(get_shared_service_names(), get_shared_service_values()))
        return shared_service_dict


def create_dg_service_dict():
    """Create a dictionary of services in a device group if no duplicate names exists."""

    if check_dups_in_list(get_dg_service_names()) is False:
        dg_service_dict = dict(zip(get_dg_service_names(), get_dg_service_values()))
        return dg_service_dict


def shared_service_dup_values():
    """Determine duplicate values in shared"""

    track_values = []
    dup_values = []
    for k, v in create_shared_service_dict().items():
        if v not in track_values:
            track_values.append(v)
        else:
            dup_values.append(v)
    return dup_values


def dg_service_dup_values():
    """Determine duplicate values in shared"""

    track_values = []
    dup_values = []
    for k, v in create_dg_service_dict().items():
        if v not in track_values:
            track_values.append(v)
        else:
            dup_values.append(v)
    return dup_values


def export_duplicate_shared_service_to_excel():
    """Write service names with duplicate values in shared to Excel"""

    workbook = xlsxwriter.Workbook(output_file)
    worksheet = workbook.add_worksheet()
    row = 0
    for k, v in create_shared_service_dict().items():
        if v in shared_service_dup_values():
            worksheet.write(row, 0, k)
            worksheet.write_string(row, 1, v)
            row += 1
    workbook.close()


def export_duplicate_dg_service_to_excel():
    """Write service names with duplicate values in a device group to Excel"""

    workbook = xlsxwriter.Workbook(output_file)
    worksheet = workbook.add_worksheet()
    row = 0
    for k, v in create_dg_service_dict().items():
        if v in dg_service_dup_values():
            worksheet.write(row, 0, k)
            worksheet.write_string(row, 1, v)
            row += 1
    workbook.close()


if __name__ == '__main__':
    if device_group == 'shared':
        export_duplicate_shared_service_to_excel()
    else:
        export_duplicate_dg_service_to_excel()
