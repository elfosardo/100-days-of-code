
from urllib.request import urlopen
from bs4 import BeautifulSoup

PAGE_URL = 'http://store.steampowered.com/stats'


def get_the_page_html(page):
    html_code = urlopen(page)
    return html_code


def soupify_page_html(page_html):
    soup = BeautifulSoup(page_html, 'html.parser')
    return soup


if __name__ == '__main__':

    page_html = get_the_page_html(PAGE_URL)
    page_soup = soupify_page_html(page_html)
    top_games_played_column = page_soup('tr', attrs={'class':'player_count_row'})

    for line in top_games_played_column:
        game_name = line.a.get_text()
        print(game_name)
