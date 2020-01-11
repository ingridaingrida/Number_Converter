# -*- coding: utf-8 -*-

"""
Created on Tue Jan  7 23:05:15 2020

@author: ingrida grigonyte
"""


def get_message(msg):

    msgs = {
        'msg_1': 'Ogiltig inmatning!',
        'msg_2': "Snälla, ange ett nummer!",
        'msg_3': "Snälla, ange bara arabiska eller romerska siffror!",
        'msg_4': "Antalet är för stort för arabiska till romerska talkonvertering!",
        'msg_5': "Romarna hade ingen noll! Inte undra på att de kollapsade.",
        'msg_6': 'Ogiltig kombination av romerska siffror.',
        'msg_7': "Romerskt tal är: ",
        'msg_8': "Arabiskt nummer är: ",
        'msg_10': 'Ange ett nummer: ',
        }

    result = None
    for i in msgs:
        if i == msg:
            result = msgs.get(msg)
    return result
