# -*- coding: utf-8 -*-

"""
Created on Tue Jan  7 22:13:37 2020

@author: ingrida grigonyte
"""


def get_message(msg):

    msgs = {
        'msg_1': 'Ionchur neamhbhailí!',
        'msg_2': 'Tabhair uimhir, le do thoil!',
        'msg_3': 'Cuir uimhreacha Araibeacha nó Rómánacha isteach le do thoil!',
        'msg_4': 'Tá an líon ró-mhór do na araibigh chun tiontú uimhreach Rómhánach a dhéanamh!',
        'msg_5': 'Ní raibh aon náid ag na Rómhánaigh! Ní haon ionadh gur thit siad.',
        'msg_6': 'Meascán neamhbhailí d’ uimhreacha Rómhánacha.',
        'msg_7': 'Is é an uimhir Rómhánach: ',
        'msg_8': 'Is é uimhir Araibis: ',
        'msg_10': 'Cuir uimhir isteach: ',
        }

    result = None
    for i in msgs:
        if i == msg:
            result = msgs.get(msg)
    return result
