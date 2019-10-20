from urllib import request
import subprocess
import api_key
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

code_version = input('Enter the target code version you want to upgrade to: ')
host = input('Enter hostname or IP: ')
if len(host) < 1:
    host = '192.168.1.100'
host_api_url = 'https://' + host + '/api/'
op_task = '?type=op&'
key = '&key=' + api_key.pa220key()


def download_latest_content():
    """Download latest content from Palo Alto Netowrks content server"""
    cmd = 'cmd=<request><content><upgrade><download><latest/>'\
        '</download></upgrade></content></request>'
    dl_latest_c = host_api_url + op_task + cmd + key
    fh = request.urlopen(dl_latest_c, context=ctx)
    global dl_content_data
    dl_content_data = fh.read().decode()
    return dl_content_data

def get_cdl_jobid():
    if 'jobid' in dl_content_data:
        pattern_o = re.compile(r'(?<=<job>)(.*)(?=</job>)')
        match_o = pattern_o.search(dl_content_data)
        global cdl_jobid
        cdl_jobid = match_o.group(0)
        return cdl_jobid
    else:
        print('Contest status progress failed; no job id found')

def show_cdl_jobid_status():
    cmd_showjb = 'cmd=<show><jobs><id>' + cdl_jobid + '</id></jobs></show>'
    get_dl_progress = host_api_url + op_task + cmd_showjb + key
    fh = request.urlopen(get_dl_progress, context=ctx)
    dl_status = fh.read().decode()
    if 'status' in dl_status:
        pattern_o = re.compile(r'(?<=<status>)(.*)(?=</status>)')
        match_o = pattern_o.search(dl_status)
        j_status = match_o.group(0)
        # print(j_status)
        return j_status

def install_latest_content():
    """Install latest content"""
    cmd = 'cmd=<request><content><upgrade><install><version>latest' + \
        '</version></install></upgrade></content></request>'
    dl_latest_c = host_api_url + op_task + cmd + key
    fh = request.urlopen(dl_latest_c, context=ctx)
    global install_content_data
    install_content_data = fh.read().decode()
    return install_content_data

def get_cinstall_j_id():
    if 'jobid' in install_content_data:
        pattern_o = re.compile(r'(?<=<job>)(.*)(?=</job>)')
        match_o = pattern_o.search(install_content_data)
        global cinstall_j_id
        cinstall_j_id = match_o.group(0)
        return cinstall_j_id
    else:
        print('Contest status progress failed; no job id found')

def show_cinstall_j_id_status():
    cmd_showjb = 'cmd=<show><jobs><id>' + cinstall_j_id + '</id></jobs></show>'
    get_install_progress = host_api_url + op_task + cmd_showjb + key
    fh = request.urlopen(get_install_progress, context=ctx)
    dl_status = fh.read().decode()
    if 'status' in dl_status:
        pattern_o = re.compile(r'(?<=<status>)(.*)(?=</status>)')
        match_o = pattern_o.search(dl_status)
        j_status = match_o.group(0)
        # print(j_status)
        return j_status

def check_now():
    """Pull software database into the firewall"""
    cmd = 'cmd=<request><system><software><check>' + \
        '</check></software></system></request>'
    checknow = host_api_url + op_task + cmd + key
    fh = request.urlopen(checknow, context=ctx)
    result = fh.read().decode()
    format_result = result.split('<')
    result = format_result[1]
    print(result[:-1])

def download_software():
    "Download software"
    cmd = 'cmd=<request><system><software><download><version>' + \
        code_version + '</version></download></software></system></request>'
    dl_software = host_api_url + op_task + cmd + key
    fh = request.urlopen(dl_software, context=ctx)
    global dl_software_data
    dl_software_data = fh.read().decode()
    return dl_software_data

def get_sdl_jobid():
    if 'jobid' in dl_software_data:
        pattern_o = re.compile(r'(?<=<job>)(.*)(?=</job>)')
        match_o = pattern_o.search(dl_software_data)
        global sdl_jobid
        sdl_jobid = match_o.group(0)
        return sdl_jobid
    else:
        print('Contest status progress failed; no job id found')

def show_sdl_jobid_status():
    cmd_showjb = 'cmd=<show><jobs><id>' + sdl_jobid + '</id></jobs></show>'
    get_dl_progress = host_api_url + op_task + cmd_showjb + key
    fh = request.urlopen(get_dl_progress, context=ctx)
    dl_status = fh.read().decode()
    if 'status' in dl_status:
        pattern_o = re.compile(r'(?<=<status>)(.*)(?=</status>)')
        match_o = pattern_o.search(dl_status)
        j_status = match_o.group(0)
        # print(j_status)
        return j_status

def install_software():
    "Install PANOS software"
    cmd = 'cmd=<request><system><software><install><version>' + \
        code_version + '</version></install></software></system></request>'
    install_software = host_api_url + op_task + cmd + key
    fh = request.urlopen(install_software, context=ctx)
    global install_software_data
    install_software_data = fh.read().decode()
    return install_software_data

def get_sw_install_jobid():
    if 'jobid' in install_software_data:
        pattern_o = re.compile(r'(?<=<job>)(.*)(?=</job>)')
        match_o = pattern_o.search(install_software_data)
        global sw_inst_jobid
        sw_inst_jobid = match_o.group(0)
        return sw_inst_jobid
    else:
        print('Contest status progress failed; no job id found')

def show_sw_install_jobid_status():
    cmd_showjb = 'cmd=<show><jobs><id>' + sw_inst_jobid + '</id></jobs></show>'
    get_sw_inst_progress = host_api_url + op_task + cmd_showjb + key
    fh = request.urlopen(get_sw_inst_progress, context=ctx)
    sw_inst_status = fh.read().decode()
    if 'status' in sw_inst_status:
        pattern_o = re.compile(r'(?<=<status>)(.*)(?=</status>)')
        match_o = pattern_o.search(sw_inst_status)
        j_status = match_o.group(0)
        # print(j_status)
        return j_status

def device_reboot():
    """Reboot device"""
    cmd_reboot = 'cmd=<request><restart><system>' + \
        '</system></restart></request>'
    reboot = host_api_url + op_task + cmd_reboot + key
    fh = request.urlopen(reboot, context=ctx)
    return fh
    # print(fh)

def ping_device():
    output = subprocess.run(['ping', '-i 30', host])
    print(output)
