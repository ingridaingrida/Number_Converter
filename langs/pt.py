# -*- coding: utf-8 -*-

"""
Created on Tue Jan  7 22:58:06 2020

@author: ingrida grigonyte
"""


def get_message(msg):

    msgs = {
        'msg_1': "Entrada inválida!",
        'msg_2': "Por favor, digite um número!",
        'msg_3': "Digite apenas números arábicos ou romanos!",
        'msg_4': "O número é muito grande para a conversão de números arábico para romano!",
        'msg_5': "Os romanos não tinham zero! Não admira que tenham desmoronado.",
        'msg_6': "Combinação inválida de algarismos romanos.",
        'msg_7': "O número romano é: ",
        'msg_8': "O número em árabe é: ",
        'msg_10': "Digite um número: ",
        }

    result = None
    for i in msgs:
        if i == msg:
            result = msgs.get(msg)
    return result
