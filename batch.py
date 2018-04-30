import requests
import json
import numpy as np
import matplotlib.pyplot as plt 
import sqlite3 as lite
import sys


with open('config.json') as data_file:
	data = json.load(data_file)

API_KEY = data["KEY"]

working_dict = {}

mem_limit = 5000

def initialize_memory(ticker):
	for ticker in tickers:
		working_dict[ticker] = []
	return working_dict


def batch_request(tickers):
	# returns json obj 
	stringified_tickers = ",".join(tickers)
	print tickers 
	r = requests.get('https://www.alphavantage.co/query?function=BATCH_STOCK_QUOTES&symbols=' + stringified_tickers+'&apikey=' + API_KEY)
	json_batch = r.json()
	return json_batch

def add_to_db(symbol, price, volume, timestamp):
	print symbol
	print price
	print volume
	print timestamp
	# add code to commit data
	working_dict[symbol].append((price, volume, timestamp))
	return 


def unpack_batch(b_request):
	quotes = b_request["Stock Quotes"]
	for quote_info in quotes:
		symbol = quote_info['1. symbol']
		price = quote_info['2. price']
		volume = quote_info['3. volume']
		timestamp = quote_info['4. timestamp']
		add_to_db(symbol, price, volume, timestamp)

ob = batch_request(['NVDA', 'MSFT'])
unpack_batch(ob)


