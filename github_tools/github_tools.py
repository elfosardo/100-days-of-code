import argparse
import getpass

from github import Github


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Github tools')
    parser.add_argument('username', metavar='U',
                        help='your github username')
    args = parser.parse_args()

    user = args.username
    password = getpass.getpass('Github Password: ')

    g = Github(user, password)
    for repo in g.get_user().get_repos():
        name = repo.name
        stars = repo.stargazers_count
        watchers = repo.watchers_count
        print('{:<25} {} {}'.format(name, stars, watchers))
