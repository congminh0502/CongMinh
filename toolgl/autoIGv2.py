import json
import requests, os, time, socket, sys
from time import strftime, sleep
from datetime import datetime, timedelta
from bs4 import BeautifulSoup

banner = """
\033[1;33m███    ███╗      ████████╗ █████╗  █████╗ ██╗
\033[1;35m████  ████║      ╚══██╔══╝██╔══██╗██╔══██╗██║
\033[1;36m██ ████ ██║ █████╗  ██║   ██║  ██║██║  ██║██║
\033[1;37m██  ██  ██║ ╚════╝  ██║   ██║  ██║██║  ██║██║
\033[1;32m██║     ██║         ██║   ╚█████╔╝╚█████╔╝██████╗
\033[1;31m╚═╝     ╚═╝         ╚═╝    ╚════╝  ╚════╝ ╚═════╝\n
\033[1;97mTool make By: \033[1;32mCông Minh            \033[1;97mPhiên Bản: \033[1;32m4.0     
\033[97m════════════════════════════════════════════════  
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Tool\033[1;31m     : \033[1;97m☞ \033[1;31mGolike - Instagram\033[1;33m♔ \033[1;97m🔫
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Youtube\033[1;31m  : \033[1;97m☞ \033[1;36mMinh Hà công\033[1;31m♔ \033[1;97m☜
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Tik Tok\033[1;31m  : \033[1;33mhttps://www.tiktok.com\033[1;31m/@mjng_ha
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Facebook\033[1;31m : \033[1;97m☞\033[1;32mhttps://www.facebook.com/ha.cong.minh.556853🔫\033[1;97m☜
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Telegram\033[1;31m : \033[1;97m☞\033[1;32mhttps://t.me/minh_ha0502🔫\033[1;97m☜
\033[97m════════════════════════════════════════════════
"""

os.system('cls' if os.name == 'nt' else 'clear')
for x in banner:
    print(x, end="")
    sleep(0.00125)
print("\033[1;31mYouTube : \033[1;33mCông \033[1;33mMinh\033[1;32m")   

# Nhập Authorization và Token
try:
    Authorization = open("Authorization.txt", "x")
    t = open("token.txt", "x")
except:
    pass
Authorization = open("Authorization.txt", "r")
t = open("token.txt", "r")
author = Authorization.read().strip()
token = t.read().strip()
if author == "":
    author = input("\033[1;97mNHẬP AUTHORIZATION: ")
    token = input("\033[1;31mNHẬP T: ")
    with open("Authorization.txt", "w") as Authorization, open("token.txt", "w") as t:
        Authorization.write(author)
        t.write(token)
else:
    select = input("\033[1;97m║ Đăng Nhập Tài Khoản Hiện Có (Enter để bỏ qua, nhập AUTHORIZATION để đổi): \n\033[1;97m╚⟩⟩⟩ ")
    if select != "":
        author = select
        token = input("\033[1;36mNhập T: ")
        with open("Authorization.txt", "w") as Authorization, open("token.txt", "w") as t:
            Authorization.write(author)
            t.write(token)
Authorization.close()
t.close()

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/json;charset=utf-8',
    'Authorization': author,
    't': token,
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'Referer': 'https://app.golike.net/account/manager/instagram',
}

# Hàm lấy danh sách tài khoản Instagram
def chonacc():
    response = requests.get('https://gateway.golike.net/api/instagram-account', headers=headers).json()
    return response

# Hàm lấy nhiệm vụ Follow
def nhannv(account_id):
    params = {
        'account_id': account_id,
        'data': 'null',
    }
    response = requests.get('https://gateway.golike.net/api/advertising/publishers/instagram/jobs',
                            params=params, headers=headers).json()
    return response

# Hàm xác nhận hoàn thành nhiệm vụ
def hoanthanh(ads_id, account_id):
    json_data = {
        'ads_id': ads_id,
        'account_id': account_id,
        'async': True,
        'data': None,
    }
    response = requests.post('https://gateway.golike.net/api/advertising/publishers/instagram/complete-jobs',
                             headers=headers, json=json_data).json()
    return response

