# prismaAccessIPRetriever.py
This script make API calls to Palo Alto Networks GlobalProtect Cloud Service and provides an option to print out 
the results on console or write results to a file.  

## Requirements
Python3
Virtual Environment - optional but recommended    

## Usage Guidelines:
Update the secrets.py file with your API key.  
If decide to store the key.py in a different directory from where the descriptors.py file is located make sure you make modifications to the code with the full path.

## Example: Running the script
Change directory to where your script is located  
*python prismaAccessIPRetriever.py <flags>*    
Run *python prismaAccessIPRetriever.py --help* to view all options available 

## Output
Check the "my-file-output" file