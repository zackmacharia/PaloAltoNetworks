import xml.etree.cElementTree as ET

tree = ET.parse('fw1.xml')
root = tree.getroot()   # function used to get the root

mgt_config = root[0]
users = mgt_config[0]


def get_admins():
    """This functions iterates over the configured Administrators on
    the firewall and prints out the admin name and their permissions"""
    for user in users.iter('entry'):  # iterating through users children
        # print(user.tag, user.attrib)  # output validation
        admin_name = user.get('name')  # using get due to assignment = value
        print(admin_name)  # output validation
        for permission in user.iter('permissions'):
            for role_base in permission.iter('role-based'):
                for role in role_base:
                    if role.tag == 'superuser':
                        print('superuser')
                    else:
                        for custom_role in role.iter('custom'):
                            for profile in custom_role.iter('profile'):
                                admin_role = profile.text
                                print(admin_role)


get_admins()
