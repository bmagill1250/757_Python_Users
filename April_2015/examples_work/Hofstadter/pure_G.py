# -*- coding: utf-8 -*-
"""
Created on Fri Feb 27 15:32:10 2015

@author: brianmagill
"""
import math


def G(n):
    """Douglas Hofstadter's G Sequence"""

    if n == 0:
        return 0

    return n - G(G(n -1))


def closed_form(n):

    GOLDEN_RATIO = (1. + math.sqrt(5))/2.

    return int(math.floor((n + 1)/GOLDEN_RATIO))
