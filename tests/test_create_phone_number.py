#! /usr/bin/env python3

from src.create_phone_number import create_phone_number


def test_phone_number0():
    digits = [0] * 10
    result = create_phone_number(digits)
    expected = '(000) 000-0000'
    assert result == expected


def test_phone_number1():
    digits = [i for i in range(10)]
    result = create_phone_number(digits)
    expected = '(012) 345-6789'
    assert result == expected


if __name__ == '__main__':
    print('Module codewars/tests/test_create_phone_number.py')
