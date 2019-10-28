import pyfiglet
import requests
import os
import sys
from colorama import Fore, Back, Style
import shodan
import json
from time import sleep
import urllib3

#Banner

from pyfiglet import Figlet

BRI = Style.BRIGHT
RED = Fore.RED
GREEN = Fore.GREEN
BLUE = Fore.BLUE
RES = Style.RESET_ALL
YELLOW = Fore.YELLOW

#CLASS DEFINING ALL MENUS AND SUBMENUS

class menu():
	def main_banner():
		print(GREEN)
		custom_fig = Figlet(font='doom')
		print(custom_fig.renderText('DATA.PIE'))

	def main_menu():
		print(BRI, GREEN + '\n\n\n::MAIN MENU::\n\n\tENTER [1] DOMAIN SCANNING\n\tENTER [2] FOR NMAP SCANS & NETWORK INFO\
		\n\tENTER [3] TO GATHER EMAIL & ORGANIZATION DATA\n\tENTER [4] FOR SHODAN\n\tENTER [5] TO EXIT\n')
		print(RES)


	def sub_1():
		print(BRI, BLUE + '\n\n::DOMAIN SCANNING OPTIONS::\n\n\t\tENTER [1] FOR HEADER CAPTURE\n\
		ENTER [2]FOR WHOIS INFO\n\t\tENTER [3] TO SCRAPE WEB PAGES\n\t\tENTER [0] TO RETURN TO THE MAIN MENU\n')
		print(RES)

	def sub_3():
		print(BRI, BLUE + "\n\n::EMAIL & ORGANIZATION SPECIFIC DATA::\n\
		\n\n\tENTER [1] TO VERIFY AN EMAIL ADDRESS\n\tENTER [0] TO RETURN TO THE MAIN MENU\n")

	def n_menu():
		print(YELLOW + '\nNMAP SCANNING OPTIONS\n\nENTER [1] FOR A FULL PORT SCAN\
		\nENTER [2] FOR A BASIC QUICK SCAN\nENTER [3] TO NMAP SCAN WITH YOUR OWN CUSTOM OPTIONS\
		\nENTER [0] TO RETURN TO MAIN MENU\n\n')
		print(RES)

#NMAP CLASS FUNCTIONS

class nmap():
	def nmap_scan_ports():
		print('SCANNING ' + (ip) + '\n\nSCANNING ALL PORTS FOR SERVICES AND REACHABILITY\nTHIS MAY TAKE A MINUTE...\n\n')
		os.system(('nmap -v -PS -p- -T4 --reason -sV -Pn ') + (ip))

	def nmap_basic():
		print('SCANNING ' + (ip))
		os.system(('nmap -v -PS -sV -Pn ') + (ip))

	def nmap_custom():
		print('SCANNING ' + (ip) + 'WITH CUSTOM SCRIPTS\nTHIS CAN TAKE A WHILE DEPENDING ON\
		\nTHE SCRIPTS CHOSEN\n')
		print('USING THE FOLLOWING SCRIPTS:' + scripts)
		os.system(('nmap -v --reason -sV -Pn ') + (ip) + (scripts))


def scrape(url):
	for y in url:
		url = ('http://' + host + y)
		rq = requests.request("GET", url)
		c = rq.status_code
		success = 'SUCCESSFUL, PAGE EXISTS'
		fail = 'ERROR, PAGE NOT AVAILABLE'
		print(url, c)
		if c == 200: 
			print(GREEN + success)
		else:
			print(RED + fail)
		print(RES)

def subdomain_brute(url):
	for x in url:
		url = ('https://' + x + host)
		r = requests.request("GET", url)
		c = r.status_code
		success = 'SUCCESSFUL, PAGE EXISTS'
		fail = 'ERROR, PAGE NOT AVAILABLE'
		print(url, c)
		if c == 200:
			print(GREEN + success)
		else:
			print(RED + fail)
		print(RES)


#IMPORTING DATA FROM CONFIG FILE

from config import API_KEYS
from config import SUBDOMAINS
from config import PAGES
from config import BASE_ENDPOINTS


