
try :
    import requests
    import time
    import os 
    from art import *
    from colorama import Fore
    import time
    import json
    import random
    from time import sleep
    import sys
    from tabulate import tabulate
except ImportError:
    os.system("pip install requests")
    os.system("pip install tabulate")
    os.system("pip install art")
    os.system("pip install colorama")
def countdown(time_sec):
    for remaining_time in range(time_sec, -1, -1):
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
    print("\033[1;35mĐang Nhận Tiền         ",end = "\r")
    # while time_sec:
    #     mins, secs = divmod(time_sec, 60)
        
    #     timeformat = 'Vui Lòng Chờ : {:02d}'.format(secs)
        
    #     print(timeformat, end='\r')
    #     time.sleep(1)
    #     time_sec -= 1
def TWITTER():
    import os, time, requests, random
    from colorama import Fore

    # Hàm an toàn để parse JSON (bắt lỗi JSONDecodeError)
    def safe_json(response):
        try:
            return response.json()
        except Exception as e:
            print(Fore.RED + f"[❌] JSONDecodeError: {e}")
            return {}

    # Hàm an toàn để gửi POST request với JSON
    def safe_post_json(url, headers, json_data):
        try:
            res = requests.post(url, headers=headers, json=json_data, timeout=10)
            if res.status_code == 200:
                return safe_json(res)
            else:
                print(Fore.RED + f"[❌] POST HTTP {res.status_code} từ {url}")
                return {}
        except Exception as e:
            print(Fore.RED + f"[❌] POST lỗi: {e}")
            return {}

    

    # Kiểm tra cookie còn sống bằng cách gọi API settings của Twitter
    def is_cookie_alive(headers_tw):
        test_url = "https://x.com/i/api/1.1/account/settings.json"
        res = safe_json(requests.get(test_url, headers=headers_tw, timeout=10))
        return bool(res)

    # --- Lấy danh sách tài khoản từ GoLike (giữ nguyên logic gốc) ---
    url1_2 = 'https://gateway.golike.net/api/twitter-account'
    checkurl1_2 = safe_json(ses.get(url1_2, headers=headers))
    user_twitter1 = []
    account_id1 = []
    account = []
    STT = []
    STATUS = []
    tong = 0
    dem = 0
    i = 1
    for data in checkurl1_2.get('data', []):
        usernametk = data['screen_name']
        user_twitter1.append(data['username'])
        account_id1.append(data['id'])
        STT.append(i)
        account.append(usernametk)
        STATUS.append(Fore.GREEN + "Hoạt Động" + Fore.RED)
        print(f'\033[1;97m•[✩]➭\033[1;36m [{i}] \033[1;91m=> '
              f'\033[1;97mTên Tài Khoản┊\033[1;32m㊪ :\033[1;93m {usernametk} '
              f'\033[1;91m=> \033[1;97mStatus|'
              f'\033[1;32m㊪ :\033[1;93m {STATUS[-1]}\n')
        i += 1
    print(Fore.RED + '_________________________________________________________')
    try:
        choose = int(input('\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  Nhập Tài Khoản : '))
        if not (1 <= choose <= len(user_twitter1)):
            print(Fore.RED + "Chọn tài khoản không hợp lệ!")
            return
    except ValueError:
        print(Fore.RED + "Giá trị nhập không hợp lệ!")
        return

    os.system('cls' if os.name == 'nt' else 'clear')
    user_twitter1 = user_twitter1[choose - 1:choose]
    account_id1 = account_id1[choose - 1:choose]
    user_tiktok = user_twitter1[0]
    account_id = account_id1[0]

    # --- Xử lý Authorization và Cookie ---
    auth_file = 'AUTH' + str(account_id) + '.txt'
    if not os.path.isfile(auth_file):
        banner()
        AUTHURX = input(Fore.GREEN + '\033[1;97m[❣] ✈  NHẬP Authorization Twitter: ')
        with open(auth_file, 'w') as f:
            f.write(AUTHURX.strip())
    else:
        with open(auth_file, 'r') as f:
            AUTHURX = f.read().strip()

    cookie_file = 'COOKIE' + str(account_id) + '.txt'
    if not os.path.isfile(cookie_file):
        banner()
        cookieX = input(Fore.GREEN + '\033[1;97m[❣] ✈  NHẬP Cookie Twitter : ')
        with open(cookie_file, 'w') as f:
            f.write(cookieX.strip())
    else:
        with open(cookie_file, 'r') as f:
            cookieX = f.read().strip()

    os.system('cls' if os.name == 'nt' else 'clear')
    banner()
    try:
        job_count = int(input(Fore.RED + '\033[1;97m[❣] ✈  Nhập Số Lượng Job : '))
        DELAY = int(input(Fore.RED + '\033[1;97m[❣] ✈  Nhập Delay : '))
    except ValueError:
        print(Fore.RED + "Giá trị nhập không hợp lệ!")
        return
    print("\033[97m════════════════════════════════════════════════")

    # Tạo headers cho Twitter dựa trên cookie và token (dùng UA từ biến User_Agent của bạn)
    headersX = {
        'accept': '*/*',
        'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
        'authorization': AUTHURX,
        'content-type': 'application/json',
        'cookie': cookieX,
        'origin': 'https://x.com',
        'priority': 'u=1, i',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': User_Agent,
        'x-client-transaction-id': 'urp5610yhQLkM+CVhUdxse7V6km/w/d0jxm8ReTQ0zYMv9OrPxn4mhIlXHxcu5p9VeJWjLh903OGJv8VyMwdt6Mnr31KuQ',
        'x-client-uuid': '8a14d42e-d7a8-4d47-9e60-cd596f91ad4b',
        'x-csrf-token': cookieX.split('ct0=')[1].split(';')[0] if 'ct0=' in cookieX else '',
        'x-twitter-active-user': 'yes',
        'x-twitter-auth-type': 'OAuth2Session',
        'x-twitter-client-language': 'en',
    }

    # Kiểm tra cookie Twitter trước khi chạy job
    if not is_cookie_alive(headersX):
        print(Fore.RED + "Cookie die! Vui lòng nhập lại cookie và Authorization.")
        if os.path.exists(cookie_file):
            os.remove(cookie_file)
        if os.path.exists(auth_file):
            os.remove(auth_file)
        return TWITTER()

    # Xử lý từng job
    for j in range(job_count):
        try:
            job_url = f'https://gateway.golike.net/api/advertising/publishers/twitter/jobs?account_id={account_id}'
            nos = safe_json(ses.get(job_url, headers=headers))
            if not nos or nos.get('status') != 200 or not nos.get('data'):
                print(Fore.YELLOW + "[!] Job trống. Đợi 15s rồi thử lại...")
                countdown(15)
                continue
            ads_id = nos['data']['id']
            object_id = nos['data']['object_id']
            type_job = nos['data']['type']
            if type=='like':
                            url = 'https://x.com/i/api/graphql/lI07N6Otwv1PhnEgXILM7A/FavoriteTweet'
                            headersX = {
                            'accept': '*/*',
                            'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
                            'authorization': AUTHURX,
                            'content-type': 'application/json',
                            'cookie': cookieX,
                            'origin': 'https://x.com',
                            'priority': 'u=1, i',
                            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
                            'sec-ch-ua-mobile': '?1',
                            'sec-ch-ua-platform': '"Android"',
                            'sec-fetch-dest': 'empty',
                            'sec-fetch-mode': 'cors',
                            'sec-fetch-site': 'same-origin',
                            'user-agent': User_Agent,
                            'x-client-transaction-id': 'urp5610yhQLkM+CVhUdxse7V6km/w/d0jxm8ReTQ0zYMv9OrPxn4mhIlXHxcu5p9VeJWjLh903OGJv8VyMwdt6Mnr31KuQ',
                            'x-client-uuid': '8a14d42e-d7a8-4d47-9e60-cd596f91ad4b',
                            'x-csrf-token': cookieX.split('ct0=')[1].split(';')[0],
                            'x-twitter-active-user': 'yes',
                            'x-twitter-auth-type': 'OAuth2Session',
                            'x-twitter-client-language': 'en',
                                    }
                            json_data = {
                                'variables': {
                                    'tweet_id': object_id,
                                },
                                'queryId': 'lI07N6Otwv1PhnEgXILM7A',
                            }

                            node = requests.post(url,headers=headersX,json=json_data).json()
                            countdown(DELAY)
                            if 'data' or 'has already favorited tweet' in str(node):
                                url = 'https://gateway.golike.net/api/advertising/publishers/twitter/complete-jobs'
                                json_data = {
                                'ads_id': ads_id,
                                'account_id': account_id,
                                'async': True,
                                }
                                time.sleep(3)
                                response3 = requests.post('https://gateway.golike.net/api/advertising/publishers/twitter/complete-jobs',
                                headers=headers,
                                json=json_data,
                                ).json()       
                                if response3['success']==True:
                                    dem += 1
                                    local_time = time.localtime()
                                    hour = local_time.tm_hour
                                    minute = local_time.tm_min
                                    second = local_time.tm_sec

                                    # Định dạng giờ, phút, giây
                                    h = f"{hour:02d}"
                                    m = f"{minute:02d}"
                                    s = f"{second:02d}"
                                    prices =response3['data']['prices']

                                    # Cộng dồn giá trị prices vào tổng tiền
                                    tong += prices

                                    chuoi = (
                                        f"\033[1;31m\| 033[1;36m{dem}\033[1;31m\033[1;97m | "
                                        f"\033[1;33m{h}:{m}:{s}\033[1;31m\033[1;97m | "
                                        f"\033[1;32msuccess\033[1;31m\033[1;97m | "
                                        f"\033[1;31mlike\033[1;31m\033[1;32m\033[1;32m\033[1;97m |"
                                        f"\033[1;32m Ẩn ID\033[1;97m | \033[1;32m+{prices} \033[1;97m| "
                                        f"\033[1;33m{tong} vnđ"
                                    )
                                    print(chuoi) 
                                else:
                                    skipjob = 'https://gateway.golike.net/api/advertising/publishers/twitter/skip-jobs'
                                    PARAMS = {
                                    'ads_id' : ads_id,
                                    'account_id' : account_id,
                                    'object_id' : object_id ,
                                    'async': 'true',
                                    'data': 'null',
                                    'type': type,
                                    }
                                    checkskipjob = ses.post(skipjob,params=PARAMS).json()
                                    if checkskipjob['status'] == 200:
                                        message = checkskipjob['message']
                                        print(Fore.RED+str(message))
                                        PARAMS = {
                                        'ads_id' : ads_id,
                                        'account_id' : account_id,
                                        'object_id' : object_id ,
                                        'async': 'true',
                                        'data': 'null',
                                        'type': type,
                                        }
                            elif 'errors' and 'Could not authenticate you' in str(node):
                                print("HẾT HẠN COOKIE")
                                os.remove('COOKIE'+str(account_id)+'.txt')
                                return 0
            elif type_job == 'follow':
                url = 'https://x.com/i/api/1.1/friendships/create.json'
                headersY = {
                    'accept': '*/*',
                    'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
                    'authorization': AUTHURX,
                    'content-type': 'application/x-www-form-urlencoded',
                    'cookie': cookieX,
                    'origin': 'https://x.com',
                    'priority': 'u=1, i',
                    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
                    'sec-ch-ua-mobile': '?1',
                    'sec-ch-ua-platform': '"Android"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': 'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36',
                    'x-client-transaction-id': 'MPwo7xERotqe3xFS4oEGGDju3YMFR9v2gW2dSTZ/c2S4KYhQfp5ZmZYR/KcwzeyIYp3GBjKulQYFzsWftgEm6c7v0StkMw',
                    'x-csrf-token': cookieX.split('ct0=')[1].split(';')[0],
                    'x-twitter-active-user': 'yes',
                    'x-twitter-auth-type': 'OAuth2Session',
                    'x-twitter-client-language': 'en',
                }
                data = {
                    'include_profile_interstitial_type': '1',
                    'include_blocking': '1',
                    'include_blocked_by': '1',
                    'include_followed_by': '1',
                    'include_want_retweets': '1',
                    'include_mute_edge': '1',
                    'include_can_dm': '1',
                    'include_can_media_tag': '1',
                    'include_ext_is_blue_verified': '1',
                    'include_ext_verified_type': '1',
                    'include_ext_profile_image_shape': '1',
                    'skip_status': '1',
                    'user_id': object_id,
                }
                response2 = safe_json(requests.post('https://x.com/i/api/1.1/friendships/create.json',headers=headersY, data=data, timeout=10))
                countdown(DELAY)
                if 'id' in str(response2):
                    complete_url = 'https://gateway.golike.net/api/advertising/publishers/twitter/complete-jobs'
                    json_data = {'ads_id': ads_id, 'account_id': account_id, 'async': True}
                    time.sleep(3)
                    response = safe_json(requests.post(complete_url, headers=headers, json=json_data, timeout=10))
                    if response.get('success') == True:
                        dem += 1
                        local_time = time.localtime()
                        h = f"{local_time.tm_hour:02d}"
                        m = f"{local_time.tm_min:02d}"
                        s = f"{local_time.tm_sec:02d}"
                        prices = response['data']['prices']
                        tong += prices
                        chuoi = (f"\033[1;31m\033[1;36m{dem}\033[1;31m\033[1;97m | "
                                 f"\033[1;33m{h}:{m}:{s}\033[1;31m\033[1;97m | "
                                 f"\033[1;32msuccess\033[1;31m\033[1;97m | "
                                 f"\033[1;31mfollow\033[1;31m\033[1;32m\033[1;32m\033[1;97m |"
                                 f"\033[1;32m Ẩn ID\033[1;97m | \033[1;32m+{prices} \033[1;97m| "
                                 f"\033[1;33m{tong} vnđ")
                        print(chuoi)
                    else:
                        skipjob = 'https://gateway.golike.net/api/advertising/publishers/twitter/skip-jobs'
                        PARAMS = {'ads_id': ads_id, 
                                  'account_id': account_id, 
                                  'object_id': object_id,
                                  'async': 'true', 
                                  'data': 'null', 
                                  'type': type_job
                                  }
                        checkskipjob = safe_json(ses.post(skipjob, params=PARAMS, timeout=10))
                        if checkskipjob.get('status') == 200:
                            message = checkskipjob.get('message', '')
                            print(Fore.RED + str(message))
                elif 'errors' in str(response2) and 'Could not authenticate you' in str(response2):
                    print(Fore.RED + "HẾT HẠN COOKIE")
                    time.sleep(2)
                    if os.path.exists(cookie_file):
                        os.remove(cookie_file)
                    if os.path.exists(auth_file):
                        os.remove(auth_file)
                    return 0
            elif type_job == 'comment':
                comment = nos['lock']['message']
                url = 'https://x.com/i/api/graphql/oB-5XsHNAbjvARJEc8CZFw/CreateTweet'
                headersZ = {
                    'accept': '*/*',
                    'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
                    'authorization': AUTHURX,
                    'content-type': 'application/json',
                    'cookie': cookieX,
                    'origin': 'https://x.com',
                    'priority': 'u=1, i',
                    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
                    'sec-ch-ua-mobile': '?1',
                    'sec-ch-ua-platform': '"Android"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': User_Agent,
                    'x-client-transaction-id': 'urp5610yhQLkM+CVhUdxse7V6km/w/d0jxm8ReTQ0zYMv9OrPxn4mhIlXHxcu5p9VeJWjLh903OGJv8VyMwdt6Mnr31KuQ',
                    'x-client-uuid': '8a14d42e-d7a8-4d47-9e60-cd596f91ad4b',
                    'x-csrf-token': cookieX.split('ct0=')[1].split(';')[0],
                    'x-twitter-active-user': 'yes',
                    'x-twitter-auth-type': 'OAuth2Session',
                    'x-twitter-client-language': 'en',
                }
                json_data = {
                    'variables': {
                        'tweet_text': comment,
                        'reply': {'in_reply_to_tweet_id': object_id, 'exclude_reply_user_ids': []},
                        'dark_request': False,
                        'media': {'media_entities': [], 'possibly_sensitive': False},
                        'semantic_annotation_ids': []
                    },
                    'features': {
                        'communities_web_enable_tweet_community_results_fetch': True,
                        'c9s_tweet_anatomy_moderator_badge_enabled': True,
                        'tweetypie_unmention_optimization_enabled': True,
                        'responsive_web_edit_tweet_api_enabled': True,
                        'graphql_is_translatable_rweb_tweet_is_translatable_enabled': True,
                        'view_counts_everywhere_api_enabled': True,
                        'longform_notetweets_consumption_enabled': True,
                        'responsive_web_twitter_article_tweet_consumption_enabled': True,
                        'tweet_awards_web_tipping_enabled': False,
                        'creator_subscriptions_quote_tweet_preview_enabled': False,
                        'longform_notetweets_rich_text_read_enabled': True,
                        'longform_notetweets_inline_media_enabled': True,
                        'articles_preview_enabled': True,
                        'rweb_video_timestamps_enabled': True,
                        'rweb_tipjar_consumption_enabled': True,
                        'responsive_web_graphql_exclude_directive_enabled': True,
                        'verified_phone_label_enabled': False,
                        'freedom_of_speech_not_reach_fetch_enabled': True,
                        'standardized_nudges_misinfo': True,
                        'tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled': True,
                        'responsive_web_graphql_skip_user_profile_image_extensions_enabled': False,
                        'responsive_web_graphql_timeline_navigation_enabled': True,
                        'responsive_web_enhance_cards_enabled': False
                    },
                    'queryId': 'oB-5XsHNAbjvARJEc8CZFw'
                }
                cf = safe_json(requests.post(url, headers=headersZ, json=json_data, timeout=10))
                countdown(DELAY)
                if ('create_tweet' in str(cf)) or ('Authorization: Status is a duplicate.' in str(cf)):
                    complete_url = 'https://gateway.golike.net/api/advertising/publishers/twitter/complete-jobs'
                    json_data = {'ads_id': ads_id, 'account_id': account_id, 'async': True, 'comment_id': nos['lock']['comment_id'], 'message': comment}
                    time.sleep(3)
                    response = safe_json(requests.post(complete_url, headers=headers, json=json_data, timeout=10))
                    if response.get('success') == True:
                        dem += 1
                        local_time = time.localtime()
                        h = f"{local_time.tm_hour:02d}"
                        m = f"{local_time.tm_min:02d}"
                        s = f"{local_time.tm_sec:02d}"
                        prices = response['data']['prices']
                        tong += prices
                        chuoi = (f"\033[1;31m\033[1;36m{dem}\033[1;31m\033[1;97m | "
                                 f"\033[1;33m{h}:{m}:{s}\033[1;31m\033[1;97m | "
                                 f"\033[1;32msuccess\033[1;31m\033[1;97m | "
                                 f"\033[1;31mcomment\033[1;31m\033[1;32m\033[1;32m\033[1;97m |"
                                 f"\033[1;32m Ẩn ID\033[1;97m | \033[1;32m+{prices} \033[1;97m| "
                                 f"\033[1;33m{tong} vnđ")
                        print(chuoi)
                    else:
                        skipjob = 'https://gateway.golike.net/api/advertising/publishers/twitter/skip-jobs'
                        PARAMS = {'ads_id': ads_id, 'account_id': account_id, 'object_id': object_id, 'async': 'true', 'data': 'null', 'type': type_job}
                        checkskipjob = safe_json(requests.post(skipjob, params=PARAMS, timeout=10))
                        if checkskipjob.get('status') == 200:
                            message = checkskipjob.get('message', '')
                            print(Fore.RED + str(message))
                elif 'errors' in str(cf) and 'Could not authenticate you' in str(cf):
                    print(Fore.RED + "HẾT HẠN COOKIE")
                    time.sleep(2)
                    if os.path.exists(cookie_file):
                        os.remove(cookie_file)
                    if os.path.exists(auth_file):
                        os.remove(auth_file)
                    return 0
            else:
                print(nos.get('message', 'Job không hợp lệ'))
                countdown(15)
        except Exception as e:
            print(Fore.RED + f"Lỗi: {e}")
            continue

    print(Fore.GREEN + f"\n[✅] Đã hoàn thành {dem} job. Tổng tiền: {tong} vnđ")




