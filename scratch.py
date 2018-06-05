import urllib.request
import sys
from bs4 import BeautifulSoup

print('Type symbol:')
symbol_pick = input()

quote_page = 'https://www.bloomberg.com/quote/' + symbol_pick
page = urllib.request.urlopen(quote_page)
soup = BeautifulSoup(page.read(), 'html.parser')
price_box = soup.find('meta', {"itemprop" : "price"})
print(price_box['content'])
