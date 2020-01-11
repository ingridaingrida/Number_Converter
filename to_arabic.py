#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Created on Fri Dec 27 21:28:56 2019

@author: ingrida grigonyte
"""

sequential_m = 0
sequential_d = 0
sequential_c = 0
sequential_l = 0
sequential_x = 0
sequential_v = 0
sequential_i = 0
flag_cmd = 0
flag_xcl = 0
flag_ixv = 0
error_flag = 0
message = 'Invalid combination'
arabic_num = 0
flag = 0
i = 0


def process_m():
    global arabic_num
    global sequential_m
    global error_flag

    if arabic_num % 1000 != 0:
        error_flag = 1
    arabic_num += 1000
    sequential_m += 1
    if sequential_m > 3:
        error_flag = 1


def process_d():
    global arabic_num
    global error_flag

    if arabic_num % 1000 != 0:
        error_flag = 1
    arabic_num += 500


def process_c1(nextsym):
    global arabic_num
    global error_flag
    global flag_cmd

    if arabic_num % 100 != 0:
        error_flag = 1
    if nextsym == 'M':
        if arabic_num % 1000 != 0:
            error_flag = 1
        arabic_num += 900
        flag_cmd += 1
        if flag_cmd > 1:
            error_flag = 1
    elif nextsym == 'D':
        if arabic_num % 1000 != 0:
            error_flag = 1
        arabic_num += 400
        flag_cmd += 1
        if flag_cmd > 1:
            error_flag = 1


def process_c2():
    global arabic_num
    global error_flag
    global sequential_c

    if arabic_num % 100 != 0:
        error_flag = 1
    arabic_num += 100
    sequential_c += 1
    if sequential_c > 3 or flag_cmd > 0:
        error_flag = 1


def process_l():
    global arabic_num
    global error_flag
    global sequential_l

    if arabic_num % 50 != 0:
        error_flag = 1
    arabic_num += 50
    sequential_l += 1
    if sequential_l > 1:
        error_flag = 1


def process_x1(nextsym):
    global arabic_num
    global error_flag
    global flag_xcl

    if arabic_num % 10 != 0:
        error_flag = 1
    if nextsym == 'C':
        if arabic_num % 100 != 0:
            error_flag = 1
        arabic_num += 90
        flag_xcl += 1
        if flag_xcl > 1:
            error_flag = 1
    elif nextsym == 'L':
        if arabic_num % 100 != 0:
            error_flag = 1
        arabic_num += 40
        flag_xcl += 1
        if flag_xcl > 1:
            error_flag = 1


def process_x2():
    global arabic_num
    global error_flag
    global sequential_x

    if arabic_num % 10 != 0:
        error_flag = 1
    arabic_num += 10
    sequential_x += 1
    if sequential_x > 3 or flag_xcl > 0:
        error_flag = 1


def process_v():
    global arabic_num
    global error_flag
    global sequential_v

    if arabic_num % 5 != 0:
        error_flag = 1
    arabic_num += 5
    sequential_v += 1
    if sequential_v > 1:
        error_flag = 1


def process_i1(nextsym):
    global arabic_num
    global error_flag
    global flag_ixv

    if nextsym == 'X':
        if arabic_num % 10 != 0:
            error_flag = 1
        arabic_num += 9
        flag_ixv += 1
        if flag_ixv > 1:
            error_flag = 1
    elif nextsym == 'V':
        if arabic_num % 10 != 0:
            error_flag = 1
        arabic_num += 4
        flag_ixv += 1
        if flag_ixv > 1:
            error_flag = 1


def process_i2():
    global arabic_num
    global error_flag
    global sequential_i

    arabic_num += 1
    sequential_i += 1
    if sequential_i > 3 or flag_ixv > 0:
        error_flag = 1


def roman_to_arabic(text_to_convert):
    global i
    global flag

    roman_num_list = list(text_to_convert)

    while i < len(roman_num_list):
        if roman_num_list[i] == 'M':
            process_m()
            if error_flag == 1:
                return message

        if roman_num_list[i] == 'D':
            process_d()
            if error_flag == 1:
                return message

        if roman_num_list[i] == 'C':
            nextsym = ''
            try:
                nextsym = roman_num_list[i + 1]
            except:
                nextsym = ''
            if nextsym == 'M' or nextsym == 'D':
                process_c1(nextsym)
                if error_flag == 1:
                    return message
                flag = 1
            else:
                process_c2()
                if error_flag == 1:
                    return message

        if roman_num_list[i] == 'L':
            process_l()
            if error_flag == 1:
                return message

        if roman_num_list[i] == 'X':
            nextsym = ''
            try:
                nextsym = roman_num_list[i + 1]
            except:
                nextsym = ''
            if nextsym == 'C' or nextsym == 'L':
                process_x1(nextsym)
                if error_flag == 1:
                    return message
                flag = 1
            else:
                process_x2()
                if error_flag == 1:
                    return message

        if roman_num_list[i] == 'V':
            process_v()
            if error_flag == 1:
                return message

        if roman_num_list[i] == 'I':
            nextsym = ''
            try:
                nextsym = roman_num_list[i + 1]
            except:
                nextsym = ''
            if nextsym == 'X' or nextsym == 'V':
                process_i1(nextsym)
                if error_flag == 1:
                    return message
                flag = 1
            else:
                process_i2()
                if error_flag == 1:
                    return message

        if flag > 0:
            i += 2
            flag = 0
        else:
            i += 1

    return str(arabic_num)
