import argparse
import time

from fibonacci_graph import FibonacciGraph


def time_performance_test(input_func):
    def timed_func(*args, **kwargs):
        start_time = time.time()
        input_func_result = input_func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print('Execution Time: {}'.format(execution_time))
        return input_func_result
    return timed_func


def fibonacci(digit):
    if digit < 2:
        return digit
    else:
        sequence_value = fibonacci(digit - 1) + fibonacci(digit - 2)
        return sequence_value


@time_performance_test
def calculate_sequence(digits):
    i = 0
    sequence = {}
    while i <= digits:
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
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-p', '--position', action='store_true',
                       help='Calculate only single position in sequence')
    group.add_argument('-g', '--graph', action='store_true',
                       help='Print a graph of the Fibonacci sequence')
    arguments = parser.parse_args()
    return arguments


if __name__ == '__main__':
    my_args = get_arguments()

    check_positive_int(my_args.digits)

    if my_args.position:
        my_result = fibonacci(digit=my_args.digits)
        print(' Fibonacci sequence value for {}'.format(my_args.digits))
        print(' {}'.format(my_result))
    else:
        my_sequence = calculate_sequence(my_args.digits)

        print(' digit value')
        for k, v in my_sequence.items():
            print(' {:>5} {}'.format(k, v))

        if my_args.graph:
            my_graph = FibonacciGraph([k for k in my_sequence.keys()],
                                      [v for v in my_sequence.values()]
                                      )
            my_graph.plot_fibonacci_sequence()
