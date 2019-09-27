#! /usr/local/bin/python3  


#Import Needed Libraries

import pyfiglet
import requests
import os
import sys
from colorama import Fore, Back, Style
import shodan


#Banner

from pyfiglet import Figlet

BRI = Style.BRIGHT
RED = Fore.RED
GREEN = Fore.GREEN
BLUE = Fore.BLUE
RES = Style.RESET_ALL

def main_banner():
	print(GREEN)
	custom_fig = Figlet(font='doom')
	print(custom_fig.renderText('DATA.PIE'))

def main_menu():
	print(GREEN + '\n\n\n::MAIN MENU::\n\n\tENTER [1] DOMAIN SCANNING\n\tENTER [2] FOR TECHNICAL AND NETWORK INFO\
	\n\tENTER [4] FOR SHODAN\n\tENTER [5] TO EXIT\n')
	print(RES)


def sub_1():
	print(BLUE + '\n\n::DOMAIN SCANNING OPTIONS::\n\n\tENTER [1] FOR HEADER CAPTURE\n\
	ENTER [2]FOR WHOIS INFO\n\tENTER [3] TO SCRAPE WEB PAGES\n\tENTER [4] FOR URL DEEP SCAN\n\tENTER [0] TO RETURN TO THE MAIN MENU\n')
	print(RES)

def sub_2():
	print(RED + '\n\nNETWORK SCANNING\n\tENTER [1] FOR BASIC NMAP SCAN\n\n')
	print(RES)

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

def ptest(url):
	for xp in url:
		url = ('http://' + host + xp)
		rqp = requests.request("GET", url)
		c = rqp.status_code
		print(rqp)

def n_menu():
	print(GREEN + '\nNMAP SCANNING OPTIONS\n\nENTER [1] FOR A FULL PORT SCAN\
	\nENTER [2] FOR A BASIC QUICK SCAN\nENTER [3] TO NMAP SCAN WITH YOUR OWN CUSTOM OPTIONS\
	\nENTER [0] TO RETURN TO MAIN MENU\n\n')
	print(RES)

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

from config import API_KEYS


pages = ["/", "/index.html", "/admin.php", "/login.php","/login.html", "/auth/login", "/oauth2/authorize", "/crossdomain.xml", "/signin", "/admin.html",
"/auth.db", "/auth/signin", "/forgotpassword", "/securelogin.asp", "/changepassword.php", "/resetpassword.php", "/password_reset"]
st = "https://api.securitytrails.com"

main_banner()
print(RED + BRI)
input('PRESS ANY KEY TO CONTINUE...\n\n\n')
print(RES)
main_menu()
xkey = input()
while xkey != '5':

	if xkey == '1':
		sub_1()
		optd = input()
		while optd != '0':
			if optd == '1':
				print(BRI + 'ENTER HOST/DOMAIN NAME TO BEGIN SCANNING')
				print(RES)
				host = input()
				x = requests.get('https://' + host)
				if x.status_code == 200:
					print(BRI + GREEN + 'SUCCESSFUL CONNECTION. STATUS CODE RETURNED IS\n\n')
					print(x.status_code)
					print('\n\nHEADERS RETURNED AS:\n\n')
					print(x.headers)
				else:
					print(RED + 'AN ERROR HAS OCCURED\n STATUS CODE RETURNED IS'\
					+ x.status_code + x.text)
					print(RES)
			if optd == '2':
				print(BRI + 'ENTER HOST NAME TO BEGIN SCANNING')	
				host = input()
				akey = API_KEYS["sectrails"]
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
				scrape(pages)
			if optd == '4':
				urlscan = API_KEYS["url_scan"]
				if not urlscan:
					print(BRI + RED + 'MISSING API KEY FOR URLSCAN.IO. PLEASE PROVIDE A PROPER API KEY IN THE CONFIG FILE\n\
					RETURNING TO MAIN MENU\n')
					print(RES)
					sub_2()
				else:
					print('ENTER THE DOMAIN NAME TO SCAN')
					domain = input()
					url = ('https://urlscan.io/api/v1/search/')
					headers = {"API-Key":"{0}".format(urlscan)}
					querystring = {"domain":"{0}".format(domain)}
					e = requests.get(url, headers=headers, params=querystring)
					print(e.text)

			sub_1()
			optd = input()


	if xkey == '2':
		n_menu()
		nkey = input()
		while nkey != '0':
			if nkey == '1':
				print('ENTER IP ADDRESS TO BEGING SCANNING...')
				ip = input()
				print('SCANNING ALL PORTS. THIS MAY TAKE A FEW MINUTES')
				nmap_scan_ports()
			if nkey == '2':
				print('ENTER THE IP ADDRESS OF HOST TO BEGIN SCANNING')
				ip = input()
				nmap_basic()
			if nkey == '3':
				print('ENTER THE IP ADDRESS TO BEGIN SCAN')
				ip = input()
				print('ENTER THE NAME OF THE SCRIPT YOU WOULD LIKE TO USE DURING THE SCAN')
				scr = input()
				scripts = ' --script=' + scr
				nmap_custom()
			else:
				print('INVALID KEY, RETURNING TO MENU')
				n_menu()
				nkey = input()
			n_menu()
			nkey = input()
			
	if xkey == '4':
		print('ENTER HOSTNAME TO SCAN AND GATHER DATA ON')
		host = input()
		shkey = API_KEYS["shodan_key"]
		if not shkey:
			print('MISSING SHODAN API KEY, RETURNING TO MAIN MENU')
		else:
			shodan = shodan.Shodan(shkey)
			results = shodan.search(host)
			print(results)

			print('ENTER IP OF HOST')
			ip = input()
			ipres = shodan.host(ip)
			print(ipres)

	main_menu()
	xkey = input()
