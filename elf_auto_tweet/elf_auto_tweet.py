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
    parser.add_argument('mytweet', metavar='T', type=str,
                        help='one phrase to tweet them all, enclosed in quotation marks!')
    parser.add_argument('-c', dest='challenge', action='store_true',
                        help='send the 100DaysOfCoding challenge tweet')
    parser.add_argument('-t', dest='test', action='store_true',
                        help='print the tweet instead of sending it')
    args = parser.parse_args()

    mytweet = args.mytweet

    if args.challenge:
        mytweet = generate_challenge_tweet(args.mytweet)

    if args.test:
        print(mytweet)
    else:
        send_tweet(mytweet)
