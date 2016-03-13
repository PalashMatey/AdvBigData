import requests
import os.path
from bs4 import BeautifulSoup as bs
import os


page="http://finance.yahoo.com/q/h?s=IBM&t=2015-03-02"

response = requests.get(page)
html = response.content
soup = bs(html)
print soup.find('a').text
#table = soup.find_all('a')
#print table.string

#print soup.prettify()
#print html
