#CONFIG FILE TO SET API KEYS


API_KEYS = {

"sectrails":"",
"shodan_key":"",
"full_contact":"",
"hunter":"",
"virus_total":""

}

#DICTS AND LISTS THAT WILL BE USED THROUGHOUT THE PROGRAM

SUBDOMAINS = [
"api.", "developers.","developer.","securelogin.",
"console.", "db.", "careers.", "intranet." ]


PAGES  = ["/", "/index.html", "/admin.php", "/login.php","/login.html", 
"/auth/login", "/oauth2/authorize", "/crossdomain.xml", "/signin", "/admin.html",
"/auth", "/auth/sign_in", "/auth.db", "/auth/signin", "/forgotpassword", 
"/securelogin.asp", "/changepassword.php", "/resetpassword.php", "/password_reset", 
"/api", "/resetpassword", "/mysql", "/mysql.db", "/.db", "/console"]

BASE_ENDPOINTS = {

"st":"https://api.securitytrails.com"	

}
