# -*- coding: utf-8 -*-

"""
Created on Tue Jan  7 22:55:57 2020

@author: ingrida grigonyte
"""


def get_message(msg):

    msgs = {
        'msg_1': "Nieprawidłowe wejście!",
        'msg_2': "Proszę wprowadzić liczbę!",
        'msg_3': "Wprowadź tylko cyfry arabskie lub rzymskie!",
        'msg_4': "Liczba jest za duża do konwersji cyfr arabskich na rzymskie!",
        'msg_5': "Rzymianie nie mieli zera! Nic dziwnego, że upadli.",
        'msg_6': 'Niepoprawna kombinacja cyfr rzymskich.',
        'msg_7': 'Liczba rzymska to: ',
        'msg_8': 'Arabski numer to: ',
        'msg_10': "Wprowadź liczbę: ",
        }

    result = None
    for i in msgs:
        if i == msg:
            result = msgs.get(msg)
    return result
