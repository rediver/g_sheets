import requests
import pandas as pd
import tablib
import openpyxl
from datetime import date
import json
import logging
import os 
import gspread


def handler(event): 

	today = str(date.today())
	
	with open(f'{os.getenv("FILE_MANAGER_PATH")}/results' + today + '.json', 'r') as f: 
		gc = gspread.service_account(filename=(f'{os.getenv("FILE_MANAGER_PATH")}/c.json'))
		sh = gc.open('scrapper').sheet1
		sh.append_row(f)