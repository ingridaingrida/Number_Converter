# -*- coding: utf-8 -*-

"""
Created on Tue Jan  7 21:50:05 2020

@author: ingrida grigonyte
"""


def get_message(msg):

    msgs = {
        'msg_1': 'Nevažeći ulaz!',
        'msg_2': 'Molim, unesite broj!',
        'msg_3': 'Molimo, unesite samo arapske ili rimske brojeve!',
        'msg_4': 'Broj je prevelik za pretvorbu arapskog u rimski broj!',
        'msg_5': 'Rimljani nisu imali nulu! Nije ni čudo što su se srušile.',
        'msg_6': 'Nevažeća kombinacija rimskih brojeva.',
        'msg_7': 'Rimski broj je: ',
        'msg_8': 'Arapski broj je: ',
        'msg_10': 'Unesite broj: ',
        }

    result = None
    for i in msgs:
        if i == msg:
            result = msgs.get(msg)
    return result
