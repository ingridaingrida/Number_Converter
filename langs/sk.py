# -*- coding: utf-8 -*-

"""
Created on Tue Jan  7 23:00:24 2020

@author: ingrida grigonyte
"""


def get_message(msg):

    msgs = {
        'msg_1': "Neplatný vstup!",
        'msg_2': "Zadajte číslo!",
        'msg_3': "Zadajte iba arabské alebo rímske čísla!",
        'msg_4': "Číslo je príliš veľké na konverziu arabských na rímske čísla!",
        'msg_5': "Rimania nemali nulu! Niet divu, že sa zrútili.",
        'msg_6': "Neplatná kombinácia rímskych číslic.",
        'msg_7': "Rímske číslo je:",
        'msg_8': "Arabské číslo je:",
        'msg_10': "Zadajte číslo: ",
        }

    result = None
    for i in msgs:
        if i == msg:
            result = msgs.get(msg)
    return result
