import argparse
import re

from morsecode import morse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Translate words in morse code')
    parser.add_argument('my_word', metavar='word', type=str,
                        help='word to translate to morse code')
    args = parser.parse_args()

    my_word = args.my_word

    print('You typed: {}'.format(my_word))
    my_word = ' '.join(my_word)
    pattern = re.compile(r"[A-Z0-9]")
    for letter in my_word:
        if pattern.match(letter.upper()):
            my_word = my_word.replace(letter, morse[letter.upper()])

    print('Morse code: {}'.format(my_word))
