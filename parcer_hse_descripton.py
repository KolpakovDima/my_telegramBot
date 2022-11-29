import requests
from bs4 import BeautifulSoup as BS

import parser_hse_urls

hse_directions = requests.get("https://www.hse.ru/n/education/bachelor?campus=51999662")
soup = BS(hse_directions.content, 'lxml')

directions = soup.find_all("span", class_="e-card__title-inner")

for pages in range(2, 5):
    hse_directions_2 = requests.get(f'https://www.hse.ru/n/education/bachelor/page/{pages}/?campus=51999662')
    soup_2 = BS(hse_directions_2.content, 'lxml')
    title_2 = soup_2.find_all("span", class_="e-card__title-inner")
    directions += title_2

all_directions = {}
all_directions_with_urls = {}

i = 1
for iterator in directions:
    all_directions[i] = [iterator.text]
    i += 1

all_directions_with_urls[all_directions[1][0]] = parser_hse_urls.all_urls[1][0]
for i in range(3, 68):
    all_directions_with_urls[all_directions[i][0]] = parser_hse_urls.all_urls[i][0]
