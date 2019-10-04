#CONFIG FILE TO SET API KEYS


API_KEYS = {

"sectrails":"",
"shodan_key":"Fl53oxwYoI9IkzflO6ayo4ZKodffKILm",
"full_contact":"",
"url_scan":""

}

#PLACING LISTS & DICTS IN THE CONFIG FILE INSTEAD OF THE MAIN SOURCE CODE 

SUBDOMAINS = [
"blog.","intranet","mail.","login.","api.", "developers.","developer.","securelogin.",
"console.", "db.", "careers." ]


PAGES  = ["/", "/index.html", "/admin.php", "/login.php","/login.html", 
"/auth/login", "/oauth2/authorize", "/crossdomain.xml", "/signin", "/admin.html",
"/auth", "/auth/sign_in", "/auth.db", "/auth/signin", "/forgotpassword", 
"/securelogin.asp", "/changepassword.php", "/resetpassword.php", "/password_reset", 
"/api", "/resetpassword", "/mysql", "/mysql.db", "/.db", "/console"]

BASE_ENDPOINTS = {

"st":"https://api.securitytrails.com"	

}
