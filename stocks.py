import os
import csv
from bisect import bisect_left

import Quandl

auth_token = "4uugWAzRCXvytRmWXysz"
database="WIKI/"

global stocks
stocks = []

path = os.path.join(os.getcwd(), "codes.csv")
with open(path, "rb") as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		stocks.append(row[0].split("/")[1])

stocks.sort()

def binary_search(a, x, lo=0, hi=None):   
    hi = hi if hi is not None else len(a)    
    pos = bisect_left(a,x,lo,hi)          
    result = (pos if pos != hi and a[pos] == x else -1) 
    if (result >= 0):
    	return True
    else:
    	return False

print binary_search(stocks, 'AAPL')
data = Quandl.get(database+"AAPL", authtoken=auth_token, returns="numpy")
print data