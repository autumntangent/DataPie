# DataPie
A CLI tool written in Python to quickly gather/sort data, scan hosts &amp; networks and utilize OSINT for additional data gathering.  
</br>
**DATAPIE IS NOT FULLY DEVELOPED, IS STILL BEING WORKED ON AND HAS MANY MORE FEATURES TO COME.  
PLEASE TAKE NOTE THAT THE CODE IS NOT COMPLETE AND IT IS AN ACTIVE PROJECT**  
This is my first tool written in Python so bare with me, any advice is greatly appreciated!

## Requirements
Datapie was written with **UNIX** systems in mind. It has not been tested on Windows. 

Datapie is written in Python and requires Python3+.  
**NMAP** is required to be installed on your operating system to complete certain modules within the program.  
If you do not have NMAP, you just won't be able to take advantage of all the features of the program, but you will still be able to run Datapie and use the other components.  

## Installation 

git clone https://github.com/autumntangent/DataPie.git  
cd DataPie  
pip3 install -r requirements.txt  
nano/ vim config.py  (Add your specifc API keys into the config file)  
python3 DataPie.py 

## Configuration

The CONFIG.py file is the **configuration** for Datapie.py. It contains configuration information specific to YOUR version of the program, such as API Keys, lists, etc.  
Aside from the API Keys, the "Subdomains" and "Pages" lists are refferred to when running specific functions in the program, you can edit these and add or delete items.  

### API KEYS
In order for Datapie to function fully, you must provide **API KEYS** within the Datapie **CONFIG FILE** to be able to authenticate and utilize some of the web services.  

The current API KEYS needed to run every module are provided by the following:  

+ https://shodan.io 
+ https://securitytrails.com 
+ https://hunter.io 
+ https://builtwith.com 


## Features

* Gathers in Depth WHOIS information, including IP address HISTORY and DNS history
* Gathers **subdomains** for a given host
* LIVE Scrapes Target Domain for common vulnerable pages. (example: example.com/admin.php, example.com/o2auth/authorize)    
  This can be very useful when performing recon & inital penetration testing. 
* Performs LIVE "GET" requests to a list of common subdomains to initiate a connection and see what the response is
* Uses NMAP to scan a network/host for open ports, services, response headers & more
* Gathers technology data of a given website including scripts used, API integrations, javascript etc.
* Verifies email addresses 

