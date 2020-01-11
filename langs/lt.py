# -*- coding: utf-8 -*-

"""
Created on Mon Jan  6 20:48:06 2020

@author: ingrida grigonyte
"""


def get_message(msg):

    msgs = {
        'msg_1': 'Neteisinga įvestis!',
        'msg_2': 'Įveskite skaičių!',
        'msg_3': 'Įveskite tik arabiškus arba romėniškus skaičius!',
        'msg_4': 'Skaičius per didelis konvertuoti į romėnišką!',
        'msg_5': 'Romėnai neturėjo nulio. Nenuostabu, jog žlugo.',
        'msg_6': 'Bloga romėniškų skaitmenų tvarka.',
        'msg_7': 'Romėniškas skaičius yra: ',
        'msg_8': 'Arabiškas skaičius yra: ',
        'msg_10': 'Įveskite skaičių: ',
        }

    result = None
    for i in msgs:
        if i == msg:
            result = msgs.get(msg)
    return result
