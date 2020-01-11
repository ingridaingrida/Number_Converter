# -*- coding: utf-8 -*-

"""
Created on Tue Jan  7 21:51:00 2020

@author: ingrida grigonyte
"""


def get_message(msg):

    msgs = {
        'msg_1': 'Ugyldig input!',
        'msg_2': 'Venligst indtast et nummer!',
        'msg_3': 'Venligst indtast kun arabiske eller romerske tal!',
        'msg_4': 'Antallet er for stort til konvertering af arabisk til romersk tal!',
        'msg_5': 'Romerne havde ingen nul! Ikke underligt, at de kollapsede. ',
        'msg_6': 'Ugyldig kombination af romertal.',
        'msg_7': 'Romertal er: ',
        'msg_8': 'Arabisk nummer er: ',
        'msg_10': 'Indtast et nummer: ',
        }

    result = None
    for i in msgs:
        if i == msg:
            result = msgs.get(msg)
    return result
