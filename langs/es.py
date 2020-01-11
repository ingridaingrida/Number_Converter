# -*- coding: utf-8 -*-

"""
Created on Tue Jan  7 23:02:48 2020

@author: ingrida grigonyte
"""


def get_message(msg):

    msgs = {
        'msg_1': "Entrada inválida",
        'msg_2': "¡Ingrese un número!",
        'msg_3': "Por favor, ingrese solo números arábigos o romanos",
        'msg_4': "¡El número es demasiado grande para la conversión de números arábigos a romanos!",
        'msg_5': "¡Los romanos no tenían cero! No es de extrañar que colapsaron",
        'msg_6': "Combinación inválida de números romanos",
        'msg_7': "El número romano es: ",
        'msg_8': "El número árabe es: ",
        'msg_10': "Ingrese un número: ",
        }

    result = None
    for i in msgs:
        if i == msg:
            result = msgs.get(msg)
    return result
