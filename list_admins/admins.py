import xml.etree.cElementTree as ET

tree = ET.parse('fw1.xml')
root = tree.getroot()   # function used to get the root


class Admininstrators:
    """ Used multiple FOR loops from root to and used Index to create the class
    variables [mgmt_config, users]
    """
    mgt_config = root[0]
    users = mgt_config[0]
    admin_perm = users[0]

    def get_admins():
        for user in Admininstrators.users:
            name_dict = user.attrib
            admin_name = name_dict['name']
            print(admin_name)


Admininstrators.get_admins()
