import urllib
import requests
from bs4 import BeautifulSoup
from  requests_file import FileAdapter


url = "http://www.naver.com"
response = urllib.request.urlopen(url)
html_ = response.read().decode()
soup = BeautifulSoup(html_, 'html.parser')
print(soup.title)



response = requests.get('http://www.naver.com')
soup = BeautifulSoup(response.text, 'html.parser')
result = soup.find_all('div', 'thumb_box _NM_NEWSSTAND_THUMB _NM_NEWSSTAND_THUMB_press_valid')
print(len(result))

list_ = []
for i in result:
    list_.append(i.find('img')['alt'])
print(list_)


url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
response = requests.get(url)
soup =BeautifulSoup(response)



