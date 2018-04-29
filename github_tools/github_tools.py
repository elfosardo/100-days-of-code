import argparse
import getpass

from github import Github


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Github tools')
    parser.add_argument('username',
                        help='your github username')
    args = parser.parse_args()

    user = args.username
    password = getpass.getpass('Github Password: ')

    g = Github(user, password)
    print('{:<25} {:<6} {}'.format('Name', 'Stars', 'Watchers'))
    for repo in g.get_user().get_repos():
        name = repo.name
        stars = repo.stargazers_count
        watchers = repo.watchers_count
        print('{:<25} {:<6} {}'.format(name, stars, watchers))
