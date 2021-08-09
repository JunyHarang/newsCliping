from bs4 import BeautifulSoup
import ssl
import re

import requests

from urllib.request import urlopen

# 보안뉴스 오늘날짜 기사 가져오기

context = ssl._create_unverified_context()
securityURL = urlopen('https://www.boannews.com/media/list.asp?Page=1&mkind=1', context=context)
soup = BeautifulSoup(securityURL, 'html.parser')

newsList = soup.find('div', attrs={'id': 'news_area'})

print(newsList)
print(len(newsList))
print('=' * 100)

mainNews = []

newsDaily = soup.findAll("span", {"class": "news_writer"})
dyaPattern = '\d+.(\d+).(\d+).'

r= re.compile(dyaPattern)
match = r.search()



for news in newsList:
    mainTitle = soup.findAll("div", {"class": "news_main_title"})
    mainContent = soup.findAll("div", {"class": "news_main_txt"})
    mainPicture = soup.findAll("img", {"class": "news_img"})
    mainNews = mainTitle, mainContent, mainPicture

print(mainNews)
print(len(mainNews))
print('=' * 100)
