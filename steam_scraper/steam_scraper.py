from urllib.request import urlopen
from bs4 import BeautifulSoup

FINAL_OUTPUT_FORMAT = '{:>4} {:>10} {:>10} {}'
PAGE_URL = 'http://store.steampowered.com/stats'


def get_the_page_html(page):
    html_code = urlopen(page)
    return html_code


def soupify_page_html(page_html):
    soup = BeautifulSoup(page_html, 'html.parser')
    return soup


def get_top_games_played_column(page_soup):
    top_games_played_column = page_soup('tr', attrs={'class': 'player_count_row'})
    return top_games_played_column


if __name__ == '__main__':

    page_html = get_the_page_html(PAGE_URL)
    page_soup = soupify_page_html(page_html)
    top_games_played_column = get_top_games_played_column(page_soup)
    position = 0

    for line in top_games_played_column:
        position += 1
        game_name = line.a.get_text()
        current_concurrency = line.find_all('span')[0].get_text()
        peak_concurrency = line.find_all('span')[1].get_text()
        print(FINAL_OUTPUT_FORMAT.format(position, current_concurrency, peak_concurrency, game_name))
