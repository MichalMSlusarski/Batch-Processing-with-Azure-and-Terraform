from typing import Set
import requests as r
import re
from bs4 import BeautifulSoup
import numpy as np

dataset = []

link_to_scrape = 'https://corewellceu.com/recorded-webinar'

request = r.get(link_to_scrape)
soup = BeautifulSoup(request.text, 'html.parser')
insite_links = soup.find_all('a', attrs={'href'})
print(insite_links)
_description = soup.find('div', class_='info')
dataset.append(insite_links)

np.savetxt('C:/Users/mslus/ML-projects-with-Python/udemy.csv', 
           dataset,
           delimiter ="; ", 
           fmt ='% s')

print(dataset)