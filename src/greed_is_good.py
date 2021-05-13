#! /usr/bin/env python3

from collections import Counter


def score(dice):
    """Calculates the score from the input dice.
    The score is calculated according to the following table:
        Three 1's => 1000 points
        Three 6's =>  600 points
        Three 5's =>  500 points
        Three 4's =>  400 points
        Three 3's =>  300 points
        Three 2's =>  200 points
        One   1   =>  100 points
        One   5   =>   50 point
    E.g.
        score([2, 3, 4, 6, 2]) = 0
        score([4, 4, 4, 3, 3]) = 400
        score([2, 4, 4, 5, 4]) = 450

    Args:
        dice (list): List of die numbers.

    Returns:
        score (int): The calculated score.
    """
    score_counts = Counter(dice)
    result = 0
    # Three 1's => 1000 points
    if score_counts[1] >= 3:
        result += 1000
        score_counts[1] -= 3
    # Three 6's =>  600 points
    elif score_counts[6] >= 3:
        result += 600
        score_counts[6] -= 3
    # Three 5's =>  500 points
    elif score_counts[5] >= 3:
        result += 500
        score_counts[5] -= 3
    # Three 4's =>  400 points
    elif score_counts[4] >= 3:
        result += 400
        score_counts[4] -= 3
    # Three 3's =>  300 points
    elif score_counts[3] >= 3:
        result += 300
        score_counts[3] -= 3
    # Three 2's =>  200 points
    elif score_counts[2] >= 3:
        result += 200
        score_counts[2] -= 3

    # One 1 = > 100 points
    if score_counts[1]:
        result += 100 * score_counts[1]
    # One 5 = > 50 points
    if score_counts[5]:
        result += 50 * score_counts[5]
    return result


if __name__ == '__main__':
    print('Module codewars/src/greed_is_good.py')
