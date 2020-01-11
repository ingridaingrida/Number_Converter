# -*- coding: utf-8 -*-

"""
Created on Tue Jan  7 21:33:32 2020

@author: ingrida grigonyte
"""


def get_message(msg):

    msgs = {
        'msg_1': 'Neplatný vstup!',
        'msg_2': 'Zadejte prosím číslo!',
        'msg_3': 'Zadejte pouze arabská nebo římská čísla!',
        'msg_4': 'Číslo je příliš velké na převod arabského na římské číslo!!',
        'msg_5': 'Římané neměli nulu! Není divu, že se zhroutili.',
        'msg_6': 'Neplatná kombinace římských číslic.',
        'msg_7': 'Římské číslo je: ',
        'msg_8': 'Arabské číslo je: ',
        'msg_10': 'Zadejte číslo: ',
        }

    result = None
    for i in msgs:
        if i == msg:
            result = msgs.get(msg)
    return result
