import hashlib
import os
import requests
import re
import time
from datetime import datetime
from bs4 import BeautifulSoup as sop
from itertools import cycle
from urllib.parse import quote
import random

def get_unique_id():
    try:
        return hashlib.sha256((str(os.getuid()) + os.getlogin()).encode()).hexdigest()
    except Exception as e:
        print(f"Error generating unique ID: {e}")
        exit(1)

def check_permission(unique_key):
    while True:
        try:
            response = requests.get("https://pastebin.com/raw/X1JRjKw9")
            if response.status_code == 200:
                data = response.text
                permission_list = [line.strip() for line in data.split("\n") if line.strip().find(unique_key) != -1]
                if not permission_list:
                    print("\033[1;31mChecking Approval.....\033[0m")
                    time.sleep(10)
                else:
                    print("\033[1;92m[√] Permission granted. Your Key Was Approved.\033[0m")
                    break
            else:
                print(f"Failed to fetch permissions list. Status code: {response.status_code}")
                time.sleep(10)
        except Exception as e:
            print(f"Error checking permission: {e}")
            time.sleep(10)

def send_approval_request(unique_key):
    try:
        input("\033[1;97m[•] Press enter to send approval Key:\033[0m")
        message = f"Hello, Bhola sir! Please Approve My Token is :: {unique_key}"
        os.system(f"am start https://wa.me/+918227039997?text={quote(message)} >/dev/null 2>&1")
        print("\033[1;97mWhatsApp opened with approval request. Waiting for approval...\033[0m")
    except Exception as e:
        print(f"Error sending approval request: {e}")
        exit(1)

def print_colored_logo(logo):
    colors = [31, 32, 33, 34, 35, 36]  # ANSI color codes for red, green, yellow, blue, magenta, cyan
    for line in logo.split("\n"):
        color = random.choice(colors)
        print(f"\033[1;{color}m{line}\033[0m")
        time.sleep(0.1)  # Add delay for animation effect

def pre_main():
    logo = """

                                                       
 @@@@@@@  @@@  @@@   @@@@@@   @@@@@@@    @@@@@@   @@@  
@@@@@@@@  @@@  @@@  @@@@@@@@  @@@@@@@@  @@@@@@@   @@@  
!@@       @@!  @@@  @@!  @@@  @@!  @@@  !@@       @@!  
!@!       !@!  @!@  !@!  @!@  !@!  @!@  !@!       !@!  
!@!       @!@!@!@!  @!@!@!@!  @!@!!@!   !!@@!!    !!@  
!!!       !!!@!!!!  !!!@!!!!  !!@!@!     !!@!!!   !!!  
:!!       !!:  !!!  !!:  !!!  !!: :!!        !:!  !!:  
:!:       :!:  !:!  :!:  !:!  :!:  !:!      !:!   :!:  
 ::: :::  ::   :::  ::   :::  ::   :::  :::: ::    ::  
 :: :: :   :   : :   :   : :   :   : :  :: : :    :    
                                                       
"""
    unique_key = get_unique_id()
    os.system('clear')
    print_colored_logo(logo)
    print('\033[1;97m•──────────────────────────────────────────────────────────────────────────────────────•\033[0m')
    print(f"\033[1;92m[🔐] Your Key :: {unique_key}\033[0m")
    print('\033[1;97m•──────────────────────────────────────────────────────────────────────────────────────•\033[0m')
    send_approval_request(unique_key)
    check_permission(unique_key)

pre_main()
os.remove('filer.txt') if os.path.exists('filer.txt') else None

# ANSI color codes
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"

def main():
    logo = """

                                                       
 @@@@@@@  @@@  @@@   @@@@@@   @@@@@@@    @@@@@@   @@@  
@@@@@@@@  @@@  @@@  @@@@@@@@  @@@@@@@@  @@@@@@@   @@@  
!@@       @@!  @@@  @@!  @@@  @@!  @@@  !@@       @@!  
!@!       !@!  @!@  !@!  @!@  !@!  @!@  !@!       !@!  
!@!       @!@!@!@!  @!@!@!@!  @!@!!@!   !!@@!!    !!@  
!!!       !!!@!!!!  !!!@!!!!  !!@!@!     !!@!!!   !!!  
:!!       !!:  !!!  !!:  !!!  !!: :!!        !:!  !!:  
:!:       :!:  !:!  :!:  !:!  :!:  !:!      !:!   :!:  
 ::: :::  ::   :::  ::   :::  ::   :::  :::: ::    ::  
 :: :: :   :   : :   :   : :   :   : :  :: : :    :    
                                                       
"""
    start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    
    while True:
        try:
            os.system('clear')
            print_colored_logo(logo)
            print(f"\033[1;97m•──────────────────────────────────────────────────────────────────────────────────────•\033[0m")
            print('\033[1;92m\033[1m[•] Thew Legend Charsi Here\033[0m')
            print(f"\033[1;92m\033[1m[+] start time: {start_time}\033[0m")
            print()
            print(f"\033[1;92m\033[1m[+] Cookies File :: \033[0m", end='')
            cokki = input().strip()
            cook = open(cokki, 'r').read().splitlines()
            print(f"\033[1;92m\033[1m[+] Post Link id :: \033[0m", end='')
            lnk = input().strip()
            print(f"\033[1;92m\033[1m[+] Kidx Name :: \033[0m", end='')
            hater = input().strip()
            print(f"\033[1;92m\033[1m[+] Comment File :: \033[0m", end='')
            filee = input().strip()
            messages = open(filee, 'r').read().splitlines()
            print(f"\033[1;92m\033[1m[+] Enter delay (seconds) :: \033[0m", end='')
            delay = int(input().strip())

            message_cycle = cycle(messages)  # Cycle through messages

            os.system('clear')
            print_colored_logo(logo)
            print()
            print(f"\033[1;92m\033[1m Process Started....\033[0m")
            print(f"\033[1;97m•──────────────────────────────────────────────────────────────────────────────────────•\033[0m")
            comment(message_cycle, cook, lnk, hater, delay)
        except Exception as e:
            print(f"{RED}An error occurred: {e}{RESET}")
            time.sleep(10)  # Wait for 10 seconds before retrying

