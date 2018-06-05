import urllib.request
from bs4 import BeautifulSoup

quote_page = 'https://finance.yahoo.com/quote/SPY?p=SPY'
page = urllib.request.urlopen(quote_page)
soup = BeautifulSoup(page, 'html.parser')
name_box = soup.find('span')

name = name_box.strip()
print (name)