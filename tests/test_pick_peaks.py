#! /usr/bin/env python3

from src.pick_peaks import pick_peaks


def test0():
    assert pick_peaks([2, 1, 4, 3]) == {'pos': [2], 'peaks': [4]}


def test1():
    assert pick_peaks([]) == {'pos': [], 'peaks': []}


def test2():
    assert pick_peaks([1, 2, 2, 3, 3, 3, 2]) == {'pos': [3], 'peaks': [3]}


def test4():
    assert pick_peaks([1, 2, 6, 4, 2, 1, 3, 1]) == {'pos': [2, 6], 'peaks': [6, 3]}


def test5():
    assert pick_peaks([1, 2, 6, 4, 5, 1, 3, 1]) == {'pos': [2, 4, 6], 'peaks': [6, 5, 3]}


if __name__ == '__main__':
    print('Module codewars/tests/test_pick_peaks.py')