def get_profile_name(cookies):
    ses = requests.Session()
    g_headers = {
        'authority': 'mbasic.facebook.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"',
        'sec-ch-ua-full-version-list': '" Not A;Brand";v="99.0.0.0", "Chromium";v="101.0.4951.40"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-ch-ua-platform-version': '"11.0.0"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 11; TECNO CE7j) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36',
    }
    response = ses.get('https://mbasic.facebook.com/me', cookies=cookies, headers=g_headers)
    if response.status_code == 200:
        soup = sop(response.text, 'html.parser')
        name_tag = soup.find('title')
        if name_tag:
            return name_tag.text.split('|')[0].strip()  # Extract name from title tag
    return "Unknown"

def is_connected():
    """Check if there is an internet connection."""
    try:
        requests.get('https://www.google.com', timeout=5)
        return True
    except requests.ConnectionError:
        return False

def comment(message_cycle, cookies_list, lnk, hater, delay):
    while True:  # Keep the comment function running continuously
        for cookie in cookies_list:
            while not is_connected():
                print(f"{YELLOW}No internet connection. Retrying...{RESET}")
                time.sleep(5)  # Wait before retrying

            ses = requests.Session()
            cookies = {'cookie': cookie}
            profile_name = get_profile_name(cookies)

            g_headers = {
                'authority': 'mbasic.facebook.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-language': 'en-US,en;q=0.9',
                'cache-control': 'max-age=0',
                'referer': lnk,
                'sec-ch-prefers-color-scheme': 'light',
                'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"',
                'sec-ch-ua-full-version-list': '" Not A;Brand";v="99.0.0.0", "Chromium";v="101.0.4951.40"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
                'sec-ch-ua-platform-version': '"11.0.0"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Linux; Android 11; TECNO CE7j) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36',
            }

            try:
                res1 = ses.get(url=lnk, cookies=cookies, headers=g_headers)
                if res1.status_code != 200:
                    print(f"{RED}Failed to load the page. Status code: {res1.status_code}{RESET}")
                    time.sleep(10)  # Wait before retrying
                    continue

                res1_text = res1.text
                j2 = re.search(r'name="jazoest" value="([^"]+)"', res1_text)
                fb_dtsg = re.search(r'name="fb_dtsg" value="([^"]+)"', res1_text)

                if not j2 or not fb_dtsg:
                    print(f"{RED}Error: 'jazoest' or 'fb_dtsg' not found{RESET}")
                    time.sleep(10)  # Wait before retrying
                    continue

                ses.headers.update({'content-type': 'application/x-www-form-urlencoded'})
                rose1 = sop(res1_text, 'html.parser')
                rose = rose1.find('form', method='post')

                if not rose:
                    print(f"{RED}Error: form action not found{RESET}")
                    time.sleep(10)  # Wait before retrying
                    continue

                rose_action = rose['action']
                if not rose_action.startswith('https://'):
                    rose_action = 'https://mbasic.facebook.com' + rose_action

                msg = next(message_cycle)
                payload = {
                    'fb_dtsg': fb_dtsg.group(1),
                    'jazoest': j2.group(1),
                    'comment_text': hater + ' ' + str(msg)
                }

                for input_tag in rose.find_all('input'):
                    if input_tag.get('name') not in payload:
                        payload[input_tag.get('name')] = input_tag.get('value')

                post = ses.post(url=rose_action, data=payload, cookies=cookies)
                if post.status_code != 200:
                    print(f"{RED}Failed to post comment. Status code: {post.status_code}{RESET}")
                    time.sleep(10)  # Wait before retrying
                    continue

                post_text = post.text
                if 'comment' not in post_text.lower():
                    print(f"{RED}Error: Your Account Comment Block.{RESET}")
                    time.sleep(10)  # Wait before retrying
                    continue

                print(f'\033[1;92m[+] Profile :: {profile_name}\033[0m')
                print(f'\033[1;92m[+] Kidx :: {hater}\033[0m')
                print(f'\033[1;92m[+] Comment Sent Successfully :: {hater} {msg}\033[0m')
                print(f'\033[1;97m•──────────────────────────────────────────────────────────────────────────────────────•\033[0m')

                time.sleep(delay)  # Wait before posting the next comment

            except requests.exceptions.ConnectionError:
                print(f"{RED}Connection error. Retrying...{RESET}")
                time.sleep(10)  # Wait before retrying
            except Exception as e:
                print(f"{RED}Error: {e}{RESET}")
                time.sleep(10)  # Wait before retrying

main()