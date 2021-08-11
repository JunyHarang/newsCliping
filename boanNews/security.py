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
newsMainLine = soup.find('div', attrs={'class': 'news_main'})

# print(newsMainLine)
# print(len(newsMainLine))
# print('=' * 100)

# print(newsList)
# print(len(newsList))
# print('=' * 100)


# newsDaily = soup.findAll("span", {"class": "news_writer"})

newsDaily = soup.select("div.news_list > span.news.writer")

print(newsDaily)


# dyaPattern = '\d+.(\d+).(\d+).'

# r = re.compile(dyaPattern)
# match = r.search()


def main_news_crawling():
    print("mainNews()가 시작 되었습니다.")
    print("-" * 100)
    print("Crawling이 시작 됩니다.\n")

    main_titles = []
    main_contents = []

    main_title_bundle = []
    main_content_bundle = []

    main_titles = soup.findAll("div", {"class": "news_main_title"})
    main_contents = soup.findAll("div", {"class": "news_main_txt"})
    main_contents_extract = soup.find_all('\n', 'br', 'div', 'p', 'img')

    for main_news_title in main_titles:
        main_title_bundle.append(main_news_title.get_text())

    print('=' * 100)
    print("Security Main News Top3 제목을 출력합니다.")
    print('-' * 100)
    print(main_title_bundle)
    print('=' * 100 + "\n")

    for main_news_content in main_contents:
        main_content_bundle.append(main_news_content.get_text('\n', strip=True))

    print("Security Main News Top3 내용을 출력합니다.")
    print('-' * 100)
    print(main_content_bundle)
    print('=' * 100 + "\n")


def general_news_crawling():
    news_titles = []
    news_contents = []
    news_infos = []

    news_title_list = []
    news_content_list = []
    news_info_list = []
    writer_list = []

    for news in newsList:
        news_titles = soup.findAll("span", {"class": "news_txt"})
        news_contents = soup.findAll("a", {"class": "news_content"})
        news_infos = soup.findAll("span", {"class": "news_writer"})

    for news_title in news_titles:
        news_title_list.append(news_title.get_text())

    print('=' * 100)
    print("Security 일반 News 제목을 출력합니다.")
    print('-' * 100)
    print(news_title_list)
    print('=' * 100 + "\n")

    for news_content in news_contents:
        news_content_list.append(news_content.get_text())

    print("Security 일반 News 내용을 출력합니다.")
    print('-' * 100)
    print(news_content_list)
    print('=' * 100 + "\n")

    for news_info in news_infos:
        news_info_list.append(news_info.get_text())

    temp = str(news_info_list).split('|')
    temp = str(temp).split(',')

    print(temp[1])

    print("Security 일반 News 기자와 작성일을 출력합니다.")
    print('-' * 100)
    print(temp)
    print('=' * 100 + "\n")


main_news_crawling()
general_news_crawling()
