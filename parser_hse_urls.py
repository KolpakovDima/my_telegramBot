import requests
from bs4 import BeautifulSoup as BS

hse_directions = requests.get("https://www.hse.ru/n/education/bachelor?campus=51999662")
soup = BS(hse_directions.content, 'lxml')

directions_url = soup.find_all("a", class_="e-card e-cards__item")

for pages in range(2, 5):
    hse_directions_urls = requests.get(f'https://www.hse.ru/n/education/bachelor/page/{pages}/?campus=51999662')
    soup_2 = BS(hse_directions_urls.content, 'lxml')
    urls_req_2 = soup_2.find_all("a", class_="e-card e-cards__item")
    directions_url += urls_req_2
all_urls = {}
it = 1
for urls in directions_url:
    all_urls[it] = [urls.get("href")]
    it += 1
