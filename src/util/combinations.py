# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 20:24:18 2016

@author: Parag
"""

NUM_REP = {10: 'a',
           11: 'b',
           12: 'c',
           13: 'd',
           14: 'e',
           15: 'f',
           16: 'g',
           17: 'h',
           18: 'i',
           19: 'j',
           20: 'k',
           21: 'l',
           22: 'm',
           23: 'n',
           24: 'o',
           25: 'p',
           26: 'q',
           27: 'r',
           28: 's',
           29: 't',
           30: 'u',
           31: 'v',
           32: 'w',
           33: 'x',
           34: 'y',
           35: 'z'}


def base10toN(num, n, output_length):
    """Change the decimal num to resp. base-n number.
    Up to base-36 is supported without special notation."""
    new_num_string = ''
    current = num
    while current != 0:
        remainder = current % n
        if 36 > remainder > 9:
            remainder_string = NUM_REP[remainder]
        elif remainder >= 36:
            remainder_string = '('+str(remainder)+')'
        else:
            remainder_string = str(remainder)
        new_num_string = remainder_string + new_num_string
        current = current / n
    return '0'*(output_length-len(new_num_string)) + new_num_string


def decodeIndex(s):
    if s in NUM_REP.values():
        return [k for k in NUM_REP if NUM_REP[k] == s][0]
    return int(s)
