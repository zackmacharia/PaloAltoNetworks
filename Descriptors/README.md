# descriptor.py
This script makes an API call to a firewall.  
Gathers the resource-monitor statistics for the last hour.  
Parses the data to retrieve CPU utilization for packet descriptors on chip.  
Writes the data in a text file.

## Requirements
Python3
Virtual Environment (Optional but recommended)
Requests Module - https://requests.readthedocs.io/en/master/user/install/#install  

## Example:
Edit script by replacing the following:
### descriptor.py
host = 'fw_ip_address' to host = '192.168.0.1'
### keys.py
return 'YOUR_FIREWALL_API_KEY' to return 'fereig#ehraih=be3h8'

CD to the directory where your script is located and run 'python descriptors.py'

## Output
Check the "packet_descriptors.txt" file

