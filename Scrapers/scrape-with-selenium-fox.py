from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
import lxml

driver = webdriver.Chrome(executable_path='D:/Pliki Pobrane/chromedriver_win32/chromedriver.exe')

links = []

data = []

def scrape_link(link_to_scrape):
    driver.get(link_to_scrape)
    sleep(15)
    soup = BeautifulSoup(driver.page_source, "lxml")
    _views = soup.find('div', class_='enrollment')
    _price = soup.find('div', class_='price-text--price-part--2npPm ud-clp-discount-price ud-heading-xxl')
    _rating = soup.find('span', class_='ud-heading-sm star-rating--rating-number--3l80q')
    _duration = soup.find('span', class_='curriculum--content-length--5Nict')
    print(_views, _duration)
    sleep(5)

for link in links:
    scrape_link(link)

driver.close()
    