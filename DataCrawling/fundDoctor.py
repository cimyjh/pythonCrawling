import urllib
import requests
from bs4 import BeautifulSoup
from requests_file import FileAdapter

fund_name = []
fund_type = []
fund_startDate = []
fund_cellArea = []
fund_3y = []

fund_assets = []
fund_scaleOperation = []
fund_cellAreaTxtR = []




url = 'http://www.funddoctor.co.kr/afn/topfund/fundrate1.jsp?page='

for pages in range(1, 3):
    url = url + str(pages)
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    print(url)
    print(soup)

    funds = soup.find_all('div', class_='table-list-ty3')

    j = 0
    for fund in funds:

        j = j + 1
        fund_name = fund.find('a').string
        fund_name = fund_name.strip()

        fund_3y = fund.find('div', class_='mw_ty1').get_text()

        fund_cellArea = fund.find_all('div', class_='cell-area')
        fund_cellArea = fund_cellArea[1].get_text()
        fund_cellArea = fund_cellArea.split('20')
        fund_type = fund_cellArea[0]
        fund_startDate = fund_cellArea[1].split('.')
        fund_startDate = '/'.join(fund_startDate[0:2])
        fund_startDate = '20' + fund_startDate

        fund_cellAreaTxtR = fund.find_all('div', class_='cell-area-txtR')
        fund_cellAreaTxtR = fund_cellAreaTxtR[0].get_text()
        fund_cellAreaTxtR = fund_cellAreaTxtR.split('.')
        fund_assets = fund_cellAreaTxtR[0]
        fund_scaleOperation = fund_cellAreaTxtR[1][1:]






        # fund_setAmount = fund.find('strong').string

        print(pages, '페이지의 글이며 ', j, '번째 글 입니다.')
        print(fund_name)
        print(fund_3y)
        print(fund_type)
        print(fund_startDate)

        print(fund_assets)
        print(fund_scaleOperation)
        print("-----------------------------------------------")

print('End')
