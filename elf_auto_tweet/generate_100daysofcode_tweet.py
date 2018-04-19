import argparse
import datetime

HASHTAGS = '#100DaysOfCode #python'
MYREPO_URL = 'https://github.com/elfosardo/100-days-of-code'
TODAY = datetime.datetime.now()
START_DATE = datetime.datetime(2018, 1, 14)
SKIPPED = 13


def generate_challenge_tweet(tweet_phrase, after_midnight):
    days_passed = calc_days_passed(after_midnight)
    tweet = 'day {}, {} {} {}'
    return tweet.format(days_passed, tweet_phrase, HASHTAGS, MYREPO_URL)


def calc_days_passed(after_midnight):
    days_passed = (TODAY - START_DATE).days - SKIPPED
    if after_midnight:
        days_passed -= 1
    return days_passed


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='100DaysOfCode Tweet generator')
    parser.add_argument('mytweet', metavar='Tweet', type=str,
                        help='one phrase to tweet them all, enclosed in quotation marks!')
    parser.add_argument('-am', '--after-midnight', dest='am', action='store_true',
                        help="select this to remove 1 day if you're up after midnight")
    args = parser.parse_args()
    mytweet = generate_challenge_tweet(args.mytweet, args.am)
    print(mytweet)
