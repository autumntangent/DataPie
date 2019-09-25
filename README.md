# DataPie
A CLI tool written in Python to quickly gather/sort data, scan hosts &amp; networks and utilize OSINT for additional data gathering.  
</br>
### DATAPIE IS NOT FULLY DEVELOPED, IS STILL BEING WORKED ON AND HAS MANY MORE FEATURES TO COME.  
### PLEASE TAKE NOTE THAT THE CODE IS NOT COMPLETE AND ITS AN ACTIVE PROJECT. 
This is my first tool written in Python so bare with me, any advice is greatly appreciated!

## Requirements
Datapie was written with **UNIX** systems in mind. It has not been tested on Windows. 

Datapie is written in Python and requires Python3+.  
**NMAP** is required to be installed on your operating system to complete certain modules within the program.  
If you do not have NMAP, you just won't be able to take advantage of all the features of the program, but you will still be able to run Datapie and use the other components.

### API KEYS
In order for Datapie to function fully, you must provide an API KEY within the Datapie Configuration to be able to authenticate and utilize some of the web services.

## Installation 

git clone https://github.com/autumnxxtang3nt/DataPie.git  
cd DataPie  
pip3 install -r requirements.txt  
python3 DataPie.py  

## Features

* Gathers in Depth WHOIS information, including IP address HISTORY and DNS history
* Gathers **subdomains** for a given host
* Scrapes Target Domain for common vulnerable pages. (example: example.com/admin.php, example.com/o2auth/authorize)    
  This can be very useful when performing recon & inital penetration testing. 
