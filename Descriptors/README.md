# descriptor.py
This script makes an API call to a firewall, gathers the resource-monitor statistics for the last hour, parses the data to retrieve CPU utilization for packet descriptors on-chip, and then writes the data in a text file.

## Requirements
Python3
Virtual Environment (Optional but recommended)  
Requests Module - https://requests.readthedocs.io/en/master/user/install/#install  

## Usage Guidelines:
Update the key.py file with your API key.  
If decide to store the key.py in a different directory from where the descriptors.py file is located make sure you make modifications to the code with the full path.

## Example: Running the script
Change directory to where your script is located  
python descriptors.py -ip 192.168.0.1 --hour 2 -o my-file-output  

## Output
Check the "my-file-output" file

