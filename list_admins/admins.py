import xml.etree.cElementTree as ET

filename = input('Enter a configuration file name: ')
tree = ET.parse(filename)
admins = list()
set_admin = set()


def get_admin_info():
    """This functions gets the configured administrators and their roles on a
    Palo Alto Networks Firewall"""
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
                # print('Administrator: ', admin_name, '-', 'Role: ', role)
                with open('admin_file.txt', mode='a') as f:
                    f.write(admin_name + ' : ')
                    f.write(role + '\n')


get_admin_info()
