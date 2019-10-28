import pyfiglet
import requests
import os
import sys
import shodan
import json
from time import sleep
import urllib3
from settings import Greetings, Style
from pyfiglet import Figlet

#CLASS DEFINING ALL MENUS AND SUBMENUS

class menu():
	def main_banner():
		custom_fig = Figlet(font='doom')
		Style.Colors.GB((custom_fig.renderText('DATA.PIE')))
		Style.RST()

	def main_menu():
		Style.Colors.GB('\n\n\n::MAIN MENU::\n\n\tENTER [1] DOMAIN SCANNING\n\tENTER [2] FOR NMAP SCANS & NETWORK INFO\
		\n\tENTER [3] TO GATHER EMAIL & ORGANIZATION DATA\n\tENTER [4] FOR SHODAN\n\tENTER [9] TO CHANGE API KEYS\n\tENTER [5] TO EXIT\n')
		Style.RST()


	def sub_1():
		Style.Colors.M('\n\n::DOMAIN SCANNING OPTIONS::\n\n\t\tENTER [1] FOR HEADER CAPTURE\n\
		ENTER [2]FOR WHOIS INFO\n\t\tENTER [3] TO SCRAPE WEB PAGES\n\t\tENTER [4] FOR HOST LINK & TECHNOLOGY SCANNING\
		\n\t\tENTER [0] TO RETURN TO THE MAIN MENU\n')
		Style.RST()

	def sub_3():
		print("\n\n::EMAIL & ORGANIZATION SPECIFIC DATA::\n\
		\n\n\tENTER [1] TO VERIFY AN EMAIL ADDRESS\n\tENTER [0] TO RETURN TO THE MAIN MENU\n")

	def n_menu():
		Style.Colors.M('\nNMAP SCANNING OPTIONS\n\nENTER [1] FOR A FULL PORT SCAN\
		\nENTER [2] FOR A BASIC QUICK SCAN\nENTER [3] TO NMAP SCAN WITH YOUR OWN CUSTOM OPTIONS\
		\nENTER [0] TO RETURN TO MAIN MENU\n\n')
		Style.RST()

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

	def tcp_trace():
		Style.Colors.C('ATTEMPTING TCP CONNECT TO ' + ip )
		os.system(('nmap -v -sT -Pn ') + (ip) + (' --packet-trace --script-trace'))

#CLASS FOR CONFIGURING AND VIEWING THE SESSIONS SAVED API KEYS

class keys():
	def show():
		Style.Colors.G("URRENT SESSION API KEYS:")
		Style.RST()
		for x, y in API_KEYS.items():
			if not y:
				Style.Colors.BB(x),Style.Colors.R("NO KEY FOUND!!")
			else:
				Style.Colors.BB(x + " : " + y)

	def change():
		Style.Colors.G("\n\nENTER THE KEY NAME TO ADD OR CHANGE IT\n")
		key = input()
		while key != '0':
			a = key
			if a in API_KEYS:
				b = API_KEYS.get(a)
				print("\nREADY TO CHANGE THE KEY FOR " + a.upper())
				Style.Colors.BB("ENTER THE NEW KEY TO SAVE FOR " + a.upper())
				z = input()
				API_KEYS[(a)] = z
				print("\033[0;36mKEY FOR " + a.upper() + " CHANGED SUCCESSFULLY! KEY SET TO " + API_KEYS[(a)])
			else:
				Style.Colors.R("ERROR... PLEASE SELECT A KEY TO CONFIGURE FROM THE LISTING...\n")
			keys.show()
			Style.Colors.G("\n\nENTER THE KEY NAME TO ADD OR CHANGE IT\n")
			key = input()

def scrape(url):
	for y in url:
		url = ('https://' + host + y)
		rq = requests.request("GET", url)
		c = rq.status_code
		success = 'SUCCESSFUL, PAGE EXISTS'
		fail = 'ERROR, PAGE NOT AVAILABLE'
		print(url, c)
		if c == 200: 
			Style.Colors.G(success)
		else:
			Style.Colors.RB(fail)
		Style.RST()

def subdomain_brute(url):
	for x in url:
		url = ('https://' + x + host)
		r = requests.request("GET", url)
		c = r.status_code
		success = 'SUCCESSFUL, PAGE EXISTS'
		fail = 'ERROR, PAGE NOT AVAILABLE'
		print(url, c)
		if c == 200:
			Style.Colors.G(success)
		else:
			Style.Colors.RB(fail)
		Style.RST()


#IMPORTING DATA FROM CONFIG FILE

from config import API_KEYS
from config import SUBDOMAINS
from config import PAGES
from config import BASE_ENDPOINTS


