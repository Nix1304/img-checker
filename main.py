from time import sleep

from requests import Session
from bs4 import BeautifulSoup

sitemap_url = 'https://unmei.nix13.dev/sitemap.xml'
urls = ['https://vk.com/1fdsgfdgdfg']
s = Session()
s.headers.update({'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36'})


with s.get('https://shikimori.one/animes/245-great-teacher-onizuka') as r:
    soup = BeautifulSoup(r.text, features="html.parser")
    for img in soup.find_all('img'):
        urls.append(img['src'])

broken_urls = []
for url in urls:
    with s.get(url) as r:
        print(f'checking url {url}')
        if r.status_code != 200:
            broken_urls.append(url)
        sleep(.1)

print(f'broken url: {len(broken_urls)}')
if len(broken_urls) > 0:
    with open('urls.txt', 'w') as file:
        file.write('\n'.join(broken_urls))
