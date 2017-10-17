# let's get LIT

import requests
import json
import numpy as np
import matplotlib.pyplot as plt 

with open('config.json') as data_file:
	data = json.load(data_file)

APY_KEY = data["KEY"]

# returns the JSON response of a daily request
def dailyRequest(ticker):
	r = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+ ticker +'&outputsize=full&apikey='+ API_KEY)
	response = r.json()
	return response

def dumbResponse():
	js = open('daily_test.json')
	data = json.load(js)
	return data

class Stock:
	def __init__(self, symbol, number = 1):
		self.sym = symbol
		self.count = number
		# self.value = self.getValue()

	def getLast20YearsDaily(self):
		# replace with dailyRequeest(self.sym)
		return dumbResponse()['Time Series (Daily)']

	def getLast20YearsValues(self):
		daysDict = self.getLast20YearsDaily()
		openList = []
		highList = []
		lowList = []
		closeList = []
		for day in daysDict:
			prices = daysDict[day]
			openList.append((day, float(prices["1. open"])))
			highList.append((day, float(prices["2. high"])))
			lowList.append((day, float(prices["3. low"])))
			closeList.append((day, float(prices["4. close"])))
		return (sorted(openList), sorted(highList), sorted(lowList), sorted(closeList))

	def plot20YearsHighLow(self):
		_, high, low, _ = self.getLast20YearsValues()
		high_y = [i[1] for i in high]
		low_y = [i[1] for i in low]
		date_x = [i[0] for i in high]
		plt.plot(high_y)
		plt.plot(low_y)
		plt.show()

class Portfolio:
	def __init__(self, stocks):
		self.stocks = stocks
		self.uniqueTickers = set([i.sym for i in self.stocks]) 

	def getNumberOfStocks(self):
		return sum([i.count for i in self.stocks])
	def getNumberOfUniqueStocks(self):
		return len(self.stocks)


nvidia = Stock('NVDA', 9)
# print nvidia.getLast20YearsDaily()
for i in nvidia.getLast20YearsValues():
	print i 
nvidia.plot20YearsHighLow()
bishesh = Portfolio([nvidia])

