# -*- coding: utf-8 -*-

"""
Created on Tue Jan  7 23:09:43 2020

@author: ingrida grigonyte
"""


def get_message(msg):

    msgs = {
        'msg_1': "Input ħażin!",
        'msg_2': "Jekk jogħġbok, daħħal numru!",
        'msg_3': "Jekk jogħġbok, daħħal numri Għarab jew Rumani biss!",
        'msg_4': "Numru huwa kbir wisq għall-konverżjoni Għarbija għal Rumana!",
        'msg_5': "Ir-Rumani ma kellhom l-ebda żero! Mhux ta 'b'xejn li waqgħu.",
        'msg_6': "Taħlita invalida ta 'numri Rumani.",
        'msg_7': 'In-numru Ruman huwa: ',
        'msg_8': "In-numru Għarbi huwa: ",
        'msg_10': "Daħħal numru: ",
        }

    result = None
    for i in msgs:
        if i == msg:
            result = msgs.get(msg)
    return result
