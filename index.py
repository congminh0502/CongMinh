import threading, base64, os, time, re, json, random
from datetime import datetime, timedelta
from time import sleep, strftime
from bs4 import BeautifulSoup
import requests, socket, sys

try:
  from faker import Faker
  from requests import session
  from colorama import Fore, Style
  import requests, random, re
  from random import randint
  import requests,pystyle
  import socks
except:
  os.system("pip install faker")
  os.system("pip install requests")
  os.system("pip install colorama")
  os.system('pip install requests && pip install bs4 && pip install pystyle')
  print('__Vui Lòng Chạy Lại Tool__')
  
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;39m"
whiteb="\033[1;39m"
red="\033[0;31m"
redb="\033[1;31m"
end='\033[0m'
dev="\033[1;39m[\033[1;31m×\033[1;39m]\033[1;39m"

def banner():
 banner = f"""
\033[1;33m███    ███╗      ████████╗ █████╗  █████╗ ██╗
\033[1;35m████  ████║      ╚══██╔══╝██╔══██╗██╔══██╗██║
\033[1;36m██ ████ ██║ █████╗  ██║   ██║  ██║██║  ██║██║
\033[1;37m██  ██  ██║ ╚════╝  ██║   ██║  ██║██║  ██║██║
\033[1;32m██║     ██║         ██║   ╚█████╔╝╚█████╔╝██████╗
\033[1;31m╚═╝     ╚═╝         ╚═╝    ╚════╝  ╚════╝ ╚═════╝\n
\033[1;97mTool remake By: \033[1;32mCông Minh            \033[1;97mPhiên Bản: \033[1;32m4.0     
\033[97m════════════════════════════════════════════════  

"""
 for X in banner:
  sys.stdout.write(X)
  sys.stdout.flush() 
  sleep(0.000001)

