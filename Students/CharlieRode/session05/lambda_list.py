#!/usr/bin/env python

def function_builder(n):
    lst= []
    for i in range(n):
        lst.append(lambda p,q=i: p+q)
    return lst

def fun_builder(n):
    return [(lambda p, q=i: p+q) for i in range(n)]