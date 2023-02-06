from typing import Set
import requests as r
import re
from bs4 import BeautifulSoup
import numpy as np

dataset = []

links = [
    'https://www.udemy.com/course/child-psychology/',
    'https://www.udemy.com/course/fully-accredited-professional-child-psychology-diploma/',
    'https://www.udemy.com/course/child-psychology-and-development/',
    'https://www.udemy.com/course/intro-child-psychology/',
    'https://www.udemy.com/course/child-psychology-course/',
    'https://www.udemy.com/course/child-psychology-social-emotional-cognitive-development/',
    'https://www.udemy.com/course/child-psychology-certification-course-aggression-prevention/',
    'https://www.udemy.com/course/clinical-child-psychology-diploma-for-child-care/',
    'https://www.udemy.com/course/child-psychology-learning-and-development/',
    'https://www.udemy.com/course/accredited-child-psychology-counseling-diploma-certificate-parenting/',
    'https://www.udemy.com/course/basics-of-child-psychology/',
    'https://www.udemy.com/course/childpsychologydeepperspective/',
    'https://www.udemy.com/course/fully-accredited-diploma-in-child-psychology/',
    'https://www.udemy.com/course/child-psychology-diploma-accredited-certificate/',
    'https://www.udemy.com/course/child-psychology-masterclass-whats-in-your-childs-brain/',
    'https://www.udemy.com/course/advanced-child-psychology-certificate-crash-course/',
    'https://www.udemy.com/course/childpsychology/',
    'https://www.udemy.com/course/learn-psychological-perspective-of-education-and-learning/',
    'https://www.udemy.com/course/childsafety/',
    'https://www.udemy.com/course/parenting-and-child-psychology-teaching-technics/'
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


    

