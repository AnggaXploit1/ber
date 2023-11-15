import random
import requests
import json
import os
from colorama import Fore

fr  =   Fore.RED
fc  =   Fore.CYAN
fw  =   Fore.WHITE
fg  =   Fore.GREEN
fm  =   Fore.MAGENTA  
os.system('cls')



print(fm+'''
         ______      __             _       __               __               
        / ____/_  __/ /_  ___  ____| |     / /___ __________/ /__  ____  _____
       / /   / / / / __ \/ _ \/ ___/ | /| / / __ `/ ___/ __  / _ \/ __ \/ ___/
      / /___/ /_/ / /_/ /  __/ /   | |/ |/ / /_/ / /  / /_/ /  __/ / / (__  ) 
      \____/\__, /_.___/\___/_/    |__/|__/\__,_/_/   \__,_/\___/_/ /_/____/  
           /____/                                                             
                      '''+'\033[90m'+'''- Copyright '''+'\033[92m'+'''[2023]'''+'\033[91m'+''' [@ShiroMoriaty]'''+'\033[0m'+fc+''' [AWSKeysGrabber]\n''')

x = int(raw_input(fc+"Input Count:"))

chars = "abcdefghijklmnopqrstuvwxyz0123456789/+"
regions = [
    "us-east-1", "us-east-2", "us-west-1", "us-west-2", "af-south-1", "ap-east-1", "ap-south-1",
    "ap-northeast-1", "ap-northeast-2", "ap-northeast-3", "ap-southeast-1", "ap-southeast-2",
    "ca-central-1", "eu-central-1", "eu-west-1", "eu-west-2", "eu-west-3", "eu-south-1",
    "eu-north-1", "me-south-1", "sa-east-1"
]

def generate_aws_id():
    return ''.join(random.choice(chars[:36]).upper() for _ in range(16))

def generate_aws_key():
    output = random.choice(chars[:26]).upper()
    output += ''.join(random.choice(chars) for _ in range(38))
    output += random.choice(chars[:26]).upper()
    return output

def generate_aws_region():
    return random.choice(regions)

def print_key():
    res = "AKIA" + generate_aws_id() + "|" + generate_aws_key() + "|" + generate_aws_region()
    print(res)
    with open("Result.txt", "a") as file:
        file.write(res + "\n")

for _ in range(x):
    print_key()
