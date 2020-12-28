from datetime import date
import gspread
import json
import os 

def handler(event): 

	today = str(date.today())

	with open(f'{os.getenv("FILE_MANAGER_PATH")}/results' + today + '.json', 'r') as f: 
		gc = gspread.service_account(filename=(f'{os.getenv("FILE_MANAGER_PATH")}/c.json'))
		sh = gc.open('scrapper').sheet1
		sh.append_row(f)