#! /usr/bin/env python3

from src.greed_is_good import score


def test_dice0():
    assert score([2, 3, 4, 6, 2]) == 0


def test_dice1():
    assert score([4, 4, 4, 3, 3]) == 400


def test_dice2():
    assert score([2, 4, 4, 5, 4]) == 450


if __name__ == '__main__':
    print('Module codewars/tests/test_greed_is_good.py')
