#!/usr/bin/env python

def function_builder(n):
    l = []
    for x in range(n):
        l.append(lambda y, x=x: y+x)
    return l