menu.main_banner()
Style.Colors.R("")
input("PRESS ANY KEY TO CONTINUE...\n\n")
Style.RST()
menu.main_menu()
xkey = input()
while xkey != '5':
		if xkey == '1':
			menu.sub_1()
			optd = input()
			while optd != '0':
				if optd == '1':
					print('ENTER HOST/DOMAIN NAME TO BEGIN SCANNING')
					Style.RST()
					host = input()
					url = 'https://' + host
					try:
						x = requests.get(url)
						if x.status_code == 200:
							Style.Colors.GB('SUCCESSFUL CONNECTION. STATUS CODE RETURNED IS\n\n')
							print(x.status_code)
							print('\n\nHEADERS RETURNED AS:\n\n')
							print(x.headers)
						else:
							Style.Colors.RB('AN ERROR HAS OCCURED\n STATUS CODE RETURNED IS'\
							+ x.status_code + x.text)
							Style.RST()
					except:
							Style.Colors.RB('ERROR IN COMPLETING THIS MODULE')
							print('PLEASE INPUT ANOTHER HOSTNAME')
							Style.RST()
							host = input()
							url = 'https://' + host
							try:
								x = requests.get(url)
								print(x.headers)
							except:
								print('CANNOT COMPLETE MODULE. ERROR RETURNED')
							finally:
								Style.RST()
								break
							
				if optd == '2':
					print('ENTER HOST NAME TO BEGIN SCANNING')	
					host = input()
					akey = API_KEYS["sectrails"]
					st = BASE_ENDPOINTS["st"]

					if not akey:
						Style.Colors.RB('MISSING SECURITY TRAILS API KEY.\nPLEASE PROVIDE PROPER API AUTHENTICATION AND RUN AGAIN\n')
					else:
						url = "{0}/v1/history/{1}/whois".format(st, host)
						querystring = {"apikey":"{0}".format(akey)}

						response = requests.request("GET", url, params=querystring)
						print(response.text)
						Style.Colors.M('SEARCHING FOR SUBDOMAINS...')
						url = "{0}/v1/domain/{1}/subdomains".format(st, host)
						querystring = {"apikey":"{0}".format(akey)}
						response = requests.request("GET", url, params=querystring)
						print(response.text)
						Style.Colors.M('GATHERING DATA...')
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
						Style.RST()

				if optd == '3':
					print('ENTER DOMAIN NAME TO SCRAPE')
					host = input()
					scrape(PAGES)

				if optd == '4':
					builtwith = API_KEYS["builtwith"]
					if not builtwith:
						Style.Colors.RB("NO BUILT WITH API KEY... CANNOT RUN THIS MODULE!!")
						Style.RST()
						break
					else:
						print("ENTER A DOMAIN NAME")
						domain = input()
						q = {"KEY":builtwith, "LOOKUP":domain}
						url = "https://api.builtwith.com/v13/api.json"
						r = requests.get(url, params=q)
						print(r.content)

				if optd == '6':
					print ('ENTER DOMAIN FOR SUBDOMAIN SCAN')
					host = input()
					try:
						subdomain_brute(SUBDOMAINS[0:19])
					except:
						pass
						print('HANDLING ERRORS, PLEASE WAIT...')
						try:
							sleep(8)
							print('CONTINUING THROUGH ERRORS...')
							subdomain_brute(SUBDOMAINS[6:19])
						except:
							pass
							print('HANDLING MORE ERRORS...')
							sleep(6)
							try:
								sleep(7)
								print('CROSSING FINGERS...')
								subdomain_brute(SUBDOMAINS[9:19])
							except:
								pass
								print('LAST TRY...')
								try:
									sleep(4)
									subdomain_brute(SUBDOMAINS[11:19])
								except:
									pass
									print('UNABLE TO FINISH SCANNING DUE TO ERRORS.')
								finally:
									print('SCANNING COMPLETE')
									break
					finally:
						break

				validopts = ["0", "1", "2", "3", "4", "5", "6"]
				if optd not in validopts:
					Style.Color.RB('INVALID KEY, PLEASE SELECT AN OPTION FROM THE MENU!')
					Style.RST()
			
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
				if nkey == '4':
					print('ENTER IP ADDRESS OR HOSTNAME')
					ip = input()
					nmap.tcp_trace()
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
						Style.Colors.RB("MISSING HUNTER API KEY. CANNOT COMPLETE THIS MODULE")
						Style.RST()
						break
					else:
						Style.Colors.C("ENTER AN EMAIL ADDRESS TO VERIFY")
						Style.RST()
						email = input()
						x = email
						hunter = PyHunter(hk)
						h = hunter.email_verifier(x)
						print(h)
						Style.RST()
					break

			
		if xkey == '4':
			print('ENTER HOSTNAME TO SCAN AND GATHER DATA ON')
			host = input()
			shkey = API_KEYS["shodan_key"]
			if not shkey:
				Style.Colors.RB('\nMISSING SHODAN API KEY, RETURNING TO MAIN MENU')
				Style.RST()
			else:
				shodan = shodan.Shodan(shkey)
				results = shodan.search(host)
				print(results)

				print('ENTER IP OF HOST')
				ip = input()
				ipres = shodan.host(ip)
				print(ipres)

		if xkey == '9':
			keys.show()
			keys.change()

		menu.main_menu()
		xkey = input()
