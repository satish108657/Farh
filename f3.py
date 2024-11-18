import requests
import time
import signal
import sys
import os
from datetime import datetime
from colorama import init, Fore

comment_url = 'https://graph.facebook.com/{}/comments'  # URL to post comments
profile_url = 'https://graph.facebook.com/me?access_token={}'

# Initialize colorama
init(autoreset=True)

def approval():
    os.system('clear')
    uuid = str(os.geteuid()) + str(os.getlogin())
    id = '='.join(uuid)

    try:
        httpCaht = requests.get('https://pastebin.com/raw/X1JRjKw9').text.strip()
    except requests.RequestException as e:
        print(f"Error accessing approval file: {e}")
        sys.exit(1)

    if id in httpCaht:
        print('\033[1;92m Your Token is Successfully Approved')
        time.sleep(0.5)
        return
    else:
        eno = input('Enter your name: ')
        os.system('clear')
        print(f'Mr {eno}, Your Token: {id}')
        print('----------------------------------------------')
        print('Important Note')
        print('----------------------------------------------')
        print(f'Mr {eno}, Your Token is not approved')
        print(f'{eno}, You Have to Take Approval first')
        print('Free users stay away :)')
        print('----------------------------------------------')
        print('Tool Owner :: Mr. Charsi')
        print(f'{eno}, Your Token is: {id}')
        input('If You Want To Buy Then Press Enter')
        tks = f'Hello%20Charsi%20!%20Please%20Approve%20My%20Token%20My%20token%20Is%20:{id}%20My%20Name%20is%20{eno}'
        os.system(f'am start https://wa.me/+918227039997?text={tks}')
        time.sleep(1)
        approval()

def get_access_tokens(file_path):
    """Reads access tokens from a file and returns them as a list."""
    with open(file_path, 'r') as file:
        tokens = file.read().splitlines()
    return tokens

def get_profile_name(token):
    """Fetches the profile name associated with the given access token."""
    try:
        response = requests.get(profile_url.format(token))
        response.raise_for_status()
        profile_data = response.json()
        return profile_data.get('name')
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while getting profile name: {e}")
        return None

def post_comment(post_id, message, token, profile_name):
    """Posts a comment on the specified post using the given access token."""
    payload = {
        'message': message,
        'access_token': token
    }
    try:
        response = requests.post(comment_url.format(post_id), data=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"\033[1;31mFailed to post comment by {profile_name} on post {post_id}. Check if the post ID is correct.")
        return None

def remove_invalid_tokens(file_path, valid_tokens):
    """Writes only valid tokens back to the file."""
    with open(file_path, 'w') as file:
        for token in valid_tokens:
            file.write(f"{token}\n")

def clear_screen():
    """Clears the terminal screen."""
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For macOS and Linux
        os.system('clear')

def loading_animation(profiles):
    """Displays loading animation with the given profiles."""
    for profile_name in profiles:
        print(f"\033[1;32m[•] Loading profile :: {profile_name}")
        time.sleep(0.5)

def center_text(text, width):
    """Centers the given text within the specified width."""
    lines = text.strip().split('\n')
    centered_lines = [line.center(width) for line in lines]
    return '\n'.join(centered_lines)

def apply_gradient(text):
    """Applies a gradient color to the text."""
    gradient_colors = [
        Fore.LIGHTRED_EX,    # Red
        Fore.LIGHTYELLOW_EX, # Yellow
        Fore.LIGHTGREEN_EX,  # Green
        Fore.LIGHTCYAN_EX,   # Cyan
        Fore.LIGHTBLUE_EX,   # Blue
        Fore.LIGHTMAGENTA_EX # Magenta
    ]
    result = ''
    for i, line in enumerate(text.split('\n')):
        color = gradient_colors[i % len(gradient_colors)]
        result += f"{color}{line}\033[0m\n"
    return result

def signal_handler(sig, frame):
    print("\nProgram exited gracefully")
    sys.exit(0)

