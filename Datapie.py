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

def main_banner():
	print(Fore.GREEN)
	custom_fig = Figlet(font='doom')
	print(custom_fig.renderText('DATA.PIE'))

def main_menu():
	print(Fore.GREEN, Style.BRIGHT + '\n\n\n::MAIN MENU::\n\n\tENTER [1] DOMAIN SCANNING\n\tENTER [2] FOR TECHNICAL AND NETWORK INFO\
	\n\tENTER [4] FOR SHODAN\n\tENTER [5] TO EXIT\n')
	print(Style.RESET_ALL)


def sub_1():
	print(Style.BRIGHT, Fore.BLUE + '\n\n::DOMAIN SCANNING OPTIONS::\n\n\tENTER [1] FOR HEADER CAPTURE\n\
	ENTER [2]FOR WHOIS INFO\n\tENTER [3] TO SCRAPE WEB PAGES\n\tENTER [0] TO RETURN TO THE MAIN MENU\n')
	print(Style.RESET_ALL)

def sub_2():
	print(Style.BRIGHT, Fore.RED + '\n\nNETWORK SCANNING\n\tENTER [1] FOR BASIC NMAP SCAN\n\n')
	print(Style.RESET_ALL)

def scrape(url):
	for y in url:
		url = ('http://' + host + y)
		rq = requests.request("GET", url)
		c = rq.status_code
		success = 'SUCCESSFUL, PAGE EXISTS'
		fail = 'ERROR, PAGE NOT AVAILABLE'
		print(url, c)
		if c == 200: 
			print(success)
		else:
			print(fail)

def ptest(url):
	for xp in url:
		url = ('http://' + host + xp)
		rqp = requests.request("GET", url)
		c = rqp.status_code
		print(rqp)


def nmap_scan():
	print('SCANNING ' + (ip) + '\n\nSCANNING ALL PORTS FOR SERVICES AND REACHABILITY\nTHIS MAY TAKE A MINUTE...\n\n')
	os.system(('nmap -v -PS -p- -T4 --reason -sV -Pn ') + (ip))


from config import API_KEYS

st = "https://api.securitytrails.com"

pages = ["/", "/index.html", "/admin.php", "/login.php","/login.html", "/auth/login", "/oauth2/authorize", "/crossdomain.xml", "/signin", "/admin.html",
"/auth.db", "/auth/signin", "/forgotpassword", "/securelogin.asp", "/changepassword.php", "/resetpassword.php", "/password_reset"]

main_banner()
print(Fore.RED, Style.BRIGHT)
input('PRESS ANY KEY TO CONTINUE...')
print(Style.RESET_ALL)
print()
print()
main_menu()
xkey = input()
while xkey != '5':

	if xkey == '1':
		sub_1()
		optd = input()
		while optd != '0':
			if optd == '1':
				print(Style.BRIGHT + 'ENTER HOST/DOMAIN NAME TO BEGIN SCANNING')
				print(Style.RESET_ALL)
				host = input()
				x = requests.get('https://' + host)
				if x.status_code == 200:
					print(Style.BRIGHT + 'SUCCESSFUL CONNECTION. STATUS CODE RETURNED IS\n\n')
					print(x.status_code)
					print('\n\nHEADERS RETURNED AS:\n\n')
					print(x.headers)
					sub_1()
				else:
					print(Fore.RED + 'AN ERROR HAS OCCURED\n STATUS CODE RETURNED IS'\
					+ x.status_code + x.text)
			if optd == '2':
				print(Style.BRIGHT + 'ENTER HOST NAME TO BEGIN SCANNING')	
				host = input()
				akey = API_KEYS["sectrails"]
				if not akey:
					print (Style.BRIGHT + 'MISSING SECURITY TRAILS API KEY.\nPLEASE PROVIDE PROPER API AUTHENTICATION AND RUN AGAIN\n')
					main_menu()
				else:
					url = "{0}/v1/history/{1}/whois".format(st, host)
					querystring = {"apikey":"{0}".format(akey)}

					response = requests.request("GET", url, params=querystring)
					print(response.text)
					print('SEARCHING FOR SUBDOMAINS...')
					url = "{0}/v1/domain/{1}/subdomains".format(st, host)

					querystring = {"apikey":"{0}".format(akey)}

					response = requests.request("GET", url, params=querystring)

					print(response.text)


					print('GATHERING DATA...')
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

			if optd == '3':
				print('ENTER DOMAIN NAME TO SCRAPE')
				host = input()
				scrape(pages)

			sub_1()
			optd = input()

	if xkey == '2':
		print('ENTER IP ADDRESS TO BEGING SCANNING...')
		ip = input()
		nmap_scan()

	if xkey == '4':
		print('ENTER HOSTNAME TO SCAN AND GATHER DATA ON')
		host = input()
		shkey = API_KEYS["shodan_key"]
		if not shkey:
			print('MISSING SHODAN API KEY, RETURNING TO MAIN MENU')
			main_menu()
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
