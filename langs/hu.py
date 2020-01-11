# -*- coding: utf-8 -*-

"""
Created on Tue Jan  7 22:12:07 2020

@author: ingrida grigonyte
"""


def get_message(msg):

    msgs = {
        'msg_1': 'Érvénytelen bemenet!',
        'msg_2': 'Kérem, írjon be egy számot!',
        'msg_3': 'Kérjük, csak arab vagy római számot írjon be!',
        'msg_4': 'Túl nagy a szám az arab-római szám konvertálásához!',
        'msg_5': 'A rómaiaknak nulla nem volt! Nem csoda, hogy összeomlottak.',
        'msg_6': 'A római számok érvénytelen kombinációja.',
        'msg_7': 'A római szám: ',
        'msg_8': 'Az arab szám: ',
        'msg_10': 'Írjon be egy számot: ',
        }

    result = None
    for i in msgs:
        if i == msg:
            result = msgs.get(msg)
    return result
