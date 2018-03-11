import argparse

from fibonacci_graph import FibonacciGraph


def fibonacci(digit):
    if digit < 2:
        return digit
    else:
        sequence_value = fibonacci(digit - 1) + fibonacci(digit - 2)
        return sequence_value


def calculate_sequence():
    i = 0
    sequence = {}
    while i <= args.digits:
        result = fibonacci(digit=i)
        sequence[i] = result
        i += 1
    return sequence


def check_positive_int(value):
    if value < 0:
        raise argparse.ArgumentTypeError('{} is not a positive integer'.format(value))
    return value


def get_arguments():
    parser = argparse.ArgumentParser('Calculate Fibonacci sequence')
    parser.add_argument('digits',
                        type=int,
                        help='Sequence to calculate; starts from 0')
    parser.add_argument('-p', '--position', dest='position', action='store_true',
                        help='Calculate only single position in sequence')
    arguments = parser.parse_args()
    return arguments


if __name__ == '__main__':
    args = get_arguments()

    check_positive_int(args.digits)

    if args.position:
        my_result = fibonacci(digit=args.digits)
        print(' Fibonacci sequence value for {}'.format(args.digits))
        print(' {}'.format(my_result))
    else:
        my_sequence = calculate_sequence()

        print(' digit value')
        for k, v in my_sequence.items():
            print(' {:>5} {}'.format(k, v))

        my_graph = FibonacciGraph([ k for k in my_sequence.keys()],
                                  [v for v in my_sequence.values()]
                                  )
        my_graph.plot_fibonacci_sequence()
