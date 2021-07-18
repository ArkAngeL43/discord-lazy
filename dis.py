import os
import sys 
import time 
import requests
import timeit
from datetime import datetime

startTime = datetime.now()

os.system(' clear ')

def restart_program():
   python = sys.executable
   os.execl(python, python, * sys.argv)
   curdir = os.getcwd()
import time
from tqdm import tqdm

# LOAD ANIMATION 
# you dont need this its just a neet function to have 
def loading():
    for _ in tqdm(range(100), desc="Loading...", ascii=False, ncols=75):
        time.sleep(0.01)
    print("Loading Done!")

if __name__ == "__main__":
    loading()

# EXAMPLE MESSAGE 
# in the future you can change this however you want 
# just an example 
payload = {
    'content': "why hello there frien, i am mark, a personal assistant to help Ark_angel my owner send messages, following that I hope you have a great night, i hope to learn more! :D"
}

header = {
    'authorization': 'YOUR AUTH KEY'
}
time.sleep(1)
os.system(' clear ')
print("="*40)
os.system('figlet DISCORD ')
os.system('figlet     LAZYYY ')
print("="*40)
time.sleep(1)
print(" [!] sending messages [!] ")
r = requests.post("user you want to send to REQUEST URL", data=payload, headers=header)
time.sleep(1)
def loading():
    for _ in tqdm(range(100), desc="Sending Msg...", ascii=False, ncols=75):
        time.sleep(0.01)
if __name__ == "__main__":
    loading()        
os.system(' clear ')
print(" [!] message has been sent [!] ")
