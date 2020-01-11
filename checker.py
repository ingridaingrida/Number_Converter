#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Created on Fri Dec 27 21:25:04 2019

@author: inggr
"""


def check_input(text):

    allowed = [
        '0',
        '1',
        '2',
        '3',
        '4',
        '5',
        '6',
        '7',
        '8',
        '9',
        'I',
        'V',
        'X',
        'L',
        'C',
        'D',
        'M',
        ]
    text_list = list(text)

    for i in text_list:
        if i not in allowed:
            return False
    return True


def check_kind(text_to_check):
    arabic = [
        '0',
        '1',
        '2',
        '3',
        '4',
        '5',
        '6',
        '7',
        '8',
        '9',
        ]
    roman = [
        'I',
        'V',
        'X',
        'L',
        'C',
        'D',
        'M',
        ]

    if text_to_check[0] in arabic:
        for i in text_to_check:
            if i not in arabic:
                return False
            else:
                kind = 'arabic'
    elif text_to_check[0] in roman:
        for i in text_to_check:
            if i not in roman:
                return False
            else:
                kind = 'roman'
    return kind
