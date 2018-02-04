import argparse


def count_words():
    counted_words = 0
    with open(args.myfile) as myfile:
        for line in myfile:
            counted_words += len(line.split())

    return counted_words


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Words Counter')
    parser.add_argument('myfile', metavar='F',
                        help='it will count words in this file')

    args = parser.parse_args()

    counted_words = count_words()

    print(counted_words)