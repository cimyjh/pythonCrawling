import urllib
import requests
from bs4 import BeautifulSoup
from  requests_file import FileAdapter


#url
url = "http://www.naver.com"
response = urllib.request.urlopen(url)
html_ = response.read().decode()
soup = BeautifulSoup(html_, 'html.parser')
print(soup.title)


#신문사 가져오기
response = requests.get('http://www.naver.com')
soup = BeautifulSoup(response.text, 'html.parser')
result = soup.find_all('div', 'thumb_box _NM_NEWSSTAND_THUMB _NM_NEWSSTAND_THUMB_press_valid')
print(len(result))

list_ = []
for i in result:
    list_.append(i.find('img')['alt'])
print(list_)



#네이버 영화 순위 가져오기
url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
response = requests.get(url)
soup =BeautifulSoup(response.text, 'html.parser')
list_ = soup.find_all('div', 'tit3')
for i in range(len(list_)):
    print('{:2}위: {}'.format(i+1, list_[i].find('a')['title']))



#네이버 뉴스의 HeadLine 가져오기
url = 'https://news.naver.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text,'html.parser')
head_line_news = []

result = soup.find_all('div', class_ = 'hdline_flick_item')
for i in result:
    head_line_news.append(i.find('p', class_ = 'hdline_flick_tit').string)

result1 = soup.find_all('div', class_ = 'hdline_article_tit')
for i in result1 :
    head_line_news.append(i.find('a').string.strip())

for i in head_line_news:
    print(i)












