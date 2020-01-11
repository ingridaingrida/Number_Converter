# -*- coding: utf-8 -*-

"""
Created on Sat Jan  4 19:27:34 2020

@author: ingrida grigonyte
"""


def get_message(msg):

    msgs = {
        'msg_1': 'Invalid input!',
        'msg_2': 'Please enter a number!',
        'msg_3': 'Please enter arabic or roman numbers only!',
        'msg_4': 'Number is too big for the arabic to roman number conversion!',
        'msg_5': 'Romans had no zero! No wonder they collapsed.',
        'msg_6': 'Invalid combination of roman numerals.',
        'msg_7': 'Roman number is: ',
        'msg_8': 'Arabic number is: ',
        'msg_10': 'Enter a number: ',
        }

    result = None
    for i in msgs:
        if i == msg:
            result = msgs.get(msg)
    return result
