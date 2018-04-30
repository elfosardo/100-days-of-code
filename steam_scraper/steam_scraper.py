import argparse
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
    top_games_played_column = page_soup('tr',
                                        attrs={'class': 'player_count_row'})
    return top_games_played_column


def we_are_not_done_yet():
    we_are_done = False
    if current_position < final_position:
        we_are_done = True
    return we_are_done


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Print top played games'
                                                 'on Steam')
    parser.add_argument('number_of_games', metavar='[1-100]', type=int,
                        choices=range(1, 101),
                        help='Number of games to print from the top 100 list;'
                             'must be a number between 1 and 100')
    args = parser.parse_args()

    page_html = get_the_page_html(PAGE_URL)
    page_soup = soupify_page_html(page_html)
    top_games_played_column = get_top_games_played_column(page_soup)
    current_position = 0
    final_position = args.number_of_games

    while we_are_not_done_yet():
        line = top_games_played_column[current_position]
        current_position += 1
        game_name = line.a.get_text()
        current_concurrency = line.find_all('span')[0].get_text()
        peak_concurrency = line.find_all('span')[1].get_text()
        print(FINAL_OUTPUT_FORMAT.format(current_position, current_concurrency,
                                         peak_concurrency, game_name))
