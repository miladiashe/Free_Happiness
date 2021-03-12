from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import time

# 와들디짤 긁기
# 아기 볼살을 상징하는 해시태그 선별
# 볼탱탱 볼빵빵 아기볼살 조카볼살 등등


baseurl = 'https://www.instagram.com/explore/tags/'
plusurl = input('검색할 태그 입력')
url = baseurl + quote_plus(plusurl)

driver = webdriver.Chrome()
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html)

insta = soup.select('.v1Nh3.kIKUG._bz0w')

print(insta)

driver.close
