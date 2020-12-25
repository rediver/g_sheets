import requests
import pandas as pd
import tablib
import openpyxl
from datetime import date
import json
import logging
import gspread

ldn_airports = ["LHR-sky", "STN-sky", "LGW-sky", "LTN-sky"]
ldn_arr = []
today = str(date.today())

headers = {
    'x-rapidapi-key': "422894374fmsh023eb926213aa23p1b8967jsn96e86f739667",
    'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com"
}

for i in ldn_airports:
    x = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browsequotes/v1.0/pl/pln/pl-PL/KRK-sky/" + i + "/" + today
    response = requests.request("GET", x, headers=headers)
    response_data = json.dumps(response.text)
    ldn_arr.append(response_data)


def output(ldn_arr):
	gc = gspread.service_account(filename='creds.json')
	sh = gc.open('scrapper').sheet1
	sh.append_row(ldn_arr)
	return 

output(ldn_arr)