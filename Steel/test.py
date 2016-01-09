#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Pyltsin'


def gen():
    i = 0
    while True:
        i += 1
        yield i


for x in gen():
    print x
    if x > 10:
        break
