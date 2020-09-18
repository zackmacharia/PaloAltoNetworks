from pathlib import Path
import xml.etree.cElementTree as ET


def main():
    """This functions extracts configured Administrators and their roles from a Palo Alto Networks Firewall or Panorama
    input: Firewall or Panorama XML File
    output: Text File
    """
    tree = ET.parse(config_file())
    output = {}
    admininstrators = {}
    for elem in tree.iter():
        if 'users' in elem.tag:
            users_node = elem
            for user in users_node.iter('entry'):
                admin_name = user.get('name')
                for options in user.iter('role-based'):
                    role_base_node = options
                    for role in role_base_node.iter():
                        if 'superuser' in role.tag:
                            if role.text == 'yes':
                                role = 'superuser'
                        elif 'superreader' in role.tag:
                            if role.text == 'yes':
                                role = 'superreader'
                        elif 'profile' in role.tag:
                            role = role.text
                output[admin_name] = role
    with open(output_filename(), mode='a') as f:
        for admin_name, role in output.items():
            if admin_name not in admininstrators:
                admininstrators[admin_name] = role
                f.write(admin_name + ' : ')
                f.write(role + '\n')


def check_if_file_exists(filename):
    p = Path()
    if Path(filename).exists():
        return p
    else:
        print('File does not exist. Check filename and try again.')


def config_file():
    """Checks that configuration file exists"""
    while True:
        filename = input('Enter Panorama or Firewall configuration file name: ')
        if check_if_file_exists(filename) and len(filename) > 0:
            return filename


def output_filename():
    """Formats the output file as a text file ".txt" if the extension is not provided."""
    output_file = input('Name of output file: ')
    if '.txt' not in output_file:
        output_file_ext = f'{output_file}.txt'
        return output_file_ext
    else:
        return output_file


if __name__ == '__main__':
    main()
