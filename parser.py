from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

def get_link(url):
    req = Request(
        url=url,
        headers={'User-Agent': 'Mozilla/5.0'},
    )
    webpage = urlopen(req)
    sourse = webpage.read()
    soup = BeautifulSoup(sourse, "lxml")
    url_ = soup.find('source').get('src')
    print('parse successfull')
    return url_