# Hàm báo lỗi và bỏ qua nhiệm vụ
def baoloi(ads_id, object_id, account_id, loai):
    json_data1 = {
        'description': 'Tôi đã làm Job này rồi',
        'users_advertising_id': ads_id,
        'type': 'ads',
        'provider': 'instagram',
        'fb_id': account_id,
        'error_type': 6,
    }
    try:
        requests.post('https://gateway.golike.net/api/report/send', headers=headers, json=json_data1).json()
    except:
        pass
    json_data = {
        'ads_id': ads_id,
        'object_id': object_id,
        'account_id': account_id,
        'type': loai,
    }
    try:
        requests.post('https://gateway.golike.net/api/advertising/publishers/instagram/skip-jobs',
                      headers=headers, json=json_data).json()
    except:
        pass

# In danh sách tài khoản để người dùng chọn
def dsacc():
    chontkinstagram = chonacc()
    if chontkinstagram.get("status") != 200:
        print("\033[1;34mAuthorization hoặc Token sai, hãy nhập lại!!!")
        quit()
    for i, acc in enumerate(chontkinstagram.get("data", [])):
        nickname = acc.get("nickname", "Không xác định")
        print(f'\033[1;36m[{i+1}] \033[1;36m✈ \033[1;97mTài Khoản┊\033[1;32m㊪ :\033[1;93m {nickname} \033[1;97m|\033[1;31m㊪ :\033[1;32m Hoạt Động')
    return chontkinstagram

chontkinstagram = dsacc()
while True:
    try:
        luachon = int(input("\033[1;35m║ Chọn Tài Khoản Để Chạy: \n\033[1;97m╚⟩⟩⟩ "))
        while luachon > len(chontkinstagram["data"]):
            luachon = int(input("\033[1;32mAcc Này Không Có Trong Danh Sách, Hãy Nhập Lại: "))
        account_id = chontkinstagram["data"][luachon - 1]["id"]
        break
    except:
        print("\033[1;35mSai Định Dạng !!!")

while True:
    try:
        delay = int(input("\033[1;97m║ Nhập Delay: \n\033[1;97m╚⟩⟩⟩ "))
        break
    except:
        print("\033[1;31mSai Định Dạng !!!")

while True:
    try:
        doiacc = int(input("\033[1;97m║ Nhận Tiền Thất Bại Bao Nhiêu Lần Thì Dừng: \n\033[1;97m╚⟩⟩⟩ "))
        break
    except:
        print("\033[1;31mNhập Vào 1 Số !!!")

os.system('cls' if os.name == 'nt' else 'clear')
dem = 0
tong = 0
checkdoiacc = 0
dsaccloi = []
os.system('cls' if os.name == 'nt' else 'clear')

for x in banner:
    print(x, end="")
    sleep(0.001)
print(f'\033[1;36m|STT\033[1;97m| \033[1;33mThời gian ┊ \033[1;32mStatus | \033[1;31mType Job | \033[1;32mID Acc | \033[1;32mXu |\033[1;33m Tổng')

