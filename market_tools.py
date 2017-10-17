# let's get LIT

import requests
import json
import numpy as np
from pprint import pprint

with open('config.json') as data_file:
	data = json.load(data_file)

API_KEY = data["KEY"]

# returns the JSON response of a daily request
def monthlyRequest(ticker):
	r = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol='
		+ ticker +'&outputsize=full&apikey='+ API_KEY)
	response = r.json()
	return (r, response)

def dailyRequest(ticker):
	r = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='
		+ ticker +'&outputsize=full&apikey='+ API_KEY)
	response = r.json()
	return (r, response)

def intraDayRequest(ticker, interval):
	valid_intervals = {1, 5, 15, 30, 60}
	assert interval in valid_intervals
	r = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol='
		+ ticker +'&interval='+ str(interval) + 'min&outputsize=full&apikey='+ API_KEY)
	response = r.json()
	return (r,response)

def dumbResponse():
	js = open('daily_test.json')
	data = json.load(js)
	return data

def resp_to_json(request_fn, ticker, interval=None, subdir = ""):
	if interval!=None:
		out = request_fn(ticker, interval)[0]
	else:
		out = request_fn(ticker)[0]
	file_name = subdir + ticker+'.json'
	with open(file_name, 'w') as f:
		f.write(out.content)
	return file_name

my_basket = ['NVDA', 'VOO', 'JPM', 'WMT']

for tick in my_basket:
	print resp_to_json(monthlyRequest, tick, subdir = "compare1/")


