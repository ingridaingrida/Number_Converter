# -*- coding: utf-8 -*-

"""
Created on Tue Jan  7 22:08:57 2020

@author: ingrida grigonyte
"""


def get_message(msg):

    msgs = {
        'msg_1': 'Ungültige Eingabe!',
        'msg_2': 'Bitte geben Sie eine Zahl ein!',
        'msg_3': 'Bitte geben Sie nur arabische oder römische Zahlen ein!',
        'msg_4': 'Die Zahl ist zu groß für die Umrechnung von arabischen in römische Zahlen!',
        'msg_5': 'Römer hatten keine Null! Kein Wunder, dass sie zusammengebrochen sind. ',
        'msg_6': 'Ungültige Kombination von römischen Ziffern.',
        'msg_7': 'Römische Zahl ist: ',
        'msg_8': 'Arabische Nummer ist: ',
        'msg_10': 'Geben Sie eine Nummer ein: ',
        }

    result = None
    for i in msgs:
        if i == msg:
            result = msgs.get(msg)
    return result
