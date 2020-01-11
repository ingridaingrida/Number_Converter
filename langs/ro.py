# -*- coding: utf-8 -*-

"""
Created on Tue Jan  7 22:59:00 2020

@author: ingrida grigonyte
"""


def get_message(msg):

    msgs = {
        'msg_1': "Intrare nevalidă!",
        'msg_2': "Vă rugăm, introduceți un număr!",
        'msg_3': "Vă rugăm, introduceți doar numere arabe sau romane!",
        'msg_4': "Numărul este prea mare pentru conversia numerelor arab în roman!",
        'msg_5': "Romanii nu aveau zero! Nu este de mirare că s-au prăbușit.",
        'msg_6': "Combinație nevalidă de cifre romane.",
        'msg_7': "Numărul roman este: ",
        'msg_8': "Numărul arab este: ",
        'msg_10': "Introduceți un număr: ",
        }

    result = None
    for i in msgs:
        if i == msg:
            result = msgs.get(msg)
    return result
