#! /usr/bin/env python3


def pick_peaks(array):
    """Finds the local peaks within the given array.

    Args:
        array (list): List to find its peaks.

    Returns:
        Dictionary containing the positions and the values of the peaks,
        i.e. {pos: [3, 7], peaks: [6, 3].
    """
    peaks = {'pos': [], 'peaks': []}
    for i, n in enumerate(array):
        if i == 0 or i == len(array)-1:
            # edge values cannot be a peak
            continue

        n_is_peak = False
        left_value = array[i-1]
        right_value = array[i+1]
        if n <= left_value:
            # n is not a peak
            continue

        if n < right_value:
            # n is not a peak
            continue
        elif n > right_value:
            # n is a peak
            n_is_peak = True
        else:
            # n can be a peak, scan the remaining right hand values
            for value in array[i+2:]:
                if value == n:
                    # keep scanning
                    continue
                elif value > n:
                    # n is not a peak
                    n_is_peak = False
                    break
                else:
                    # n is a peak
                    n_is_peak = True
                    break

        if n_is_peak:
            peaks['pos'].append(i)
            peaks['peaks'].append(n)
    return peaks

# smart solution
# def pick_peaks(arr):
#     pos = []
#     prob_peak = False
#     for i in range(1, len(arr)):
#         if arr[i] > arr[i-1]:
#             prob_peak = i
#         elif arr[i] < arr[i-1] and prob_peak:
#             pos.append(prob_peak)
#             prob_peak = False
#     return {'pos': pos, 'peaks': [arr[i] for i in pos]}


if __name__ == '__main__':
    # print(pick_peaks([1,2,3,6,4,5,2,3,2,1]))
    print(pick_peaks([2,1,3,1,2,2,2,2])) # {"pos": [2], "peaks": [3]}
    print('Module codewars/src/pick_peaks.py')
