import argparse
from die import Die

if __name__ == '__main__':
    parser = argparse.ArgumentParser('Simple Dice Roller')
    parser.add_argument('--number_of_dice', '-n', dest='num_dice', type=int, default=1,
                        help='Number of dice to roll; default 1')
    parser.add_argument('--sides', '-s', dest='sides', type=int, default=6,
                        help='Sides of the die; default 6')
    args = parser.parse_args()

    print('Rolling {}d{}'.format(args.num_dice, args.sides))

    results = []

    for n in range(args.num_dice):
        my_die = Die(args.sides)
        result = my_die.roll()
        results.append(result)

    for result in results:
        print('Rolled: {}'.format(result))

    total = sum(results)

    print('Sum: {}'.format(total))
