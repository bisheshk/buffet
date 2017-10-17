import market_tools as mt
import matplotlib.pyplot as plt 

class Stock:
	def __init__(self, symbol, number = 1):
		self.sym = symbol
		self.count = number
		# self.value = self.getValue()

	def getLast20YearsDaily(self):
		# replace with dailyRequeest(self.sym)
		return mt.dumbResponse()['Time Series (Daily)']

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
