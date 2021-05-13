#! /usr/bin/env python3

def create_phone_number(digits):
    """Converts a list of digits into a string formatted as a phone number.

    Args:
        digits (list): List of digits.

    Returns:
        phone_number (str): String formatted as "(XXX) YYY-ZZZZ".
    """
    digits = [str(digit) for digit in digits]
    first_bit = ''.join(digits[:3])
    second_bit = ''.join(digits[3:6])
    third_bit = ''.join(digits[6:10])
    phone_number = f'({first_bit}) {second_bit}-{third_bit}'
    return phone_number

# best solution
# def create_phone_number(n):
#     return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)


if __name__ == '__main__':
    print('Module codewars/src/create_phone_number.py')
