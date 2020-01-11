# -*- coding: utf-8 -*-

"""
Created on Tue Jan  7 21:42:41 2020

@author: ingrida grigonyte
"""


def get_message(msg):

    msgs = {
        'msg_1': 'Vale sisestus!',
        'msg_2': 'Palun sisesta number!',
        'msg_3': 'Palun sisestage ainult araabia või rooma numbrid!',
        'msg_4': 'Number on Araabia-Rooma numbrite teisendamiseks liiga suur!',
        'msg_5': 'roomlastel polnud nulli! Pole ime, et nad kokku kukkusid.',
        'msg_6': 'Rooma numbrite sobimatu kombinatsioon.',
        'msg_7': 'Rooma number on: ',
        'msg_8': 'Araabia number on: ',
        'msg_10': 'Sisestage number: ',
        }

    result = None
    for i in msgs:
        if i == msg:
            result = msgs.get(msg)
    return result
