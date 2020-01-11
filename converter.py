# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 22:43:14 2019

@author: ingrida grigonyte
"""
import checker
import to_roman
import to_arabic
import transl


def convert_num(text, lang):

    msg_1 = transl.translate_msg(lang, 'msg_1')
    msg_2 = transl.translate_msg(lang, 'msg_2')
    msg_3 = transl.translate_msg(lang, 'msg_3')
    msg_4 = transl.translate_msg(lang, 'msg_4')
    msg_5 = transl.translate_msg(lang, 'msg_5')
    msg_6 = transl.translate_msg(lang, 'msg_6')
    msg_7 = transl.translate_msg(lang, 'msg_7')
    msg_8 = transl.translate_msg(lang, 'msg_8')

    if text == '':
        print(msg_2)
        return msg_2

    if checker.check_input(text) is True:
        kind = checker.check_kind(text)
        if kind == 'arabic':
            if int(text) > 3999:
                print(msg_4)
            elif int(text) == 0:
                print(msg_5)
            else:
                converted_text = to_roman.arabic_to_roman(text)
                print(msg_7 + converted_text)
        elif kind == 'roman':
            converted_text = to_arabic.roman_to_arabic(text)
            if converted_text == 'Invalid combination':
                print(msg_6)
            else:
                print(msg_8 + converted_text)
        else:
            print(msg_3)
    else:
        print(msg_1)
        