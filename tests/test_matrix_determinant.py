#! /usr/bin/env python3

from src.matrix_determinant import determinant


def test0():
    matrix = [[1]]
    assert determinant(matrix) == 1


def test1():
    matrix = [[0, 1], [2, 3]]
    assert determinant(matrix) == -2


def test2():
    matrix = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    assert determinant(matrix) == 0


if __name__ == '__main__':
    print('Module codewars/tests/test_matrix_determinant.py')
