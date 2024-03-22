# Made by gokiimax
# https://github.com/gokiimax

# ====================================================================================================================================== #

import os
import json
import requests
from colorama import Fore

# ====================================================================================================================================== #

# Read config file
f = open("config.json")
data = json.load(f)

# variables
access_key = data['access_key']

# ====================================================================================================================================== #

def banner():
    # Clear the console
    if os.name == 'nt':     # Windows
        os.system("cls")
    else:                   # Linux
        os.system("clear")

    print(f"""{Fore.CYAN}
    
        ██╗███╗   ███╗██████╗ ██╗   ██╗██╗     ███████╗███████╗
        ██║████╗ ████║██╔══██╗██║   ██║██║     ██╔════╝██╔════╝
        ██║██╔████╔██║██████╔╝██║   ██║██║     ███████╗█████╗  
        ██║██║╚██╔╝██║██╔═══╝ ██║   ██║██║     ╚════██║██╔══╝  
        ██║██║ ╚═╝ ██║██║     ╚██████╔╝███████╗███████║███████╗
        ╚═╝╚═╝     ╚═╝╚═╝      ╚═════╝ ╚══════╝╚══════╝╚══════╝

                        {Fore.WHITE}Author:{Fore.CYAN} gokimax
                        {Fore.WHITE}Github:{Fore.CYAN} https://github.com/gokiimax
    
    """)

# ====================================================================================================================================== #

def check_access_key():
    print("Cheking Access Key...")
    try:
        res = requests.get(f"https://app.numlookupapi.com/v1/status?apikey={access_key}").json()
        if res['month']['remaining'] > 0:
            print(f"[SUCCESS] ACCESS KEY VALID")
            return True
        else:
            print(f"[ERROR] ACCESS KEY NOT VALID")
            return False
    except:
        print(f"[ERROR] ACCESS KEY NOT VALID")
        return False

# ====================================================================================================================================== #

def get_information():
    number = input(f"{Fore.CYAN}Enter a phone number: ")
    api = f"https://app.numlookupapi.com/v1/validate/{number}?apikey={access_key}"
    data = requests.get(api).json()

    if data['valid']:
        info_text = f"""

╭─= Information for {number} =─╮
│      
│
│    Valid: {Fore.WHITE}{ 'yes' if data['valid'] else 'no' }{Fore.CYAN}
│    Number: {Fore.WHITE}{ data['number'] }{Fore.CYAN}
│    Carrier: {Fore.WHITE}{ data['carrier'] }{Fore.CYAN}
│    Location: {Fore.WHITE}{ data['location'] if data['location'] else 'No Location given' }{Fore.CYAN}
│    Line Type: {Fore.WHITE}{ data['line_type'] }{Fore.CYAN}
│    Country Code: {Fore.WHITE}{ data['country_code'] }{Fore.CYAN}
│    Country Name: {Fore.WHITE}{ data['country_name'] }{Fore.CYAN}
│    Local Format: {Fore.WHITE}{ data['local_format'] }{Fore.CYAN}
│    Country Prefix: {Fore.WHITE}{ data['country_prefix'] }{Fore.CYAN}
│    International Format: {Fore.WHITE}{ data['international_format'] }{Fore.CYAN}
│
╰= ────────────────────────────── =╯

        """
        print(info_text)
        input("Press any key to continue...")
    else:
        info_text = f"{Fore.RED}[-] {Number} is not a valid phone number"
        print(info_text)
        exit(-1)


# ====================================================================================================================================== #

while True:
    banner()
    if check_access_key():
        get_information()
