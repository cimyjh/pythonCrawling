#
# 작성자: 윤재형
# 프로그램의 목적: 네이버 스포츠에서 현재 KBO 순위를 웹 크롤링하는 것
# 작성일: 2020년 7월 1일
#
import random

import requests
import time
from bs4 import BeautifulSoup

teamNums = 0
teamName = []


url = 'https://sports.news.naver.com/kbaseball/record/index.nhn?category=kbo'
soup = BeautifulSoup(requests.get(url).text, 'html.parser')
teams = soup.find_all('td', class_='tm')

for team in teams:
    teamNums = teamNums + 1
    teamName = team.find('span').get_text()
    print(teamNums, " 위: ", teamName)

print('End')