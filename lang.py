#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Created on Fri Jan  3 21:02:50 2020

@author: ingrida grigonyte
"""


def get_language():

    langs = [
        'en',
        'bg',
        'cz',
        'da',
        'de',
        'el',
        'es',
        'et',
        'fi',
        'fr',
        'ga',
        'hr',
        'hu',
        'it',
        'lt',
        'lv',
        'mt',
        'nl',
        'pl',
        'pt',
        'ro',
        'sk',
        'sl',
        'sv',
        ]

    while True:
        inp = input('Choose language: ')
        lang = str(inp).lower().strip().replace(' ', '')

        if lang not in langs:
            print ('This language is not supported')
        else:
            print ('Thank you, chosen language is: ', lang)
            break
    return lang
