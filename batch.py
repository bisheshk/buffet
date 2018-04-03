import requests
import json
import numpy as np
import matplotlib.pyplot as plt 
import sqlite3 as lite
import sys


with open('config.json') as data_file:
	data = json.load(data_file)

API_KEY = data["KEY"]

def batch_request(tickers):
	stringified_tickers = ",".join(tickers)
	print tickers 
	r = requests.get('https://www.alphavantage.co/query?function=BATCH_STOCK_QUOTES&symbols=' + stringified_tickers+'&apikey=' + API_KEY)
	json_batch = j.json()
	print json_batch
	return json_batch

def add_to_db(symbol, price, volume, timestamp):

	# add code to commit data
	return 


def unpack_batch(b_request):
	quotes = b_request["Stock Quotes"]
	for quote_info in quotes:
		symbol = quote_info['1. symbol']
		price = quote_info['2. price']
		volume = quote_info['3. volume']
		timestamp = quote_info['4. timestamp']

		add_to_db(symbol, price, volume, timestamp)

batchRequest(['NVDA', 'MSFT'])
