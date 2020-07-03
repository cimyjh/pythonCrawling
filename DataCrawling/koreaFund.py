import urllib
import pymysql
import requests
import time
from bs4 import BeautifulSoup
from requests_file import FileAdapter
from traceback import format_exc


fund_num = []
fund_name = []
fund_type = []
fund_startDate = []
fund_cellArea = []
fund_3y = []

fund_assets = []
fund_scaleOperation = []
fund_cellAreaTxtR = []


for pages in range(16, 57):
    url = 'http://www.funddoctor.co.kr/afn/topfund/fundrate1.jsp?page='
    url = url + str(pages)
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    # time.sleep(30)
    print(url)

    funds = soup.find_all('div', class_='table-list-ty3')

    pagesInNum = 0
    for fund in funds:
        mariaData = []
        pagesInNum = pagesInNum + 1

        fund_num = fund.find('div', id="morechk").string

        fund_name = fund.find('div', class_="inputChk")
        fund_name = str(fund_name)
        fund_name = fund_name.split('title=')[1].split(' 선택')[0][1:]

        fund_3y = fund.find('div', class_='mw_ty1').get_text()
        fund_3y = fund_3y.split('(')[0]

        fund_cellArea = fund.find_all('div', class_='cell-area')
        fund_cellArea = fund_cellArea[1].get_text()

        print(fund_cellArea)

        if '19' in fund_cellArea:
            fund_cellArea = fund_cellArea.split('19')
        else:
            fund_cellArea = fund_cellArea.split('20')


        print(fund_cellArea)


        fund_type = fund_cellArea[0]

        fund_startDate = fund_cellArea[1].split('.')
        fund_startDate = '/'.join(fund_startDate[0:2])
        fund_startDate = '20' + fund_startDate

        fund_cellAreaTxtR = fund.find_all('div', class_='cell-area-txtR')
        fund_cellAreaTxtR = fund_cellAreaTxtR[0].get_text()
        fund_cellAreaTxtR = fund_cellAreaTxtR.split('.')
        fund_assets = fund_cellAreaTxtR[0].replace(',', '')
        fund_scaleOperation = fund_cellAreaTxtR[1][1:].replace(',', '')


        print(" ")
        print(pages, '페이지의 글이며 ', pagesInNum, '번째 글 입니다.')
        print('펀드 고유번호:', fund_num)
        print('펀드 이름:', fund_name)
        print('펀드 3년 수익률:', fund_3y)
        print('펀드 소유형:', fund_type)
        print('펀드 설정일:', fund_startDate)

        print('펀드 순자산액:', fund_assets)
        print('펀드 운용규모:', fund_scaleOperation)

        try:
            mariaData.append((fund_num, fund_name, fund_type, fund_startDate, fund_3y, fund_assets, fund_scaleOperation))
        except IndexError:
            print(format_exc())

        print(mariaData)

        print("-----------------------------------------------")
        #time.sleep(1)

    time.sleep(3)

print('End')
