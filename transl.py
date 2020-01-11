# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 22:08:09 2020

@author: ingrida grigonyte
"""
from langs import en, bg, cz, da, de, el, es, et, fi, fr, ga, hr, hu, it, lt, lv, mt, nl, pl, pt, ro, sk, sl, sv


def translate_msg(lang, msg):

    if lang == 'en':
        message = en.get_message(msg)

    if lang == 'bg':
        message = bg.get_message(msg)

    if lang == 'cz':
        message = cz.get_message(msg)

    if lang == 'da':
        message = da.get_message(msg)

    if lang == 'de':
        message = de.get_message(msg)

    if lang == 'el':
        message = el.get_message(msg)

    if lang == 'es':
        message = es.get_message(msg)

    if lang == 'et':
        message = et.get_message(msg)

    if lang == 'fi':
        message = fi.get_message(msg)

    if lang == 'fr':
        message = fr.get_message(msg)

    if lang == 'ga':
        message = ga.get_message(msg)

    if lang == 'hr':
        message = hr.get_message(msg)

    if lang == 'hu':
        message = hu.get_message(msg)

    if lang == 'it':
        message = it.get_message(msg)

    if lang == 'lt':
        message = lt.get_message(msg)

    if lang == 'lv':
        message = lv.get_message(msg)

    if lang == 'mt':
        message = mt.get_message(msg)

    if lang == 'nl':
        message = nl.get_message(msg)

    if lang == 'pl':
        message = pl.get_message(msg)

    if lang == 'pt':
        message = pt.get_message(msg)

    if lang == 'ro':
        message = ro.get_message(msg)

    if lang == 'sk':
        message = sk.get_message(msg)

    if lang == 'sl':
        message = sl.get_message(msg)

    if lang == 'sv':
        message = sv.get_message(msg)

    return message
