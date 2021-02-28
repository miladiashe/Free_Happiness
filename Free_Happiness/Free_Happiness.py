from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import time

print("와들디 볼살 만질래")
# 와들디짤 긁기
# 아기 볼살을 상징하는 해시태그 선별
# 볼탱탱 볼빵빵 아기볼살 조카볼살 등등

# https://www.instagram.com/explore/tags/%EC%95%84%EA%B8%B0%EB%B3%BC%EC%82%B4/

baseurl = 'https://www.instagram.com/explore/tags/'
plusurl = input('검색할 태그 입력')
url = baseurl + quote_plus(plusurl)

print(url)
