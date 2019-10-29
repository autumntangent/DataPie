#CONFIG FILE TO SET API KEYS


API_KEYS = {

"sectrails":"",
"shodan_key":"",
"full_contact":"",
"hunter":"",
"virus_total":"",
"builtwith":""

}

#DICTS AND LISTS THAT WILL BE USED THROUGHOUT THE PROGRAM

SUBDOMAINS = [
"about.", "api.", "login.", "developers.", "developer.", "share.", "staff.", 
"events.", "portal.", "db.", "console.", "private.", "careers.", "contact.",
"dns.", "intranet.", "accounts.", "securelogin." ]


PAGES  = ["/", "/index.html", "/admin.php", "/login.php","/login.html", 
"/auth/login", "/oauth2/authorize", "/crossdomain.xml", "/signin", "/admin.html",
"/auth", "/auth/sign_in", "/auth.db", "/auth/signin", "/forgotpassword", 
"/securelogin.asp", "/changepassword.php", "/resetpassword.php", "/password_reset", 
"/api", "/resetpassword", "/mysql", "/mysql.db", "/.db", "/console"]

BASE_ENDPOINTS = {

"st":"https://api.securitytrails.com"	

}
