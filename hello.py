from typing import Set
import requests as r
import re
from bs4 import BeautifulSoup
import numpy as np

dataset = []

links = [
    'https://www.udemy.com/course/40-psychotherapy-approaches/',
    'https://www.udemy.com/course/accredited-professional-existential-psychotherapy-diploma/',
    'https://www.udemy.com/course/become-a-couples-counselor-effective-therapies-for-couples-counseling/',
    'https://www.udemy.com/course/cbt-psychotherapy-certificate-diploma-course/',
    'https://www.udemy.com/course/emerging-psychotherapy-trends/',
    'https://www.udemy.com/course/existential-therapy/',
    'https://www.udemy.com/course/fully-accredited-professional-psychotherapy-diploma-course/',
    'https://www.udemy.com/course/gestalt-psychotherapy/',
    'https://www.udemy.com/course/gestalt-therapy-training-accredited-psychotherapy-diploma-certificate/',
    'https://www.udemy.com/course/intro-psychotherapy/',
    'https://www.udemy.com/course/practical-mastery-of-psychotherapy/',
    'https://www.udemy.com/course/psychodynamic-therapy/',
    'https://www.udemy.com/course/psychotherapy-101/',
    'https://www.udemy.com/course/psychotherapy-difficult-patients-using-hypnotherapy/',
    'https://www.udemy.com/course/psychotherapy-skills/',
    'https://www.udemy.com/course/specialist-certificate-in-cognitive-behavioral-psychotherapy/',
    'https://www.udemy.com/course/three-yoga-paths-karma-yoga-bhakti-yoga-raja-yoga-online-course/',
    'https://www.udemy.com/course/transactionalanalysis/'
]

def scrape_udemy(link_to_scrape):
    request = r.get(link_to_scrape)
    soup = BeautifulSoup(request.text, 'html.parser')
    _views = soup.find('div', class_='enrollment')
    #_price = soup.find('div', class_='price-text--price-part--2npPm ud-clp-discount-price ud-heading-xxl')
    _rating = soup.find('span', class_='ud-heading-sm star-rating--rating-number--3l80q')
    #_duration = soup.find('span', class_='curriculum--content-length--5Nict')
    dataset.append([link_to_scrape, _views.text, _rating.text])

for link in links:
    scrape_udemy(link)

np.savetxt('C:/Users/mslus/ML-projects-with-Python/udemy.csv', 
           dataset,
           delimiter ="; ", 
           fmt ='% s')

print(dataset)


    

