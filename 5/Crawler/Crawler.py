import requests
import re
from bs4 import BeautifulSoup
import time
import random

max_count = 101
url = 'https://www.business-gazeta.ru'#'http://www.selfcreation.ru/category/zdorove'#'http://fanserials.golf'
def crawl_web(initial_url):
    to_crawl = []
    crawled = set()
    to_crawl.append(initial_url)

    while to_crawl:
        print(random.random())
        time.sleep(random.random())
        current_url = to_crawl.pop(0)
        r = requests.get(current_url)
        crawled.add(current_url)
        for url in re.findall('<a href="([^"]+)">', str(r.content)):
            if url[0] == '/':
                url = current_url + url
            pattern = re.compile('https?')
            if pattern.match(url):
                to_crawl.append(url)
                print(str(len(crawled)) + url)
            if len(crawled) >= max_count:
                  return crawled
    if len(crawled) >= max_count:
        return crawled
    return crawled

file = open('urls.json', 'w')
crawled = crawl_web(url)
ursString = '{\n'
index = 0
for url in crawled:
    time.sleep(random.random())
    index += 1
    print(str(index) + url)
    if index < max_count:
     ursString += '  "' + str(index) + '": "' + url + '",\n'
    else:
     ursString += '  "' + str(index) + '": "' + url + '"\n'

    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    for script in soup(["script", "style"]):
        script.decompose()
    filePage = open(str(index) + '.txt', 'w')
    filePage.write(soup.get_text(strip=True, separator=" "))
    filePage.close()

ursString += '}'

file.write(ursString)
file.close()