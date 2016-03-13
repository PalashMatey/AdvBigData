import time
from yahoo_finance import Share
share = 'WMT'
stocks_price = []
def getPrice(share):
	for x in range(0, 30):
	
		price = Share(share)
		print price.get_price()
		stocks_price.append(price.get_price)
		
		time.sleep(60)
	print 'Share information recieved'
getPrice(share)