while True:
	os.system('cls' if os.name == 'nt' else 'clear')
	banner()
	print("\033[1;37m╔══════════════════════╗         ")
	print("\033[1;37m║  \033[1;32mTool Auto Golike    \033[1;37m║          ")
	print("\033[1;37m╚══════════════════════╝           ")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m1 \033[1;97m: \033[1;34mTool Auto TikTok \033[1;32m[Online]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m1.1 \033[1;97m: \033[1;34mTool Auto TikTokv1 \033[1;32m[Online]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m1.2 \033[1;97m: \033[1;34mTool Auto TikTok Tự Động \033[1;32m[Online]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m1.3 \033[1;97m: \033[1;34mTool Auto Instagram \033[1;32m[Online]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m1.4 \033[1;97m: \033[1;34mTool Auto Twitter \033[1;32m[Online]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m1.5 \033[1;97m: \033[1;34mTool Auto Youtube \033[1;32m[Online]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m1.6 \033[1;97m: \033[1;34mTool Auto Thread \033[1;32m[Online]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m1.7 \033[1;97m: \033[1;34mTool Auto Linkedin \033[1;32m[Online]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m1.8 \033[1;97m: \033[1;34mTool Auto Shoppe \033[1;32m[Off]")
	print("\033[1;37m╔══════════════════════╗         ")
	print("\033[1;37m║  \033[1;32mTool Tương Tác Chéo \033[1;37m║          ")
	print("\033[1;37m╚══════════════════════╝           ")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m2.1 \033[1;97m: \033[1;34mTool TTC Facebook \033[1;32m[Online]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m2.2 \033[1;97m: \033[1;34mTool TTC Pro5 \033[1;32m[Online]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m2.3 \033[1;97m: \033[1;34mTool TTC Pro5v1 \033[1;32m[Online]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m2.4 \033[1;97m: \033[1;34mTool TTC TikTok \033[1;32m[Online]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m2.5 \033[1;97m: \033[1;34mTool TTC Instagram \033[1;32m[Online]")
	print("\033[1;37m╔══════════════════════╗         ")
	print("\033[1;37m║  \033[1;32mTool TraoDoiSub.com \033[1;37m║          ")
	print("\033[1;37m╚══════════════════════╝           ")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m3.1 \033[1;97m: \033[1;34mTool TDS Facebook \033[1;32m[Online]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m3.2 \033[1;97m: \033[1;34mTool TDS FB Full Job \033[1;32m[Online]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m3.3 \033[1;97m: \033[1;34mTool TDS Pro5 \033[1;32m[Online]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m3.4 \033[1;97m: \033[1;34mTool TDS Pro5v1 \033[1;32m[Online]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m3.5 \033[1;97m: \033[1;34mTool TDS TikTok \033[1;32m[Online]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m3.6 \033[1;97m: \033[1;34mTool TDS Instagram \033[1;32m[Online]")
	print("\033[1;37m╔══════════════════════╗         ")
	print("\033[1;37m║  \033[1;32mTool Buff View \033[1;37m     ║   ")
	print("\033[1;37m╚══════════════════════╝           ")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m4.1 \033[1;97m: \033[1;34mTool Follow Page Pro5 \033[1;32m[Online]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m4.2 \033[1;97m: \033[1;34mTool Buff Member Facebook \033[1;32m[Online]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m4.3 \033[1;97m: \033[1;34mTool Buff Member Telegram \033[1;32m[Online]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m4.4 \033[1;97m: \033[1;34mBuff Reaction Story Bằng Page Pro5 \033[1;32m[Online]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m4.5 \033[1;97m: \033[1;34mTool Buff View Story Bằng Page Pro5 \033[1;32m[Online]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m4.6 \033[1;97m: \033[1;34mTool Buff View Tik Tok \033[1;32m[Online]")
	print("\033[1;37m╔════════════════════════╗         ")
	print("\033[1;37m║  \033[1;32mTool Gen Mail + Proxy \033[1;37m║   ")
	print("\033[1;37m╚════════════════════════╝           ")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m5.1 \033[1;97m: \033[1;34mTool Gen Mail V1 \033[1;32m[Online]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m5.2 \033[1;97m: \033[1;34mTool Gen Mail V2 \033[1;32m[Online]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m5.3 \033[1;97m: \033[1;34mTool Gen Proxy V1 \033[1;32m[Online]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m5.4 \033[1;97m: \033[1;34mTool Gen Proxy V2 \033[1;32m[Online]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m5.5 \033[1;97m: \033[1;34mTool Gen Proxy V3 \033[1;32m[Online]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m5.6 \033[1;97m: \033[1;34mTool Gen Proxy V4 \033[1;32m[Online]")
	print("\033[1;37m╔══════════════════════╗         ")
	print("\033[1;37m║  \033[1;32mTool Spam Vip \033[1;37m      ║   ")
	print("\033[1;37m╚══════════════════════╝           ")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m6.1 \033[1;97m: \033[1;34mTool Spam Box Messager \033[1;32m[Online]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m6.2 \033[1;97m: \033[1;34mTool Follow Spam Comment \033[1;32m[Online]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m6.3 \033[1;97m: \033[1;34mTool Spam Messager \033[1;32m[Online]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m6.4 \033[1;97m: \033[1;34mTool Spam sms + call♔ \033[1;32m[Online]")
	print("\033[1;37m╔══════════════════════╗         ")
	print("\033[1;37m║  \033[1;32mTool Airdrop Vip \033[1;37m   ║   ")
	print("\033[1;37m╚══════════════════════╝           ")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m7.1 \033[1;97m: \033[1;34mTool Đào Coin Blum \033[1;32m[Online]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m7.2 \033[1;97m: \033[1;34mTool Đào Coin Banana \033[1;32m[Online]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m7.3 \033[1;97m: \033[1;34mTool Đào Coin Birds \033[1;32m[Online]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m7.4 \033[1;97m: \033[1;34mTool Đào coin Xkucoin♔ \033[1;32m[Online]")
	print("\033[1;37m╔══════════════════════╗         ")
	print("\033[1;37m║  \033[1;32mTool Tiện Ích \033[1;37m      ║   ")
	print("\033[1;37m╚══════════════════════╝           ")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m8.1 \033[1;97m: \033[1;34mTool Get ID Facebook \033[1;32m[Online]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m8.2 \033[1;97m: \033[1;34mTool Get Token Facebook \033[1;32m[Online]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m8.3 \033[1;97m: \033[1;34mTool Spam Message \033[1;32m[Online]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m8.4 \033[1;97m: \033[1;34mTool Share Ảo Facebook \033[1;32m[Online]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m8.5 \033[1;97m: \033[1;34mTool Get Url Google \033[1;32m[Online]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m8.6 \033[1;97m: \033[1;34mTool Download Video TikTok \033[1;32m[Online]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m8.7 \033[1;97m: \033[1;34mTool Download Video Youtube \033[1;32m[Online]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m8.8 \033[1;97m: \033[1;34mTool Đào Mail \033[1;32m[Online]")
	print(f"\033[1;97m[\033[1;32m*\033[1;97m] \033[1;33m8.9 \033[1;97m: \033[1;34mThoát Tool \033[1;32m[Online]")
	print(f"\033[97m════════════════════════════════════════════════════════")
	chon = input('\033[1;91m┌─╼\033[1;97m[\033[1;91m<\033[1;97m/\033[1;91m>\033[1;97m]--\033[1;91m>\033[1;97m Nhập lựa chọn \033[1;97m \n\033[1;91m└─╼\033[1;91m✈ \033[1;33m : ')
	print('\033[1;39m─────────────────────────────────────────────────────────── ')
	if chon == '1':
		# Thành Công
		exec(requests.get('https://raw.githubusercontent.com/congminh0502/CongMinh/refs/heads/main/toolgl/HuongDev.py').text)
	elif chon == '1.1':
		exec(requests.get('https://raw.githubusercontent.com/huongdev6868/HuongDev/refs/heads/main/Full%20Golike/AutoTikTokv1.py').text)
	elif chon == '1.2':
		exec(requests.get('https://raw.githubusercontent.com/congminh0502/CongMinh/refs/heads/main/toolgl/AutoTikTokv3.1.py').text)
	elif chon == '1.3':
		exec(requests.get('https://raw.githubusercontent.com/congminh0502/CongMinh/refs/heads/main/toolgl/autoIG.py').text)

	elif chon == '1.4':
		exec(requests.get('https://raw.githubusercontent.com/huongdev6868/HuongDev/refs/heads/main/Full%20Golike/AutoX.py').text)
	elif chon == '1.5':
		exec(requests.get('https://raw.githubusercontent.com/huongdev6868/HuongDev/refs/heads/main/Full%20Golike/AutoYTB.py').text)
	elif chon == '1.6':
		exec(requests.get('https://raw.githubusercontent.com/huongdev6868/HuongDev/refs/heads/main/Full%20Golike/AutoTheads.py').text)
	elif chon == '1.7':
		exec(requests.get('https://raw.githubusercontent.com/congminh0502/CongMinh/refs/heads/main/toolgl/AutoLinkedin.py').text)
	elif chon == '1.8':
		exec(requests.get('https://raw.githubusercontent.com/congminh0502/CongMinh/refs/heads/main/toolgl/autoIGv2.py').text)
        
		# TTC
	elif chon == '2.1':
		exec(requests.get('https://raw.githubusercontent.com/huongdev6868/HuongDev/refs/heads/main/TuongTacCheo/TTCFB.py').text)
	elif chon == '2.2':
		exec(requests.get('https://raw.githubusercontent.com/huongdev6868/HuongDev/refs/heads/main/TuongTacCheo/TTCPro5.py').text)
	elif chon == '2.3':
		exec(requests.get('https://raw.githubusercontent.com/huongdev6868/HuongDev/refs/heads/main/TuongTacCheo/TTCPro5v1.py').text)
	elif chon == '2.4':
		exec(requests.get('https://raw.githubusercontent.com/huongdev6868/HuongDev/refs/heads/main/TuongTacCheo/TTCTikTok.py').text)
	elif chon == '2.5':
		exec(requests.get('https://raw.githubusercontent.com/huongdev6868/HuongDev/refs/heads/main/TuongTacCheo/TTCIG.py').text)
		# TDS
	elif chon == '3.1':
		# Thanh Công
		exec(requests.get('https://raw.githubusercontent.com/huongdev6868/HuongDev/refs/heads/main/TraoDoiSub/ToolTDSFb.py').text)
	elif chon == '3.2':
		# Thanh Công
		exec(requests.get('https://raw.githubusercontent.com/huongdev6868/HuongDev/refs/heads/main/TraoDoiSub/ToolTDSPro5.py').text)
	elif chon == '3.3':
		# Thanh Công
		exec(requests.get('https://raw.githubusercontent.com/huongdev6868/HuongDev/refs/heads/main/TraoDoiSub/ToolTDSPro5v1.py').text)
	elif chon == '3.4':
		# Thanh Công
		exec(requests.get('https://raw.githubusercontent.com/huongdev6868/HuongDev/refs/heads/main/TraoDoiSub/ToolTDSTikTok.py').text)
	elif chon == '3.5':
		# Thanh Công
		exec(requests.get('https://raw.githubusercontent.com/huongdev6868/HuongDev/refs/heads/main/TraoDoiSub/TDSIG.py').text)
	elif chon == '3.6':
		# Thanh Công
		exec(requests.get('https://raw.githubusercontent.com/huongdev6868/HuongDev/refs/heads/main/TraoDoiSub/TDSIG.py').text)	
		# Buff view
	elif chon == '4.1':
		# Thanh Công
		exec(requests.get('https://github.com/trinhhuong2004/ToolGop/blob/main/buff/bufffl.py').text)
	elif chon == '4.2':
		# Thanh Công
		exec(requests.get('https://github.com/trinhhuong2004/ToolGop/blob/main/buff/buffmemfb.py').text)
	elif chon == '4.3':
		# Thanh Công
		exec(requests.get('https://github.com/trinhhuong2004/ToolGop/blob/main/buff/buffmemtele.py').text)
	elif chon == '4.4':
		# Thanh Công
		exec(requests.get('https://github.com/trinhhuong2004/ToolGop/blob/main/buff/buffreactstr.py.py').text)
	elif chon == '4.5':
		# Thanh Công
		exec(requests.get('https://github.com/trinhhuong2004/ToolGop/blob/main/buff/buffview.py').text)
	elif chon == '4.6':
		# Thanh Công
		exec(requests.get('https://github.com/trinhhuong2004/ToolGop/blob/main/buff/viewtik.py').text)
	elif chon == '5.1':
		# Thanh Công
		exec(requests.get('https://raw.githubusercontent.com/huongdev6868/HuongDev/refs/heads/main/mailer/genmailv1.py').text)
	elif chon == '5.2':
		# Thanh Công
		exec(requests.get('https://raw.githubusercontent.com/huongdev6868/HuongDev/refs/heads/main/mailer/genmailv2.py').text)
	elif chon == '5.3':
		# Thanh Công
		exec(requests.get('https://raw.githubusercontent.com/huongdev6868/HuongDev/refs/heads/main/proxy/genproxyv1.py').text)
	elif chon == '5.4':
		# Thanh Công
		exec(requests.get('https://raw.githubusercontent.com/huongdev6868/HuongDev/refs/heads/main/proxy/genproxyv2.py').text)
	elif chon == '5.5':
		# Thanh Công
		exec(requests.get('https://raw.githubusercontent.com/huongdev6868/HuongDev/refs/heads/main/proxy/genproxyv3.py').text)
	elif chon == '5.6':
		# Thanh Công
		exec(requests.get('https://raw.githubusercontent.com/huongdev6868/HuongDev/refs/heads/main/proxy/genproxyv4.py').text) 
	elif chon == '6.1':
		# Thanh Công
		exec(requests.get('https://raw.githubusercontent.com/huongdev6868/HuongDev/refs/heads/main/KeyVip.py').text)
	elif chon == '6.2':
		# Thanh Công
		exec(requests.get('https://raw.githubusercontent.com/huongdev6868/HuongDev/refs/heads/main/KeyVip.py').text)
	elif chon == '6.3':
		# Thanh Công
		exec(requests.get('https://raw.githubusercontent.com/huongdev6868/HuongDev/refs/heads/main/spam/spammess.py').text)
	elif chon == '6.4':
		# Thanh Công
		exec(requests.get('https://raw.githubusercontent.com/huongdev6868/HuongDev/refs/heads/main/spam/spamsms.py').text)
	elif chon == '7.1':
		# Thanh Công
		exec(requests.get('https://raw.githubusercontent.com/huongdev6868/HuongDev/refs/heads/main/KeoAirdrop/ToolBlum.py').text)
	elif chon == '7.2':
		# Thanh Công
		exec(requests.get('https://raw.githubusercontent.com/huongdev6868/HuongDev/refs/heads/main/KeoAirdrop/ToolBlum.py').text)
	elif chon == '7.3':
		# Thanh Công
		exec(requests.get('https://raw.githubusercontent.com/huongdev6868/HuongDev/refs/heads/main/KeoAirdrop/ToolBlum.py').text)
	elif chon == '7.4':
		# Thanh Công
		exec(requests.get('https://raw.githubusercontent.com/huongdev6868/HuongDev/refs/heads/main/KeoAirdrop/ToolBlum.py').text)
	elif chon == '8.1':
		# Thanh Công
		exec(requests.get('https://raw.githubusercontent.com/huongdev6868/HuongDev/refs/heads/main/TienIchFaceBook/ToolGetidFacebook.py').text)
	elif chon == '8.2':
		# Thanh Công
		exec(requests.get('https://raw.githubusercontent.com/huongdev6868/HuongDev/refs/heads/main/TienIchFaceBook/ToolGetTokenFB.py').text)
	elif chon == '8.3':
		# Thanh Công
		exec(requests.get('https://raw.githubusercontent.com/huongdev6868/HuongDev/refs/heads/main/TienIchFaceBook/ToolSpamMessage.py').text)
	elif chon == '8.4':
		# Thanh Công
		exec(requests.get('https://raw.githubusercontent.com/huongdev6868/HuongDev/refs/heads/main/TienIchFaceBook/ToolShareAoCookieV1.py').text)
	elif chon == '8.5':
		# Thanh Công
		exec(requests.get('https://raw.githubusercontent.com/huongdev6868/HuongDev/refs/heads/main/TienIchFaceBook/urllink.py').text)
	elif chon == '8.6':
		# Thanh Công
		exec(requests.get('https://raw.githubusercontent.com/huongdev6868/HuongDev/refs/heads/main/TienIchFaceBook/vidtiktok.py').text) 
	elif chon == '8.7':
		# Thanh Công
		exec(requests.get('https://raw.githubusercontent.com/huongdev6868/HuongDev/refs/heads/main/TienIchFaceBook/vidytb.py').text)
	elif chon == '8.8':
		# Thanh Công
		exec(requests.get('https://raw.githubusercontent.com/huongdev6868/HuongDev/refs/heads/main/TienIchFaceBook/ToolDaoMail.py').text)
	elif chon == '8.9':
		# Thanh Công
		exec(requests.get('https://raw.githubusercontent.com/huongdev6868/HuongDev/refs/heads/main/TienIchFaceBook/ThoatTool.py').text)          
	else:
		sys.exit("")
