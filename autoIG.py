#cre : huongdev27
#zalo : 0362166863
import json
import requests, os, time
from time import sleep

def get_accounts(headers):
    response = requests.get('https://gateway.golike.net/api/tiktok-account', headers=headers).json()
    return response

def get_like_jobs(account_id, headers):
    params = {'account_id': account_id, 'data': 'null'}
    response = requests.get('https://gateway.golike.net/api/advertising/publishers/tiktok/jobs', params=params, headers=headers).json()
    return response

def complete_job(ads_id, account_id, headers):
    json_data = {'ads_id': ads_id, 'account_id': account_id, 'async': True, 'data': None}
    response = requests.post(
        'https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs', headers=headers, json=json_data).json()
    return response

def report_error(ads_id, object_id, account_id, job_type, headers):
    json_data = {'ads_id': ads_id, 'object_id': object_id, 'account_id': account_id, 'type': job_type}
    requests.post('https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs', headers=headers, json=json_data)

def get_auth():
    try:
        with open("Authorization.txt", "r") as auth_file, open("token.txt", "r") as token_file:
            author = auth_file.read().strip()
            token = token_file.read().strip()
    except FileNotFoundError:
        author = input("\033[1;97mNHẬP AUTHORIZATION: ")
        token = input("\033[1;31mNHẬP TOKEN: ")
        with open("Authorization.txt", "w") as auth_file, open("token.txt", "w") as token_file:
            auth_file.write(author)
            token_file.write(token)
    return author, token

def main():
    author, token = get_auth()
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json;charset=utf-8',
        'Authorization': author,
        't': token,
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36'
    }

    accounts = get_accounts(headers)
    if accounts.get("status") != 200:
        print("Lỗi xác thực, vui lòng nhập lại!")
        return

    for i, acc in enumerate(accounts["data"], 1):
        print(f'[{i}] TikTok: {acc["nickname"]}')
    
    choice = int(input("Chọn tài khoản để chạy: ")) - 1
    account_id = accounts["data"][choice]["id"]
    delay = int(input("Nhập delay giữa các job (giây): "))

    while True:
        print("Đang lấy nhiệm vụ like...")
        job = get_like_jobs(account_id, headers)
        if job.get("status") != 200 or not job.get("data"):
            print("Không có nhiệm vụ nào, thử lại sau 10 giây...")
            sleep(10)
            continue

        ads_id = job["data"]["id"]
        link = job["data"]["link"]
        object_id = job["data"]["object_id"]
        
        if job["data"].get("type") != "like":
            report_error(ads_id, object_id, account_id, job["data"]["type"], headers)
            continue
        
        os.system(f"termux-open-url {link}")
        print(f"Like bài viết tại: {link}")
        sleep(delay)
        
        result = complete_job(ads_id, account_id, headers)
        if result.get("status") == 200:
            print(f"Nhận tiền thành công: +{result['data']['prices']} VNĐ")
        else:
            print("Không thể nhận tiền, bỏ qua nhiệm vụ.")

if __name__ == "__main__":
    main()
