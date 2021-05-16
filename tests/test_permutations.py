#! /usr/bin/env python3

from src.permutations import permutations


def test0():
    assert permutations('a') == ['a']


def test1():
    assert permutations('ab') == ['ab', 'ba']


def test2():
    assert permutations('aabb') == ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']


if __name__ == '__main__':
    print('Module codewars/tests/test_permutations.py')
