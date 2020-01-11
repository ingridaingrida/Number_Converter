# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 21:30:18 2019

@author: ingrida grigonyte
"""
import converter
import lang
import transl


def run():
    ln = lang.get_language()
    msg = transl.translate_msg(ln, 'msg_10')
    number = input(msg)
    text = str(number).upper().strip().replace(' ', '')

    converter.convert_num(text, ln)
