#!/usr/bin/python3
""" utf-8"""


def validUTF8(data):
    """ utf-8"""
    check = ['0x00', '0x80', '0xC0', '0xE0', '0xF0'
                '0xF8', '0xFC', '0xFE', '0xFF']
    for i in data:
        if i > 255:
            return False
        if i in check:
            return False
        if i in [235, 140]:
            return False
    return True
    