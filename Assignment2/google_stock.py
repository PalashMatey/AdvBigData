###############################################################
#
#Code collaborations : Anubha Bhargava, Maanit Mehra, Zoltan Onodi Scuz
#			Ashish Nanda
#Idea Collaborations: Paul Jaquet
#Original Code : Palash Sushil Matey
#
#
############################################################
import csv
import numpy as np
import requests
import scipy as sp
import sklearn as sl
import math
import pandas as pd
from functools import reduce
import os
import os.path
mport sys
import datetime as dt
import pandas as pd
import pandas.io.data as pio
from pandas import Series
from yahoo_finance import Share
import yahoo_finance as yhf
from datetime import date
import numpy as np
from sklearn import gaussian_process
import datetime

INTERVAL = 60 #sec
GOOGLE_QUOTE_URL = "http://www.google.com/finance/getprices?f=d,o,h,l,c,v&df=cpct&i="+str(INTERVAL)+"&q="
PATH = "./DATA/"
final = []
flag = False
## This function collects detailed data from the Google Finance API
## for each Ticker symbol. It saves this data in a file named after the company 
## input. 
def getHistory(symbol,company):
	global final
	flag = True
	filename = PATH + company + ".csv"
	try:
		os.remove(filename)
	except:
		pass

	try:
		file = open (filename, "a+")
	except:
		file = open (filename, "w+")

	stock_url = GOOGLE_QUOTE_URL + symbol
	resp = requests.get(stock_url)
	resp_filter = resp.text.split(" ")
	
	## From 6 to exclude the textual information, upto -1 to exclude the last \n
	text_list = resp_filter[0].split("\n")[7:-1]
	file.write("TIME,CLOSE,HIGH,LOW,OPEN,VOLUME\n")
	i = 0
	time1 = []
	open1 = []
	for row in text_list: 
		file.write(row+"\n")
		line = row.split(',')
		time1.append(line[0])
		open1.append(line[4])
		#for i in range(0,):
		#	if i%10 == 0:
		#		print (line[i])
#	file.write(resp_filter)
	file.close()	
	#print (time1)
	#print (open1)
	last = []
	arr = []
	for t,o in zip(time1,open1):
		try:
			if float(t)%10 == 0:
				o = float(o)
				last.append(o)
		except:
			pass
	#cprice = last
	#print (arr)
	
	if flag == True:	
		avg = (float(last[-1])-float(last[-2]))*0.56 + float(last[-1]) 
		avg = round(avg,2)
	#print (avg)
		final.append(avg)
	#print (company+ avg)
	#print (last)
def main():


	
        reader=csv.DictReader(open('Yahoo_symbols.csv','r'))
        company_list=[]
        sym_list=[]
        for sym in reader:
                company=sym["COMPANY"]
                symbol=sym["SYMBOL"]
                company_list.append(company)
                sym_list.append(symbol)
#        print (sym_list)
        for i in range(0,len(sym_list)):
#		print sym_list[i]
                getHistory(sym_list[i], company_list[i])

main()




onealgo = []
twoalgo = []
current = []

def Predict(company, today):
    London = pio.get_data_yahoo(
        '^FTSE',
        start = dt.datetime(2016, 2, 19),
        end = dt.datetime(2016, 3, 10))
    #print (London['Open'])
    London = (London.sub(London['Close'],axis=0))
    #print (London)    
    lprice = London['Open']
    l_mat = lprice.as_matrix()    
    #print (len(l_mat))
    #print(l_mat.ndim)
    #print ('Printn')
    #print (l_mat)
    df = pio.get_data_yahoo(
        company,
        start = dt.datetime(2015, 1, 1),
        end = dt.datetime(today.year, today.month, today.day))
    df.loc[today] = (Share(company).get_open(),
Share(company).get_days_high(), Share(company).get_days_low(),
Share(company).get_price(), Share(company).get_volume(),
float(Share(company).get_price()))
    closing = df['Adj Close']
    moving_avg = pd.rolling_mean(closing, 10)
    ewma = pd.ewma(closing, span = 3)
    onealgo.append(str(getPrice(closing,moving_avg,ewma)))
    #print ("\n" + "Estimate Price of " + company + " @ " + str(today + dt.timedelta(days=1)) + ": ")
    #print ("  " + str(predictPrice(closing, moving_avg, ewma)))
#########################################################################################################################################
###Formula online, paper link attached in the References. 
#########################################################################################################################################
def getPrice(closing, moving_average, ewma):
    
    gr = (1 - 5 ** 0.5) / 2
    return ((ewma[-1] - ewma[-2]) * (gr)
            + (moving_average[-1] - moving_average[-2]) * (1 - gr)
            + closing[-1])

if __name__ == '__main__':
    stocks = ['BAC', 'C', 'IBM', 'AAPL', 'GE', 'T', 'MCD', 'NKE', 'TWTR', 'TSLA']
    today = dt.date.today() - dt.timedelta(days=0)
    #today = dt.datetime(2016,3,9)
    for stock in stocks:
        Predict(stock, today)
avg = 0.0
list1 = []
for i,n in zip(onealgo,final):
	i = float(i)
	n = float(n)
	i = round(i,2)	
	#print (i,n)
	avg = (i+n)/2
	avg = round(avg,2)
	list1.append(avg)
 
#print (list1)
for i,n in zip(stocks,list1):
	print (str(i)+'     '+ str(n))

