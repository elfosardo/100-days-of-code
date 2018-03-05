import argparse
import requests
import config as cfg


def get_arguments():
    parser = argparse.ArgumentParser('Currency converter based on openexchange rates')
    mx_group = parser.add_mutually_exclusive_group()
    mx_group.add_argument('-c', '--get-currencies-list', dest='get_curr_list', action='store_true',
                          help='display available currencies list and exit')
    sub_group = mx_group.add_argument_group()
    sub_group.add_argument('-a', '--amount', dest='from_curr_amount',
                           help='amount to convert')
    sub_group.add_argument('-f', '--from-currency', dest='from_curr',
                           help='currency to convert from')
    sub_group.add_argument('-t', '--to-currency', dest='to_curr',
                           help='currency to convert to')
    arguments = parser.parse_args()
    return arguments


def collect_data(data_type):
    api_url = '{}/{}.json?app_id={}'.format(cfg.API_URL, data_type, cfg.api_key)
    json_data = requests.get(api_url).json()
    return json_data


def get_latest_rates():
    latest_rates = collect_data('latest')
    return latest_rates


def get_valid_currencies():
    valid_currencies = collect_data('currencies')
    return valid_currencies


def print_valid_currencies():
    valid_currencies = get_valid_currencies()
    print('Available Currencies:')
    for i, k in valid_currencies.items():
        print(i, k)
    exit()


def get_currency_rate(currency):
    my_latest_rates = get_latest_rates()
    currency_rate = my_latest_rates['rates'][currency]
    return currency_rate


def convert_currencies(from_curr_amount, to_curr_rate, from_curr_rate):
    to_curr_value = float(from_curr_amount) * to_curr_rate / from_curr_rate
    return to_curr_value


def validate_currency(currency):
    try:
        my_valid_currencies = get_valid_currencies()
        if currency not in my_valid_currencies:
            raise KeyError
    except KeyError:
        exit('Currency not valid: {}'.format(currency))


if __name__ == '__main__':
    args = get_arguments()

    if args.get_curr_list:
        print_valid_currencies()

    for my_currency in [args.from_curr, args.to_curr]:
        validate_currency(my_currency)

    my_from_curr_rate = get_currency_rate(args.from_curr)
    my_to_curr_rate = get_currency_rate(args.to_curr)

    to_curr_final_value = convert_currencies(from_curr_amount=args.from_curr_amount,
                                             to_curr_rate=my_to_curr_rate,
                                             from_curr_rate=my_from_curr_rate)

    print('{} {} = {} {}'.format(args.from_curr_amount,
                                 args.from_curr,
                                 to_curr_final_value,
                                 args.to_curr))
