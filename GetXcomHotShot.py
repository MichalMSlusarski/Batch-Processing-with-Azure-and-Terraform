from os import name
import requests
from dataclasses import dataclass
from typing import Set, Tuple

@dataclass
class HotShot:
    promotion_name: str
    promotion_total_count: int

def get_xkom_hotshot_product_data() -> HotShot:

    headers = {
        'authority': 'mobileapi.x-kom.pl',
        'method': 'GET',
        'path': '/api/v1/xkom/hotShots/current?onlyHeader=true&commentAmount=15',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'x-api-key': 'jfsTOgOL23CN2G8Y'
    }

    response = requests.get('https://mobileapi.x-kom.pl/api/v1/xkom/hotShots/current?onlyHeader=true&commentAmount=15', headers=headers)
    
    response.encoding = 'br'

    r = response.json()

    HotShot.promotion_name = r['PromotionName']
    HotShot.promotion_total_count = r['PromotionTotalCount']

    return HotShot

def get_matching_keywords(name: str, keywords: Set[str]) -> Set[str]:

    name = name.lower()
    keywords = [keyword.lower() for keyword in keywords]

    found_keywords = set()
    for keyword in keywords:
        if keyword in name:
            found_keywords.add(keyword)

    return found_keywords


def check_xkom_hotshot(keywords: Set[str]) -> Tuple[HotShot, Set[str]]:

    _HotShot = get_xkom_hotshot_product_data()
    _name = _HotShot.promotion_name
    _keywords = get_matching_keywords(_name, keywords)

    return _HotShot(_HotShot.promotion_name, _HotShot.promotion_total_count), _keywords
