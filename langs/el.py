# -*- coding: utf-8 -*-

"""
Created on Tue Jan  7 22:10:03 2020

@author: ingrida grigonyte
"""


def get_message(msg):

    msgs = {
        'msg_1': 'Μη έγκυρη είσοδος!',
        'msg_2': 'Παρακαλώ εισάγετε έναν αριθμό!',
        'msg_3': 'Παρακαλώ εισάγετε μόνο αραβικούς ή ρωμαϊκούς αριθμούς!',
        'msg_4': 'Ο αριθμός είναι πολύ μεγάλος για τη μετατροπή του αραβικού σε ρωμαϊκού αριθμού!',
        'msg_5': 'Οι Ρωμαίοι δεν είχαν μηδέν! Δεν είναι περίεργο ότι κατέρρευσαν. ',
        'msg_6': 'Μη έγκυρος συνδυασμός λατινικών αριθμών',
        'msg_7': 'Ρωμαϊκός αριθμός είναι: ',
        'msg_8': 'Αραβικός αριθμός είναι: ',
        'msg_10': 'Πληκτρολογήστε έναν αριθμό: ',
        }

    result = None
    for i in msgs:
        if i == msg:
            result = msgs.get(msg)
    return result