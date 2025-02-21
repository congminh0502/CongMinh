import json
import requests, os, time
import platform
from time import sleep, strftime
from datetime import datetime
from bs4 import BeautifulSoup
import sys

banner = """
\033[1;33m██      ██╗      ████████╗ █████╗  █████╗ ██╗
\033[1;35m██╗    ╔██║      ╚══██╔══╝██╔══██╗██╔══██╗██║
\033[1;36m██║████║██║ █████╗  ██║   ██║  ██║██║  ██║██║
\033[1;37m██║    ╚██║ ╚════╝  ██║   ██║  ██║██║  ██║██║
\033[1;32m██║     ██║         ██║   ╚█████╔╝╚█████╔╝██████╗
\033[1;31m╚═╝     ╚═╝         ╚═╝    ╚════╝  ╚════╝ ╚═════╝\n
\033[1;97mTool By: \033[1;32mTrịnh Hướng            \033[1;97mPhiên Bản: \033[1;32m4.0     
\033[97m════════════════════════════════════════════════  
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Instagram\033[1;31m  : \033[1;33mhttps://www.instagram.com\033[1;31m/m@huongdev27
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Youtube\033[1;31m  : \033[1;32mhttps://www.youtube.com/@Huongdev27
\033[97m════════════════════════════════════════════════
"""

os.system('cls' if os.name == 'nt' else 'clear')
for x in banner:
    print(x, end="")
    sleep(0.001)

# Nhập Authorization và Token
try:
    Authorization = open("Authorization.txt", "x")
    t = open("token.txt", "x")
except:
    pass

try:
    Authorization = open("Authorization.txt", "r")
    t = open("token.txt", "r")
    author = Authorization.read().strip()
    token = t.read().strip()
    Authorization.close()
    t.close()
except Exception as e:
    author = ""
    token = ""

if author == "":
    author = input("\033[1;97mNHẬP AUTHORIZATION : ")
    token = input("\033[1;31mNHẬP T : ")
    with open("Authorization.txt", "w") as f:
        f.write(author)
    with open("token.txt", "w") as f:
        f.write(token)

# Nhập Delay (tính bằng giây)
while True:
    try:
        delay = int(input("\033[1;97m║ Nhập\033[1;91m Delay (giây): \033[1;97m"))
        break
    except:
        print("\033[1;31mSai định dạng! Vui lòng nhập số nguyên.")

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/json;charset=utf-8',
    'Authorization': author,
    't': token,
    'User-Agent': 'Mozilla/5.0'
}

def get_tasks():
    """Lấy danh sách nhiệm vụ Instagram từ GoLike"""
    url = "https://gateway.golike.net/api/advertising/publishers/instagram/jobs"
    try:
        response = requests.get(url, headers=headers)
        # Nếu phản hồi không trả về JSON hợp lệ
        try:
            data = response.json()
        except Exception:
            print("\033[1;31mLỗi JSON: Dữ liệu nhận được không hợp lệ!")
            print("Dữ liệu:", response.text)
            return None
        return data
    except Exception as e:
        print("\033[1;31mLỗi kết nối API:", e)
        return None

def complete_task(ads_id, account_id):
    """Gửi yêu cầu hoàn thành nhiệm vụ"""
    url = "https://gateway.golike.net/api/advertising/publishers/instagram/complete-jobs"
    json_data = {
        'ads_id': ads_id,
        'account_id': account_id,
        'async': True,
        'data': None,
    }
    try:
        response = requests.post(url, headers=headers, json=json_data)
        return response.json()
    except Exception as e:
        print("\033[1;31mLỗi hoàn thành nhiệm vụ:", e)
        return None

def open_link(url):
    """Mở link Instagram trên Windows hoặc Android (Termux)"""
    if os.name == "nt":
        os.system(f'start {url}')
    else:
        os.system(f'termux-open-url {url}')

def main():
    task_count = 0
    total_reward = 0  # Nếu API trả về số tiền, nếu không, giữ nguyên = 0
    while True:
        print("\n\033[1;97mĐang lấy nhiệm vụ...")
        tasks = get_tasks()
        if tasks is None or "status" not in tasks or tasks["status"] != 200:
            print("\033[1;31mKhông có nhiệm vụ hoặc lỗi kết nối!")
            time.sleep(10)
            continue

        for task in tasks["data"]:
            ads_id = task["id"]
            link = task["link"]
            account_id = task["object_id"]
            task_type = task["type"]

            print(f"\033[1;36mThực hiện nhiệm vụ {task_type.upper()} - {link}")
            open_link(link)
            # Chờ người dùng thực hiện thao tác trên Instagram theo delay do người dùng nhập
            for remaining_time in range(delay, -1, -1):
                print(f"\r\033[1;33mĐang chờ {remaining_time} giây...", end="")
                time.sleep(1)
            print("\r                          ", end="")  # Xóa dòng chờ

            result = complete_task(ads_id, account_id)
            if result and "status" in result and result["status"] == 200:
                task_count += 1
                reward = 0
                if "data" in result and "prices" in result["data"]:
                    reward = result["data"]["prices"]
                total_reward += reward

                # Lấy thời gian hiện tại
                local_time = time.localtime()
                h = f"{local_time.tm_hour:02}"
                m = f"{local_time.tm_min:02}"
                s = f"{local_time.tm_sec:02}"
                # In thông báo nhiệm vụ thành công theo giao diện giống tool TikTok
                chuoi = (f"\033[1;31m| \033[1;36m{task_count}\033[1;31m | "
                         f"\033[1;33m{h}:{m}:{s}\033[1;31m | "
                         f"\033[1;32msuccess\033[1;31m | "
                         f"\033[1;31m{task_type}\033[1;32m |"
                         f"\033[1;32m Ẩn ID\033[1;97m | \033[1;32m+{reward}\033[1;97m | "
                         f"\033[1;33mTổng: {total_reward}")
                print(chuoi)
            else:
                print("\033[1;31m✘ Không thể xác nhận nhiệm vụ!")
            # Chờ trước khi chuyển nhiệm vụ tiếp theo
            time.sleep(5)

if __name__ == "__main__":
    main()
