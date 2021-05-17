#! /usr/bin/env python3

import numpy as np


def determinant(matrix):
    """Calculates the determinant of the given N*N matrix.

    Args:
        matrix (list): N*N matrix. (N >= 1)

    Returns:
        Determinant (float)
    """
    matrix = np.array(matrix)
    if matrix.shape == (1, 1):
        return matrix[0]
    elif matrix.shape == (2, 2):
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        det_value = 0
        for i in range(matrix.shape[0]):
            subset_matrix = np.delete(matrix, 0, axis=0)
            subset_matrix = np.delete(subset_matrix, i, axis=1)
            det_value += (-1) ** i * matrix[0][i] * determinant(subset_matrix)
        return det_value

# clever
# def determinant(m):
#     a = 0
#     if len(m) == 1:
#         a = m[0][0]
#     else:
#         for n in xrange(len(m)):
#             if (n + 1) % 2 == 0:
#                 a -= m[0][n] * determinant([o[:n] + o[n + 1:] for o in m[1:]])
#             else:
#                 a += m[0][n] * determinant([o[:n] + o[n + 1:] for o in m[1:]])
#
#     return a


if __name__ == '__main__':
    print('Module codewars/src/matrix_determinant.py')