def banner():
 os.system("cls" if os.name == "nt" else "clear")
 banner = """
\033[1;33m███    ███╗      ████████╗ █████╗  █████╗ ██╗
\033[1;35m████  ████║      ╚══██╔══╝██╔══██╗██╔══██╗██║
\033[1;36m██ ████ ██║ █████╗  ██║   ██║  ██║██║  ██║██║
\033[1;37m██  ██  ██║ ╚════╝  ██║   ██║  ██║██║  ██║██║
\033[1;32m██║     ██║         ██║   ╚█████╔╝╚█████╔╝██████╗
\033[1;31m╚═╝     ╚═╝         ╚═╝    ╚════╝  ╚════╝ ╚═════╝\n
\033[1;97mTool By: \033[1;32mCông Minh            \033[1;97mPhiên Bản: \033[1;32m4.0     
\033[97m════════════════════════════════════════════════  
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Tool\033[1;31m     : \033[1;97m☞ \033[1;31mGolike - Twiteer\033[1;33m♔ \033[1;97m🔫
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Youtube\033[1;31m  : \033[1;97m☞ \033[1;36mMinh Hà công\033[1;31m♔ \033[1;97m☜
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Tik Tok\033[1;31m  : \033[1;33mhttps://www.tiktok.com\033[1;31m/@mjng_ha
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Facebook\033[1;31m : \033[1;97m☞\033[1;32mhttps://www.facebook.com/ha.cong.minh.556853🔫\033[1;97m☜
\033[1;97m[\033[1;91m❣\033[1;97m]\033[1;97m Telegram\033[1;31m : \033[1;97m☞\033[1;32mhttps://t.me/minh_ha0502🔫\033[1;97m☜
\033[97m════════════════════════════════════════════════
"""
 for X in banner:
  sys.stdout.write(X)
  sys.stdout.flush() 
  sleep(0.00125)

