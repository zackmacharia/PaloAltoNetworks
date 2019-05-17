import time
import fw_upgrade


def main():
    """Uses functions in the fw_upgrade module"""
    fw_upgrade.download_latest_content()
    fw_upgrade.get_cdl_jobid()
    print('Downloading content. Please wait...')
    while True:
        time.sleep(15)  # used to reduce the number of GET requests sent
        status = fw_upgrade.show_cdl_jobid_status()
        if status == 'FIN':
            print('Download complete.')
            break
    print('Starting content install. Please wait...')
    time.sleep(3)
    fw_upgrade.install_latest_content()
    fw_upgrade.get_cinstall_j_id()
    while True:
        time.sleep(60)
        status = fw_upgrade.show_cinstall_j_id_status()
        if status == 'FIN':
            print('Content install complete.')
            break
    fw_upgrade.check_now()
    fw_upgrade.download_software()
    print('Downloading PANOS software. Please wait...')
    fw_upgrade.get_sdl_jobid()
    while True:
        time.sleep(15)  # used to reduce the number of GET requests sent
        status = fw_upgrade.show_sdl_jobid_status()
        if status == 'FIN':
            print('Successfully downloaded PANOS software.')
            break
    print('Starting PANOS software install. Please wait...')
    fw_upgrade.install_software()
    print('Installing PANOS software. Please wait...')
    time.sleep(300)  # refactor this line to use a while loop
    fw_upgrade.get_sw_install_jobid()
    while True:
        time.sleep(15)  # used to reduce the number of GET requests sent
        status = fw_upgrade.show_sw_install_jobid_status()
        if status == 'FIN':
            print('Successfully installed PAONS software.')
            break
    print('Rebooting device. Please wait...')
    fw_upgrade.device_reboot()
    print('Device going down for a reboot')
    time.sleep(5)
    print('Starting a ping to device every 30 seconds.')
    time.sleep(5)
    fw_upgrade.ping_device()


main()
