import urllib
import requests
from bs4 import BeautifulSoup
from  requests_file import FileAdapter

fund_name = []
fund_setAmount = []
#fund_1m = []

url = 'https://finance.naver.com/fund/fundList.nhn?search=AIN&sortOrder=m1&page='

for i in range(1, 130):
    url = url + str(i)
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    funds = soup.find_all('td', class_='text')
    for fund in funds:
        fund_name = fund.find('a', target='_top').string
        fund_setAmount = fund.find('strong').string
        print(i)
        print(fund_name)
        print(fund_setAmount)
        print("---------------------------")
print('End')
