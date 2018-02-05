import argparse
import collections
import fileinput


def count_words():
    counted_words = 0
    with open(args.myfile) as myfile:
        for line in myfile:
            counted_words += len(line.split())
    return counted_words


def count_most_frequent(lines, top):
    words = collections.Counter()
    for line in lines:
        words.update(line.lower().split())
    return words.most_common(top)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Words Counter')
    parser.add_argument('myfile', metavar='F',
                        help='it will count words in this file')

    args = parser.parse_args()

    my_counted_words = count_words()
    print('Total words in file: ', my_counted_words)

    with fileinput.input(files=args.myfile) as my_input:
        most_frequent_words = count_most_frequent(my_input, 10)
    print('Most frequent words in file:')
    for i, k in most_frequent_words:
        print('{:>10} {:>3}'.format(i, k))