def LIST():
    banner()
    print("\033[1;32mNhập \033[1;31m1 \033[1;33mđể vào \033[1;34mTool Twitter\033[1;33m")
os.system('cls' if os.name== 'nt' else 'clear')
banner()
checkfile = os.path.isfile('user.txt')
if checkfile == False:
    AUTHUR = input(Fore.GREEN+'\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mNHẬP Authorization Golike : ')
    createfile = open('user.txt','w')
    createfile.write(AUTHUR)
    createfile.close()
    readfile = open('user.txt','r')
    file = readfile.read()
    readfile.close()
else:
    readfile = open('user.txt','r')
    file = readfile.read()
    readfile.close()
ses = requests.Session()
User_Agent = random.choice([
    "android|Mozilla/5.0 (Linux; Android 14; SM-S928B Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.64 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 13; Pixel 7 Pro Build/TQ3A.230901.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.230 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 12; SM-G998B Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.163 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 11; Nexus 7 Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.178 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 13; IQ4502 Quad Build/TQ2A.230305.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.94 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 14; SM-G925FQ Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 12; SM-G935S Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.193 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 13; Pixel 6 Build/TQ3A.230901.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.64 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 11; Pixel C Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.230 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 12; LG-D725 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.85 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 13; Lenovo A7000-a Build/TQ2A.230305.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.163 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 11; SM-G925M Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.94 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 12; MOTOROLA XT1021 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 13; LG-D350 Build/TQ3A.230901.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.178 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 14; Xperia Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.193 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 11; Nexus 9X Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.64 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 13; GT-I9600 Build/TQ2A.230305.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.230 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 12; MOTO XT1570 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.85 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 14; HTC Butterfly S 919d Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.163 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 11; MOTOROLA MOTOG Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.94 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 13; HTC One801e dual sim Build/TQ3A.230901.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 12; HTC OneS Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.178 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 14; LG-H220 Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.193 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 11; Nexus 6 Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.64 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 13; GT-I9800 Build/TQ2A.230305.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.230 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 12; SM-D925S Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.85 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 14; LG-H900 Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.163 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 11; HTC One_M8 Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.94 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 13; Nokia 1100 wifi Build/TQ3A.230901.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 12; SGH-I337 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.178 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 14; SM-N915G Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.193 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 11; SM-G9350FG Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.64 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-G9350M Build/TQ2A.230305.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.230 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 12; Nexus 8 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.85 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 14; XT1045 Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.163 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 11; Xperia Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.94 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 13; MOTO X PLAY XT1562 Build/TQ3A.230901.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 12; MOTOROLA MOTO E XT1021 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.178 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 14; GT-I9700 Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.193 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 11; LG-D710 Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.64 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-T534 Build/TQ2A.230305.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.230 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 12; SAMSUNG GT-I9700 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.85 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 14; SM-T534 Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.163 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-G925F Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.94 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 13; HTC One_M9 Build/TQ3A.230901.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 12; SM-D920M Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.178 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 14; Nexus5 V7.1 Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.193 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 11; HTC [M8|M9|M8 Pro Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.64 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 13; SM-G838K Build/TQ2A.230305.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.230 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G490 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.85 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 14; SM-G9350FQ Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.163 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 11; Xperia V Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.94 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-G9358 Build/TQ3A.230901.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 12; Nexus 5 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.178 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 14; SAMSUNG SM-G925F Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.193 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 11; SAMSUNG-SM-N910F Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.64 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 13; HTC OneS Build/TQ2A.230305.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.230 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 12; [HM NOTE|NOTE-III|NOTE2 1LTET Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.85 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 14; Lenovo A7000-a Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.163 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 11; MOTOROLA MSM8960 Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.94 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 13; SM-E500F Build/TQ3A.230901.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 12; Ascend G310 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.178 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 14; [HM NOTE|NOTE-III|NOTE2 1LTETD Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.193 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 11; Samsung Galaxy S4 Mega GT-I8900 Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.64 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 13; Xperia V Build/TQ2A.230305.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.230 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 12; SM-G920T Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.85 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 14; LG-D325 Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.163 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 11; XT1030 Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.94 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 13; SM-A800F Build/TQ3A.230901.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G440 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.178 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 14; XT1015 Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.193 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 11; Nexus 5P Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.64 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 13; HTC One0P6B Build/TQ2A.230305.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.230 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 12; Nexus S Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.85 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 14; Nexus 7 Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.163 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 11; Xperia Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.94 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 13; Nexus 7X Build/TQ3A.230901.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 12; HTC One max Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.178 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 14; [HM NOTE|NOTE-III|NOTE2 1LTETD Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.193 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 11; HTC One_M8 Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.64 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 13; Nexus 5X Build/TQ2A.230305.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.230 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 12; GT-I9200 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.85 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 14; Samsung Galaxy SIV Mega GT-I9200 Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.163 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 11; LG-D337 Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.94 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 13; SM-G925I Build/TQ3A.230901.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 12; XT1050 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.178 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 14; Pixel C Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.193 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 11; Nexus 8X Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.64 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 13; HTC One801e Build/TQ2A.230305.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.230 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 12; Nexus 6 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.85 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 14; MOTOROLA MOTO XT1570 Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.163 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 11; LG-H910 Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.94 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 13; SAMSUNG-SM-N915A Build/TQ3A.230901.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 12; SM-N9008 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.178 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 14; Nexus 6X Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.193 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-G920M Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.64 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 13; HTC One_M8 Pro Build/TQ2A.230305.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.230 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 12; Nexus 6 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.85 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 14; MOTOROLA MOTOG Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.163 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 11; GT-I9100 Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.94 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 13; HTC One_M8 Build/TQ3A.230901.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 12; HTC One809d Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.178 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 14; SAMSUNG SM-D9350V Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.193 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 11; Nexus 7 Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.64 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 13; LG-F200L Build/TQ2A.230305.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.230 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 12; LG-E989 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.85 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 14; HTC [M8|M9|M8 Pro Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.163 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-G925FQ Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.94 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 13; SM-N9005 Build/TQ3A.230901.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 12; LG-H920 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.178 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 14; HTC One_M9 Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.193 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 11; Nexus 6X Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.64 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 13; SM-T550 Build/TQ2A.230305.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.230 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 12; HTC One M9 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.85 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 14; Nexus 6P Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.163 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-N8010 Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.94 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 13; Nokia 1100 wifi Build/TQ3A.230901.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 12; MOTOROLA RAZR Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.178 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 14; MOTOROLA MOTO X PLAY XT1562 Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.193 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 11; Lenovo A7000-a Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.64 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 13; SM-D859T Build/TQ2A.230305.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.230 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 12; SM-J100G Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.85 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 14; LG-V710 Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.163 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 11; SM-G935FG Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.94 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 13; HTC [M8|M9|M8 Pro Build/TQ3A.230901.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 12; SM-G925FD Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.178 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 14; LG-V500 Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.193 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 11; HTC One_M8 dual sim Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.64 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-G920V Build/TQ2A.230305.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.230 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 12; Lenovo A7000-a Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.85 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 14; SAMSUNG GT-I9100 Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.163 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 11; SM-A700F Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.94 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 13; Nexus 5P Build/TQ3A.230901.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 12; HTC [M8|M9|M8 Pro Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.178 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 14; SM-G900FQ Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.193 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 11; Nokia 1000 LTE Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.64 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 13; XT1048 Build/TQ2A.230305.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.230 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G3645A Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.85 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 14; SAMSUNG-SGH-I337M Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.163 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 11; SM-G935FD Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.94 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 13; LG-D716 Build/TQ3A.230901.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 12; SM-G920M Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.178 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 14; HTC One_M8 Pro Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.193 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-T265t Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.64 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-J200F Build/TQ2A.230305.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.230 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 12; Lenovo P772 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.85 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 14; LG-H920 Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.163 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 11; HTC One 801e Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.94 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 13; HTC Butterfly S 901 Build/TQ3A.230901.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 12; SM-G900FG Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.178 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 14; Nexus 5P Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.193 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 11; LG-V700 Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.64 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 13; SAMSUNG-SM-N915F Build/TQ2A.230305.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.230 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 12; Xperia Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.85 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 14; HTC Xplorer A280s Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.163 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 11; SM-D928V Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.94 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 13; Nexus 6 Build/TQ3A.230901.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 12; HP 695 Notebook PC Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.178 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 14; SM-A800T Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.193 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 11; Nokia 1000 wifi Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.64 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 13; SAMSUNG SGH-N075T Build/TQ2A.230305.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.230 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G920H Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.85 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 14; HTC Butterfly S 901 Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.163 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 11; LG-H930 Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.94 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 13; Nokia 1100 4G Build/TQ3A.230901.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 12; HTC One_M8 dual sim Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.178 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 14; HTC One 801s Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.193 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 11; Nexus 6 Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.64 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 13; GT-I9303T Build/TQ2A.230305.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.230 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 12; Xperia V Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.85 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 14; SM-G935FG Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.163 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 11; HP Compaq 2110b Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.94 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 13; Pixel C Build/TQ3A.230901.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 12; LG-H910 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.178 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 14; Nexus 5P Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.193 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 11; HTC 80:number1-2s Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.64 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 13; HUAWEI G6-L11 Build/TQ2A.230305.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.230 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 12; Nexus 8P Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.85 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 14; MOTOROLA MOTO XT1580 Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.163 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 11; Nexus 9 Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.94 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 13; SM-G920F Build/TQ3A.230901.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 12; Pixel C Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.178 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 14; LG-D335 Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.193 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 11; Nexus 7P Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.64 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 13; LG-D337 Build/TQ2A.230305.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.230 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G935M Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.85 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 14; SAMSUNG SM-A800I Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.163 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 11; SAMSUNG GT-I9700 Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.94 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 13; SM-N910F Build/TQ3A.230901.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 12; GT-I9400 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.178 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 14; SM-N915V Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.193 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 11; SAMSUNG GT-I9600 Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.64 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 13; HTC Butterfly S 919 Build/TQ2A.230305.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.230 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 12; HTC Butterfly S 901 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.85 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 14; SAMSUNG SM-G920L Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.163 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 11; SAMSUNG GT-I9404N Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.94 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 13; Nexus 8 Build/TQ3A.230901.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 12; Xperia Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.178 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 14; MOTOROLA MOTO XT1570 Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.193 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 11; SAMSUNG SGH-N085A Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.64 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 13; GT-I9506V Build/TQ2A.230305.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.230 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 12; Nexus_S_4G Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.85 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 14; XT1044 Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.163 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 11; HTC [M8|M9|M8 Pro Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.94 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 13; SM-G430 Build/TQ3A.230901.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 12; HTC [M8|M9|M8 Pro Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.178 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 14; Nexus 10 Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.193 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 11; Xperia V Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.64 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 13; SM-G925FQ Build/TQ2A.230305.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.230 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 12; GT-I9400I Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.85 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 14; LG-H900 Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.163 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 11; Pixel XL Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.94 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 13; LG-F500K Build/TQ3A.230901.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 12; MOTO X PLAY XT1562 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.178 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 14; Lenovo A7000-a Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.193 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 11; Nexus 9 Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.64 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 13; LG-D718 Build/TQ2A.230305.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.230 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G430 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.85 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 14; Xperia V Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.163 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-G900H Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.94 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 13; SAMSUNG GT-I9100 Build/TQ3A.230901.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-N8010 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.178 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 14; Nokia 3110 Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.193 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 11; Nexus 6 Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.64 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-A700 Build/TQ2A.230305.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.230 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 12; Pixel C Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.85 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 14; Xperia V Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.163 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 11; LG-H910 Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.94 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 13; HTC One M9 Build/TQ3A.230901.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 12; MOTO E XT1021 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.178 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 14; SAMSUNG SM-G900T Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.193 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 11; Xperia V Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.64 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 13; LG-D727 Build/TQ2A.230305.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.230 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 12; SM-G920S Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.85 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 14; HTC M8|M9|M8 Pro Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.193 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 11; MOTOROLA XT1021 Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.94 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 13; MOTO X PLAY XT1562 Build/TQ3A.230901.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 12; SM-G920FQ Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.178 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 14; SM-A700T Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.193 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 11; SM-G310I Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.64 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 13; Xperia V Build/TQ2A.230305.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.230 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 12; SM-G440 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.85 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 14; MOTO E XT1021 Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.193 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 11; LG Optimus G Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.94 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 13; HTC One_M8 Build/TQ3A.230901.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.144 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 12; Lenovo A7000-a Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.178 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 14; Lenovo P781 Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.193 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 11; LG-H920 Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.64 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 13; LG-D722 Build/TQ2A.230305.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.230 Mobile Safari/537.36",
    "android|Mozilla/5.0 (Linux; Android 12; SM-G928I Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.85 Mobile Safari/537.36"
])
headers = {'Accept-Language':'vi,en-US;q=0.9,en;q=0.8',
            'Referer':'https://app.golike.net/',
            'Sec-Ch-Ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
            'Sec-Ch-Ua-Mobile':'?0',
            'Sec-Ch-Ua-Platform':"Windows",
            'Sec-Fetch-Dest':'empty',
            'Sec-Fetch-Mode':'cors',
            'Sec-Fetch-Site':'same-site',
            'T' : 'VFZSamQwOUVSVEpQVkVFd1RrRTlQUT09',
            'User-Agent':User_Agent,
            "Authorization" : file,
            'Content-Type':'application/json;charset=utf-8'            
}

