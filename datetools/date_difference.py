import argparse
from datetime import datetime


def get_arguments():
    parser = argparse.ArgumentParser(description='Calculate number of days between two dates')
    parser.add_argument('starting_date',
                        help='Starting date; should be in the format "dd/mm/year"')
    parser.add_argument('end_date',
                        help='Ending date; should be in the format "dd/mm/year"')
    args = parser.parse_args()
    return args


def convert_date(my_date_str):
    my_date = datetime.strptime(my_date_str, '%d/%m/%Y')
    return my_date


def get_days_between_dates(sd, ed):
    ed_date = convert_date(ed)
    sd_date = convert_date(sd)
    days_between_dates = ed_date - sd_date
    return days_between_dates.days


if __name__ == '__main__':
    my_args = get_arguments()
    my_days_between_dates = get_days_between_dates(my_args.starting_date,
                                                   my_args.end_date)

    print('days between dates: {}'.format(my_days_between_dates))