while True:
    if checkdoiacc == doiacc:
        dsaccloi.append(chontkinstagram["data"][luachon - 1]["nickname"])
        print(f"\033[1;36mCác Acc Instagram {dsaccloi} Có Vẻ Gặp Vấn Đề Nên Đổi Acc Chạy Đê")
        chontkinstagram = dsacc()
        while True:
            try:
                luachon = int(input("\033[1;35m║ Chọn Tài Khoản Để Chạy: \n\033[1;97m╚⟩⟩⟩ "))
                while luachon > len(chontkinstagram["data"]):
                    luachon = int(input("\033[1;32mAcc Này Không Có Trong Danh Sách, Hãy Nhập Lại: "))
                account_id = chontkinstagram["data"][luachon - 1]["id"]
                checkdoiacc = 0
                break  
            except:
                print("\033[1;35mSai Định Dạng !!!")
    
    print(f'\033[1;97mĐang \033[1;96mLấy \033[1;95mNhiệm \033[1;91mVụ\033[1;93m Follow', end="\r")
    while True:
        try:  
            nhanjob = nhannv(account_id)
            break
        except:
            time.sleep(1)
            pass
    if nhanjob.get("status") == 200:
        ads_id = nhanjob["data"]["id"]
        link = nhanjob["data"]["link"]
        object_id = nhanjob["data"]["object_id"]
        if nhanjob["data"]["type"] != "follow":
            baoloi(ads_id, object_id, account_id, nhanjob["data"]["type"])
            continue
        os.system(f"termux-open-url {link}")
        for remaining_time in range(delay, -1, -1):
            colors = [
                "\033[1;37mM\033[1;36mi\033[1;32mn\033[1;31mh \033[1;34mD\033[1;33me\033[1;36mv\033[1;36m🍉 - Tool\033[1;36m Vip \033[1;31m\033[1;32m",
                "\033[1;34mM\033[1;31mi\033[1;36mn\033[1;32mh \033[1;35mD\033[1;37me\033[1;33mv\033[1;32m🍉 - Tool\033[1;34m Vip \033[1;31m\033[1;32m",
                "\033[1;31mM\033[1;37mi\033[1;33mn\033[1;35mh \033[1;32mD\033[1;34me\033[1;35mv\033[1;37m🍉 - Tool\033[1;33m Vip \033[1;31m\033[1;32m",
                "\033[1;32mM\033[1;33mi\033[1;35mn\033[1;36mh \033[1;37mD\033[1;36me\033[1;31mv\033[1;34m🍉 - Tool\033[1;31m Vip \033[1;31m\033[1;32m",
                "\033[1;37mM\033[1;34mi\033[1;36mn\033[1;32mh \033[1;33mD\033[1;31me\033[1;37mv\033[1;34m🍉 - Tool\033[1;37m Vip \033[1;31m\033[1;32m",
                "\033[1;34mM\033[1;33mi\033[1;35mn\033[1;31mh \033[1;36mD\033[1;36me\033[1;32mv\033[1;37m🍉 - Tool\033[1;36m Vip \033[1;31m\033[1;32m",
                "\033[1;36mM\033[1;35mi\033[1;34mn\033[1;37mh \033[1;35mD\033[1;32me\033[1;36mv\033[1;33m🍉 - Tool\033[1;33m Vip \033[1;31m\033[1;32m",
            ]
            for color in colors:
                print(f"\r{color}|{remaining_time}| \033[1;31m", end="")
                time.sleep(0.12)
        print("\r                          \r", end="") 
        print("\033[1;35mĐang Nhận Tiền         ", end="\r")
        max_attempts = 2
        attempts = 0
        nhantien = None
        while attempts < max_attempts:
            try:
                nhantien = hoanthanh(ads_id, account_id)
                if nhantien.get("status") == 200:
                    break
            except:
                pass
            attempts += 1
        if nhantien and nhantien.get("status") == 200:
            dem += 1
            tien = nhantien["data"]["prices"]
            tong += tien
            local_time = time.localtime()
            hour = local_time.tm_hour
            minute = local_time.tm_min
            second = local_time.tm_sec
            h = f"0{hour}" if hour < 10 else hour
            m = f"0{minute}" if minute < 10 else minute
            s = f"0{second}" if second < 10 else second
            chuoi = (f"\033[1;31m| \033[1;36m{dem}\033[1;31m | "
                     f"\033[1;33m{h}:{m}:{s}\033[1;31m | "
                     f"\033[1;32msuccess\033[1;31m | "
                     f"\033[1;31m{nhantien['data']['type']}\033[1;32m |"
                     f"\033[1;32m Ẩn ID\033[1;97m |\033[1;32m +{tien} \033[1;97m| "
                     f"\033[1;33m{tong}")
            print("                                                    ", end="\r")
            print(chuoi)
            checkdoiacc = 0
        else:
            while True:
                try:
                    baoloi(ads_id, object_id, account_id, nhanjob["data"]["type"])
                    print("                                              ", end="\r")
                    print("\033[1;31mBỎ QUA NHIỆM VỤ ", end="\r")
                    sleep(1)
                    checkdoiacc += 1
                    break
                except:
                    pass
