from typing import Set
import requests
from bs4 import BeautifulSoup
import re

def get_recepie_links(keyword: str) -> Set[str]:

    base_url = 'https://www.kwestiasmaku.com'
    request_url = base_url + '/szukaj?search_api_views_fulltext=' + keyword

    recipies = [] 
    paths = [] 
    links = [] 

    response = requests.get(request_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    recipies = soup.find_all('a', attrs={'href': re.compile('^(/przepis/)')})
    
    for link in recipies:
      paths.append(link.get('href'))

    for link in paths:
      link = base_url + link
      links.append(link)

    links = list(dict.fromkeys(links)) #remove duplicates

    return links
