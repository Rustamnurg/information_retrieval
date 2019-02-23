import requests
import re
from bs4 import BeautifulSoup

url = 'https://www.pravda.ru'
def crawl_web(initial_url):
    to_crawl = []
    crawled = set()
    to_crawl.append(initial_url)
    max_count = 50

    while to_crawl:
        current_url = to_crawl.pop(0)
        r = requests.get(current_url)
        crawled.add(current_url)
        for url in re.findall('<a href="([^"]+)">', str(r.content)):
            if url[0] == '/':
                url = current_url + url
            pattern = re.compile('https?')
            if pattern.match(url):
                soup = BeautifulSoup(r.content, 'html.parser')
                for script in soup(["script", "style"]):
                    script.decompose()
                file = open(str(len(crawled)) + '.txt', 'w')
                file.write(soup.get_text(strip=True, separator=" "))
                file.close()
                to_crawl.append(url)
                print(str(len(crawled)) + url)
            if len(crawled) >= max_count:
                  return crawled
    if len(crawled) >= max_count:
        return crawled
    return crawled

file = open('urls.txt', 'w')
crawled = crawl_web(url)
ursString = ''
for url in crawled:
    ursString += url + '\n'
file.write(ursString)
file.close()
