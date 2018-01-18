import datetime

HASHTAGS = '#100DaysOfCode #python'
MYREPO_URL = 'https://github.com/elfosardo/100-days-of-code'
TODAY = datetime.datetime.now()
START_DATE = datetime.datetime(2018, 1, 14)


def generate_tweet():
    days_passed = calc_days_passed()
    tweet = "day ", days_passed
    return tweet


def calc_days_passed():
    days_passed = (TODAY - START_DATE).days
    return days_passed


mytweet = generate_tweet()
print(mytweet)
