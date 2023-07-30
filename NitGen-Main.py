import string
import random
import requests
import subprocess
import ctypes
from colorama import Fore, Back, Style
import os
import win32gui
import asyncio


def generate_random_code(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


def check_nitro_code(code, token):
    headers = {
        "Authorization": token
    }
    response = requests.get(f"https://discord.com/api/v10/entitlements/gift-codes/{code}", headers=headers)
    return response.status_code == 200


def save_result(code, valid):
    with open("nitro.txt", "a") as file:
        if valid:
            file.write(f"VALID: {code}\n")


def set_window_title(valid_count, invalid_count):
    title = f"NitGen | Valid: {valid_count} | Invalid: {invalid_count} | Made By PersonalPr0xy"
    hwnd = win32gui.GetForegroundWindow()
    win32gui.SetWindowText(hwnd, title)


async def main():
    os.system('cls')
    print(Fore.RED + """

 ▄▄        ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄ 
▐░░▌      ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░▌      ▐░▌
▐░▌░▌     ▐░▌ ▀▀▀▀█░█▀▀▀▀  ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌░▌     ▐░▌
▐░▌▐░▌    ▐░▌     ▐░▌          ▐░▌     ▐░▌          ▐░▌          ▐░▌▐░▌    ▐░▌
▐░▌ ▐░▌   ▐░▌     ▐░▌          ▐░▌     ▐░▌ ▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌ ▐░▌   ▐░▌
▐░▌  ▐░▌  ▐░▌     ▐░▌          ▐░▌     ▐░▌▐░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌  ▐░▌  ▐░▌
▐░▌   ▐░▌ ▐░▌     ▐░▌          ▐░▌     ▐░▌ ▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░▌   ▐░▌ ▐░▌
▐░▌    ▐░▌▐░▌     ▐░▌          ▐░▌     ▐░▌       ▐░▌▐░▌          ▐░▌    ▐░▌▐░▌
▐░▌     ▐░▐░▌ ▄▄▄▄█░█▄▄▄▄      ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░▌     ▐░▐░▌
▐░▌      ▐░░▌▐░░░░░░░░░░░▌     ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌      ▐░░▌
 ▀        ▀▀  ▀▀▀▀▀▀▀▀▀▀▀       ▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀ 


    """)

    codes = input("How many codes do you want to generate? => ")
    num_codes = int(codes)
    code_length = 16

    tokenask = input("Please Type Your Token Here => ")
    token = tokenask.strip()

    valid_count = 0
    invalid_count = 0

    for _ in range(num_codes):
        code = generate_random_code(code_length)
        valid = check_nitro_code(code, token)

        if valid:
            valid_count += 1
            print(Fore.GREEN + f"VALID: {code}")
        else:
            invalid_count += 1
            print(Fore.RED + f"INVALID: {code}")

        save_result(code, valid)
        set_window_title(valid_count, invalid_count)

        await asyncio.sleep(0)

if __name__ == "__main__":
    asyncio.run(main())
