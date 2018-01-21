import argparse
import pyperclip


def add_bullet_points(lines):
    bullet_lines = []
    for line in lines:
        bullet_line = '* ' + line
        bullet_lines.append(bullet_line)
    return bullet_lines


def capitalize_first_word(lines):
    capital_lines = []
    for line in lines:
        capital_line = line.capitalize()
        capital_lines.append(capital_line)
    return capital_lines


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Playing with clipboard')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-b', dest='bulletize', action='store_true',
                       help='add bullet points to each line in the clipboard')
    group.add_argument('-c', dest='capitalize', action='store_true',
                       help='capitalize first word of each line of text in the clipboard')

    args = parser.parse_args()

    text = pyperclip.paste()
    lines = text.split('\n')

    if args.capitalize:
        final_lines = capitalize_first_word(lines)

    if args.bulletize:
        final_lines = add_bullet_points(lines)

    final_text = '\n'.join(final_lines)
    pyperclip.copy(final_text)
    print(final_text)
