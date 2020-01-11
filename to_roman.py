#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Created on Fri Dec 27 21:27:45 2019

@author: inggr
"""


def arabic_to_roman(text_to_convert):
    roman_list = []

    rom_numb = {
        0: '',
        1: 'I',
        2: 'II',
        3: 'III',
        4: 'IV',
        5: 'V',
        6: 'VI',
        7: 'VII',
        8: 'VIII',
        9: 'IX',
        10: 'X',
        20: 'XX',
        30: 'XXX',
        40: 'XL',
        50: 'L',
        60: 'LX',
        70: 'LXX',
        80: 'LXXX',
        90: 'XC',
        100: 'C',
        200: 'CC',
        300: 'CCC',
        400: 'CD',
        500: 'D',
        600: 'DC',
        700: 'DCC',
        800: 'DCCC',
        900: 'CM',
        1000: 'M',
        2000: 'MM',
        3000: 'MMM',
        }

    text_list = list(text_to_convert)
    digit_list = [int(i) for i in text_list]
    for i in range(len(digit_list)):
        digit_list[i] *= 10 ** (len(digit_list) - i - 1)
        roman_list.append(rom_numb[digit_list[i]])

    converted_to_ro = ''.join(roman_list)

    return converted_to_ro