def main():
    approval()

    logo = """

 ██████╗██╗  ██╗ █████╗ ██████╗ ███████╗██╗
██╔════╝██║  ██║██╔══██╗██╔══██╗██╔════╝██║
██║     ███████║███████║██████╔╝███████╗██║
██║     ██╔══██║██╔══██║██╔══██╗╚════██║██║
╚██████╗██║  ██║██║  ██║██║  ██║███████║██║
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝
                                                   
    """

    # Determine terminal width
    terminal_width = os.get_terminal_size().columns

    # Apply gradient and center the logo
    colored_logo = apply_gradient(logo)
    centered_logo = center_text(colored_logo, terminal_width)
    
    clear_screen()
    print(centered_logo)

    start_time = datetime.now()
    print(f"\033[1;33m[#] Start Time :: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    access_tokens_file = input("\033[1;32m[+] Enter the Token File :: ")
    num_post_ids = int(input("\033[1;32m[+] Enter the number of post IDs :: "))
    post_ids = []
    for i in range(num_post_ids):
        post_id = input(f"\033[1;32m[+] Enter Post ID {i+1} :: ")
        post_ids.append(post_id.strip())

    comment_file_path = input("\033[1;32m[+] Enter the comment file :: ")
    try:
        with open(comment_file_path, 'r') as file:
            comment_messages = file.read().splitlines()
    except FileNotFoundError:
        print("Comment file not found. Exiting...")
        return
    
    delay_seconds = float(input("\033[1;32m[+] Enter the delay :: "))

    delay_seconds = max(delay_seconds, 1)

    clear_screen()

    print(centered_logo)
    print('\033[97m--------------------------------------------------------------------------------------\033[0m') 
    print("\033[1;37mAll Profiles Is Loading...")

    access_tokens = get_access_tokens(access_tokens_file)
    valid_tokens = []
    invalid_tokens = []

    for token in access_tokens:
        profile_name = get_profile_name(token)
        if profile_name:
            valid_tokens.append((token, profile_name))
        else:
            invalid_tokens.append((token, "Invalid Token"))

    remove_invalid_tokens(access_tokens_file, [token for token, _ in valid_tokens])

    print("\n")

    loading_animation([profile_name for _, profile_name in valid_tokens])

    print(f"\033[1;32m[√] Valid Profiles :: ({len(valid_tokens)}):")
    for token, profile_name in valid_tokens:
        print(profile_name)

    if not valid_tokens:
        print("No valid access tokens found.")
        return

    num_accounts = len(valid_tokens)
    print(" " * 65)
    print('\033[97m--------------------------------------------------------------------------------------\033[0m') 

    signal.signal(signal.SIGINT, signal_handler)

    comment_index = 0

    while True:
        for i, post_id in enumerate(post_ids):
            if not post_id:
                print("Invalid Post ID.")
                continue

            for j, (token, profile_name) in enumerate(valid_tokens):
                post_id_index = (i * num_accounts + j) % len(post_ids)
                current_post_id = post_ids[post_id_index]

                if comment_index >= len(comment_messages):
                    comment_index = 0

                comment_message = comment_messages[comment_index]
                comment_index += 1

                response = post_comment(current_post_id, comment_message, token, profile_name)
                if response and 'id' in response:
                    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    print(f"\033[1;32m[+] Profile Name :: {profile_name}")
                    print(f"\033[1;32m[+] Post ID :: {current_post_id}")
                    print(f"\033[1;32m[√] Comment Sent Done :: {comment_message}")
                    print(f"\033[1;32m[√] Sahii Hai :: {current_time}")
                    print(" " * 65)
                else:
                    print(f"\033[1;31mFailed to post comment by {profile_name} on post {post_id}. Check if the post ID is correct.")
                    print(" " * 65)

                time.sleep(delay_seconds)

def signal_handler(sig, frame):
    """Signal handler function to handle Ctrl+C."""
    print('\nExiting...')
    sys.exit(0)

if __name__ == '__main__':
    main()