url1 = 'https://gateway.golike.net/api/users/me'
checkurl1 = ses.get(url1,headers=headers).json()
    #user
if checkurl1['status']== 200 :
        print('DANG NHAP THANH CONG')
        time.sleep(3)
        os.system('cls' if os.name== 'nt' else 'clear')
        # banner()
        # print(Fore.BLUE + '1.Tool Golike Mobile')
        # choose = int(input(Fore.WHITE + 'Nhập Lựa Chọn : '))
        # if choose == 1 :
        LIST()
        username = checkurl1['data']['username']
        coin = checkurl1['data']['coin']
        user_id = checkurl1['data']['id']
        print(Fore.GREEN+'\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mTài Khoản : '+Fore.YELLOW+username)
        print(Fore.GREEN+'\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mTổng Tiền : '+Fore.YELLOW+str(coin))
        print(Fore.RED+'\033[97m════════════════════════════════════════════════')
        print("\033[1;32mNhập \033[1;31m1 \033[1;33mđể vào \033[1;34mTool Twitter\033[1;33m")
        print(Fore.RED+'Nhập 2 Để Xóa Authorization Hiện Tại')
        choose = int(input(Fore.WHITE+'Nhập Lựa Chọn : '))
        if choose == 1:
            os.system('cls' if os.name== 'nt' else 'clear')
            LIST()
            username = checkurl1['data']['username']
            coin = checkurl1['data']['coin']
            user_id = checkurl1['data']['id']
            print(Fore.GREEN+'\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mTài Khoản : '+Fore.YELLOW+username)
            print(Fore.GREEN+'\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;32mTổng Tiền : '+Fore.YELLOW+str(coin))
            print(Fore.RED+'\033[97m════════════════════════════════════════════════')
            TWITTER()
        elif choose == 2:
                os.remove('user.txt')
else:
    print(Fore.RED+'DANG NHAP THAT BAI')
    os.remove('user.txt')
