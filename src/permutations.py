#! /usr/bin/env python3

def permutations(string):
    """Returns all permutations of the input string.
    E.g. permutations('abc') = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Args:
        string: Input string.

    Returns:
        List of possible permutations sorted by alphabetical order.
    """
    if len(string) == 1:
        return [string]
    else:
        patterns = []
        for i in range(len(string)):
            subset = permutations(string[:i] + string[i+1:])
            patterns.extend([string[i] + other_string for other_string in subset])
        return sorted(list(set(patterns)))


if __name__ == '__main__':
    print('Module codewars/src/permutations.py')
