import requests
import random
from telebot import TeleBot
from time import sleep
bot = TeleBot('7130084462:AAFJ1hVu-1MTGb5P2M0zNhXybHMRvGYCCpA')
id = '6040761848'
def Garena():
	code = ''.join(random.choices('1234567890QWERTYUIOPASDFGHJKLZXCVBNM',k=12))
	headers = {
	    'authority': 'prod-api.reward.ff.garena.com',
	    'accept': 'application/json, text/plain, */*',
	    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	    'access-token': 'b53911e1154a8ab561db98b3bfec828289f39a4dd795baf8f075e55ec0969398',
	    'code': 'null',
	    'content-type': 'application/json',
	     'cookie': '_ga=GA1.1.1603319018.1723290180; _ga_G8QGMJPWWV=GS1.1.1723290185.1.1.1723290221.0.0.0; datadome=g44TBTLmiVuhlmxAUUsEI_spSQ74a6SpX0j6MRMASz4AfJr3WF8Tl~JdpF91EFAmJHnoTnHkjXZLJ2plkEFGJiBHXiwJAzWLrht6U0bpjVYji49~J_RKBuZkZ7vWA3CS; _ga_Y1QNJ6ZLV6=GS1.1.1723376539.2.0.1723376539.0.0.0',
	    'origin': 'https://reward.ff.garena.com',
	    'referer': 'https://reward.ff.garena.com/',
	    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
	}
	json_data = {
	    'serialno': code,
	}
	response = requests.post(
	    'https://prod-api.reward.ff.garena.com/redemption/api/game/ff/redeem/',
	    headers=headers,
	    json=json_data,
	).text
	if '{"msg":"error_invalid_serialno"}' in response:
		print('-'*30)
		print(f'\033[91m[×]False ==> [{code}]')
		sleep(0.5)
		print('-'*30)
	elif '{"msg":"error_too_many_requests"}' in response:
		print('-'*30)
		print(f'\033[94m[¥]BAN ==> [{code}]')
		sleep(5)
		print('-'*30)
	else:
		print('-'*30)
		print(f'\033[92m[✓]True ==> [{code}]')
		print('-'*30)
		bot.send_message(id,f'{response}\n{code}')
		exit()
while True:
	Garena()	
