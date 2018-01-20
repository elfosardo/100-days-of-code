
from urllib.request import urlopen
from bs4 import BeautifulSoup

PAGE_URL = 'http://store.steampowered.com/'


def get_the_page_html(page):
    html_code = urlopen(page)
    return html_code


def soupify_page_html(page_html):
    soup = BeautifulSoup(page_html, 'html.parser')
    return soup


if __name__ == '__main__':

    page_html = get_the_page_html(PAGE_URL)
    page_soup = soupify_page_html(page_html)

    special_offers = page_soup.find('div', attrs={'class':'home_page_content special_offers'})

    print(special_offers)
