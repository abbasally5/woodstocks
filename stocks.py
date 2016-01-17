import os, csv, requests
from bisect import bisect_left

import Quandl

auth_token = "4uugWAzRCXvytRmWXysz"
database="WIKI/"

global stocks
stocks = []
#global stockNames
#stockNames = {}

path = os.path.join(os.getcwd(), "codes.csv")
with open(path, "rb") as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		stocks.append(row[0].split("/")[1])
		#stockNames[row[0].split("/")[1]] = row[1]
csvfile.close()

#print stockNames

stocks.sort()

def binary_search(x, lo=0, hi=None):  
    print 'binary search'
    global stocks
    hi = hi if hi is not None else len(stocks)
    pos = bisect_left(stocks,x,lo,hi)          
    result = (pos if pos != hi and stocks[pos] == x else -1) 
    if (result >= 0):
    	return True
    else:
    	return False

def get_stock_data(stock_name):
	if binary_search(stock_name) is True:
		data = Quandl.get(database+stock_name, authtoken=auth_token)
		return data
	else:
		return None

def get_stock_info(stock_symbol):
	json = requests.get('http://dev.markitondemand.com/Api/v2/Quote/json?symbol=%s' % stock_symbol).json()
	exchange = requests.get('http://dev.markitondemand.com/Api/v2/Lookup/json?input=%s' % stock_symbol).json()

	json['Exchange'] = exchange[0]['Exchange']
	return json


#print binary_search('AAPL')
#data = Quandl.get(database+"AAPL", authtoken=auth_token, returns="numpy")
#name = get_stock_info('MAT')
#print name
#data = get_stock_data("AAPL")
#print data
#data.to_csv('stock.csv')