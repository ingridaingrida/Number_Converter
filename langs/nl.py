# -*- coding: utf-8 -*-

"""
Created on Tue Jan  7 22:34:21 2020

@author: ingrida grigonyte
"""


def get_message(msg):

    msgs = {
        'msg_1': 'Ongeldige invoer!',
        'msg_2': 'Voer een nummer in!',
        'msg_3': 'Voer alleen Arabische of Romeinse cijfers in!',
        'msg_4': 'Nummer is te groot voor de Arabische naar Romeinse nummerconversie!',
        'msg_5': 'Romeinen hadden geen nul! Geen wonder dat ze instortten.',
        'msg_6': 'Ongeldige combinatie van Romeinse cijfers.',
        'msg_7': 'Roman nummer is: ',
        'msg_8': 'Arabisch nummer is: ',
        'msg_10': 'Voer een nummer in: ',
        }

    result = None
    for i in msgs:
        if i == msg:
            result = msgs.get(msg)
    return result
