import argparse
from config import api, logging
from generate_100daysofcode_tweet import generate_challenge_tweet


def send_tweet(tweet):
    try:
        api.update_status(tweet)
        logging.info('Tweet sent to Twitter')
    except Exception as e:
        logging.error('Error sending tweet to Twitter: ', e)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Tweet from command line')
    parser.add_argument('mytweet', metavar='Tweet', type=str,
                        help='one phrase to tweet them all, enclosed in'
                             'quotation marks!')
    parser.add_argument('-c', '--challenge', action='store_true',
                        help='send the 100DaysOfCoding challenge tweet')
    parser.add_argument('-am', '--after-midnight', action='store_true',
                        help='remove 1 day from code challenge if posting'
                             'after midnight')
    parser.add_argument('-t', '--test', action='store_true',
                        help='print the tweet instead of sending it')
    args = parser.parse_args()

    mytweet = args.mytweet

    if args.challenge:
        after_midnight = args.after_midnight
        mytweet = generate_challenge_tweet(args.mytweet, after_midnight)

    if args.test:
        print(mytweet)
    else:
        send_tweet(mytweet)
