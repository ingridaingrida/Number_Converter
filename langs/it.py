# -*- coding: utf-8 -*-

"""
Created on Tue Jan  7 22:14:49 2020

@author: ingrida grigonyte
"""


def get_message(msg):

    msgs = {
        'msg_1': 'Input non valido!',
        'msg_2': 'Per favore, inserisci un numero!',
        'msg_3': 'Per favore, inserisci solo numeri arabi o romani!',
        'msg_4': "Il numero è troppo grande per la conversione numerica da arabo a romano!",
        'msg_5': "I romani non avevano zero! Non c'è da stupirsi che siano crollati.",
        'msg_6': 'Combinazione non valida di numeri romani.',
        'msg_7': "Il numero romano è: ",
        'msg_8': "Il numero arabo è: ",
        'msg_10': 'Inserisci un numero: ',
        }

    result = None
    for i in msgs:
        if i == msg:
            result = msgs.get(msg)
    return result
