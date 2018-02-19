import argparse
import datetime

HASHTAGS = '#100DaysOfCode #python'
MYREPO_URL = 'https://github.com/elfosardo/100-days-of-code'
TODAY = datetime.datetime.now()
START_DATE = datetime.datetime(2018, 1, 14)
SKIPPED = 1


def generate_challenge_tweet(tweet_phrase):
    days_passed = calc_days_passed()
    tweet = 'day {}, {} {} {}'
    return tweet.format(days_passed, tweet_phrase, HASHTAGS, MYREPO_URL)


def calc_days_passed():
    days_passed = (TODAY - START_DATE).days - SKIPPED
    return days_passed


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='100DaysOfCode Tweet generator')
    parser.add_argument('tweet_phrase', metavar='P', type=str,
                        help='one phrase to tweet them all, enclosed in quotation marks!')
    args = parser.parse_args()
    mytweet = generate_challenge_tweet(args.tweet_phrase)
    print(mytweet)
