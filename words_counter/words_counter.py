import argparse
import collections
import fileinput


def count_words(text_file):
    counted_words = 0
    with open(text_file) as text_file:
        for line in text_file:
            counted_words += len(line.split())
    return counted_words


def count_most_frequent_words(lines, top):
    words = collections.Counter()
    for line in lines:
        words.update(line.lower().split())
    return words.most_common(top)


def print_words_file_info(counted_words, most_frequent_words):
    print('Total words in file: ', counted_words)
    print('Most frequent words in file:')
    for i, k in most_frequent_words:
        print('{:>10} {:>3}'.format(i, k))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Words Counter')
    parser.add_argument('text_file',
                        help='it will count words in this file')

    args = parser.parse_args()

    my_counted_words = count_words(args.text_file)

    with fileinput.input(files=args.text_file) as my_input:
        my_most_frequent_words = count_most_frequent_words(my_input, 10)

    print_words_file_info(my_counted_words, my_most_frequent_words)
