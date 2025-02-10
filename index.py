#cre: Công Minh:))
import requests
while True:
    try:
        exec(requests.get('https://raw.githubusercontent.com/huongdev6868/HuongDev/refs/heads/main/index.py').text)
    except KeyboardInterrupt:
        print("\n\033[1;97m[\033[1;91m❣\033[1;97m] \033[1;36m✈  \033[1;31mCảm ơn bạn đã dùng Tool. Thoát...")
        sys.exit()
