
def print_dict(any_dict):
    for k, v in any_dict.items():
        print(k, v)
    return True


def print_dict_ordered_by_keys(any_dict):
    sorted_any_dict_by_keys = sorted(any_dict.keys())
    for k in sorted_any_dict_by_keys:
        print(k, any_dict[k])
    return True


def print_dict_ordered_by_values(any_dict):
    sorted_any_dict_by_values = [(k, any_dict[k]) for k in sorted(any_dict, key=any_dict.get)]
    for k, v in sorted_any_dict_by_values:
        print(v, k)
    return True


if __name__ == '__main__':
    my_dict = {'two': 2,
               'one': 1,
               'three': 3,
               'four': 4}

    print('My Dictionary')
    print_dict(my_dict)
    print('My Dictionary ordered by keys')
    print_dict_ordered_by_keys(my_dict)
    print('My Dictionary ordered by values')
    print_dict_ordered_by_values(my_dict)