menu.main_banner()
print(RED + BRI)
input('PRESS ANY KEY TO CONTINUE...\n\n\n')
print(RES)
menu.main_menu()
xkey = input()
while xkey != '5':
		if xkey == '1':
			menu.sub_1()
			optd = input()
			while optd != '0':
				if optd == '1':
					print(BRI + 'ENTER HOST/DOMAIN NAME TO BEGIN SCANNING')
					print(RES)
					host = input()
					url = 'https://' + host
					try:
						x = requests.get(url)
						if x.status_code == 200:
							print(BRI, GREEN + 'SUCCESSFUL CONNECTION. STATUS CODE RETURNED IS\n\n')
							print(x.status_code)
							print('\n\nHEADERS RETURNED AS:\n\n')
							print(x.headers)
						else:
							print(RED + 'AN ERROR HAS OCCURED\n STATUS CODE RETURNED IS'\
							+ x.status_code + x.text)
							print(RES)
					except:
							print(BRI, RED + 'ERROR IN COMPLETING THIS MODULE')
							print('PLEASE INPUT ANOTHER HOSTNAME')
							print(RES)
							host = input()
							url = 'https://' + host
							try:
								x = requests.get(url)
								print(x.headers)
							except:
								print('CANNOT COMPLETE MODULE. ERROR RETURNED')
							finally:
								print(RES)
								break
							
				if optd == '2':
					print(BRI + 'ENTER HOST NAME TO BEGIN SCANNING')	
					host = input()
					akey = API_KEYS["sectrails"]
					st = BASE_ENDPOINTS["st"]

					if not akey:
						print (BRI + RED + 'MISSING SECURITY TRAILS API KEY.\nPLEASE PROVIDE PROPER API AUTHENTICATION AND RUN AGAIN\n')
					else:
						url = "{0}/v1/history/{1}/whois".format(st, host)
						querystring = {"apikey":"{0}".format(akey)}

						response = requests.request("GET", url, params=querystring)
						print(response.text)
						print(GREEN + 'SEARCHING FOR SUBDOMAINS...')
						url = "{0}/v1/domain/{1}/subdomains".format(st, host)
						querystring = {"apikey":"{0}".format(akey)}
						response = requests.request("GET", url, params=querystring)
						print(response.text)
						print(GREEN + 'GATHERING DATA...')
						url = "{0}/v1/domains/{1}/list/".format(st, host)
						querystring = {"apikey":"{0}".format(akey)}
						response = requests.request("GET", url, params=querystring)
						print(response.text)
						print()
						print('SCANNING...')
						url = "{0}/v1/history/{1}/dns/a".format(st, host)
						querystring = {"apikey":"{0}".format(akey)}
						response = requests.request("GET", url, params=querystring)
						print(response.text)
						print(RES)

				if optd == '3':
					print('ENTER DOMAIN NAME TO SCRAPE')
					host = input()
					scrape(PAGES)

				validopts = ["0", "1", "2", "3", "4"]
				if optd not in validopts:
					print(RED + 'INVALID KEY, PLEASE SELECT AN OPTION FROM THE MENU!')
					print(RES)
			
				menu.sub_1()
				optd = input()


		if xkey == '2':
			menu.n_menu()
			nkey = input()
			while nkey != '0':
				if nkey == '1':
					print('ENTER IP ADDRESS TO BEGING SCANNING...')
					ip = input()
					print('SCANNING ALL PORTS. THIS MAY TAKE A FEW MINUTES')
					nmap.nmap_scan_ports()
				if nkey == '2':
					print('ENTER THE IP ADDRESS OF HOST TO BEGIN SCANNING')
					ip = input()
					nmap.nmap_basic()
				if nkey == '3':
					print('ENTER THE IP ADDRESS TO BEGIN SCAN')
					ip = input()
					print('ENTER THE NAME OF THE SCRIPT YOU WOULD LIKE TO USE DURING THE SCAN')
					scr = input()
					scripts = ' --script=' + scr
					nmap.nmap_custom()
				menu.n_menu()
				nkey = input()



		if xkey == '3':
			from pyhunter import PyHunter
			hk = API_KEYS["hunter"]
			menu.sub_3()
			ek = input()
			while ek != '0':
				if ek == '1':
					if not hk:
						print(RED + "MISSING HUNTER API KEY. CANNOT COMPLETE THIS MODULE")
						print(RES)
						break
					else:
						print(RED + "ENTER AN EMAIL ADDRESS TO VERIFY")
						print(RES)
						email = input()
						x = email
						hunter = PyHunter(hk)
						h = hunter.email_verifier(x)
						print(GREEN, BRI)
						print(h)
						print(RES)
					break

			
		if xkey == '4':
			print('ENTER HOSTNAME TO SCAN AND GATHER DATA ON')
			host = input()
			shkey = API_KEYS["shodan_key"]
			if not shkey:
				print(RED + '\nMISSING SHODAN API KEY, RETURNING TO MAIN MENU')
				print(RES)
			else:
				shodan = shodan.Shodan(shkey)
				results = shodan.search(host)
				print(results)

				print('ENTER IP OF HOST')
				ip = input()
				ipres = shodan.host(ip)
				print(ipres)



		menu.main_menu()
		xkey = input()
