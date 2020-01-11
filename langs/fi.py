# -*- coding: utf-8 -*-

"""
Created on Tue Jan  7 21:54:31 2020

@author: ingrida grigonyte
"""


def get_message(msg):

    msgs = {
        'msg_1': 'Virheellinen syöttö!',
        'msg_2': 'Anna numero!',
        'msg_3': 'Anna vain arabialaiset tai roomalaiset numerot!',
        'msg_4': 'Numero on liian suuri arabia-rooma-luvun muuntamiseen!',
        'msg_5': 'Roomalaisilla ei ollut nollaa! Ei ihme, että ne romahtivat.',
        'msg_6': 'Virheellinen roomalaisten numeroiden yhdistelmä.',
        'msg_7': 'Roomalainen numero on: ',
        'msg_8': 'Arabialainen numero on: ',
        'msg_10': 'Kirjoita numero: ',
        }

    result = None
    for i in msgs:
        if i == msg:
            result = msgs.get(msg)
    return result
