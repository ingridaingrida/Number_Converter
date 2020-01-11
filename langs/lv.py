# -*- coding: utf-8 -*-

"""
Created on Tue Jan  7 22:27:32 2020

@author: ingrida grigonyte
"""


def get_message(msg):

    msgs = {
        'msg_1': "Nederīga ievade!",
        'msg_2': "Lūdzu, ievadiet numuru!",
        'msg_3': "Lūdzu, ievadiet tikai arābu vai romiešu ciparus!",
        'msg_4': "Skaitlis ir pārāk liels, lai pārveidotu numuru arābu - romiešu!",
        'msg_5': "Romiešiem nebija nulles! Nav brīnums, ka viņi sabruka. ",
        'msg_6': "Nederīga romiešu ciparu kombinācija.",
        'msg_7': "Romiešu numurs ir: ",
        'msg_8': "Arābu numurs ir: ",
        'msg_10': 'Ievadiet numuru: ',
        }

    result = None
    for i in msgs:
        if i == msg:
            result = msgs.get(msg)
    return result
