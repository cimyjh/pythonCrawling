import urllib
import pymysql
import requests
import time
from bs4 import BeautifulSoup
from requests_file import FileAdapter
from traceback import format_exc


db = pymysql.connect("", "", "", "", charset='utf8mb4')
cursor = db.cursor()


etf_num = []
etf_name = []
etf_basicIndex = []

etf_cellAreaTxtR = []

etf_close = []
etf_assets = []
etf_1dY = []
etf_1wY = []
etf_1mY = []
etf_3mY = []
etf_1dVolume = []




url = 'http://www.funddoctor.co.kr/ast/etf/etf_01.jsp'

soup = BeautifulSoup(requests.get(url).text, 'html.parser')
# time.sleep(100)

# print(url)
# print(soup)

etfs = soup.find_all('div', class_='table-list-ty3')
# print(etfs)

pagesInNum = 0
for etf in etfs:
    mariaData = []
    pagesInNum = pagesInNum + 1

    etf_num = etf.find('div', class_="cell-area").string

    etf_name = etf.find('div', class_="txt-area").get_text().strip()

    etf_basicIndex = etf.find_all('div', class_="cell-area")
    etf_basicIndex = etf_basicIndex[1].string

    etf_cellAreaTxtR = etf.find_all('div', class_="cell-area-txtR")

    etf_close = etf_cellAreaTxtR[0].string.replace(',', '')
    etf_assets = etf_cellAreaTxtR[1].string.replace(',', '')
    etf_1dY = etf_cellAreaTxtR[2].string.replace(',', '')
    etf_1wY = etf_cellAreaTxtR[3].string.replace(',', '')
    etf_1mY = etf_cellAreaTxtR[4].string.replace(',', '')
    etf_3mY = etf_cellAreaTxtR[5].string.replace(',', '')
    etf_1dVolume = etf_cellAreaTxtR[6].string.replace(',', '')


    print(" ")
    print(pagesInNum, '번째 글 입니다.')
    print('펀드 고유번호:', etf_num)
    print('펀드 이름:', etf_name)
    print('펀드의 기초지수:', etf_basicIndex)
    print('펀드의 종가:', etf_close)
    print('펀드의 자산규모:', etf_assets)
    print('펀드의 1일 변동률', etf_1dY)
    print('펀드의 1주일 변동률', etf_1wY)
    print('펀드의 1개월 변동률', etf_1mY)
    print('펀드의 3개월 변동률', etf_3mY)
    print('펀드의 1일 거래량', etf_1dVolume)
    # print('펀드 3년 수익률:', etf_3y)
    # print('펀드 소유형:', etf_type)
    # print('펀드 설정일:', etf)
    #
    # print('펀드 순자산액:', etf_assets)
    # print('펀드 운용규모:', etf_scaleOperation)

    # try:
    #     mariaData.append((etf_num, etf_name, etf_type, etf_startDate, etf_3y, etf_assets, etf_scaleOperation))
    # except IndexError:
    #     print(format_exc())
    #
    # print(mariaData)

    # query = """insert into koreaEtfs(etf_num, etf_name, etf_type, etf_startDate, etf_3y, etf_assets, etf_scaleOperation) values (%s, %s, %s, %s, %s, %s, %s)"""
    # cursor.executemany(query, tuple(mariaData))
    # db.commit()
    # print('MariaDB에 insert 완료')

    print("-----------------------------------------------")
    time.sleep(1)
# time.sleep(100)

print('End')
