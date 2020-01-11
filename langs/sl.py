# -*- coding: utf-8 -*-

"""
Created on Tue Jan  7 23:01:39 2020

@author: ingrida grigonyte
"""


def get_message(msg):

    msgs = {
        'msg_1': 'Neveljaven vnos!',
        'msg_2': "Prosim, vnesite številko!",
        'msg_3': "Prosimo, vnesite samo arabske ali rimske številke!",
        'msg_4': "Številka je prevelika za pretvorbo številk med arabsko in rimsko!",
        'msg_5': "Rimljani niso imeli ničle! Ni čudno, da so propadli.",
        'msg_6': "Neveljavna kombinacija rimskih številk.",
        'msg_7': "Rimska številka je: ",
        'msg_8': "Arabska številka je: ",
        'msg_10': "Vnesite številko: ",
        }

    result = None
    for i in msgs:
        if i == msg:
            result = msgs.get(msg)
    return result
