# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 22:05:23 2020

@author: inggr
"""

def get_message(msg):
    
    msgs = {
     'msg_1': "Entrée non valide!",
     'msg_2': "Veuillez saisir un nombre!",
     'msg_3': "Veuillez saisir uniquement des chiffres arabes ou romains!",
     'msg_4': "Le nombre est trop grand pour la conversion du nombre arabe en nombre romain!",
     'msg_5': "Les Romains n'avaient pas de zéro! Pas étonnant qu''ils se soient effondrés.",
     'msg_6': "Combinaison invalide de chiffres romains.",
     'msg_7': "Le nombre romain est: ",
     'msg_8': "Le nombre arabe est: ",
     # 'msg_9': 'Choisissez la langue:',
     'msg_10': "Entrez un nombre: "
    }
  
    result = None
    for i in msgs:
        if i == msg:         
            result = msgs.get(msg)
    return result