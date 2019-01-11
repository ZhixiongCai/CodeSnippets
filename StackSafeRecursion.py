#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# StackSafeRecursion.py
#
# Copyright © 2019 zhixiong.cai <zhixiong.cai@yahoo.com>
#

"""
@package CodeSnippets.StackSafeRecursion

Recursion in Python that will not exhaust the stack.
"""

iden = lambda x: x

l = [1, 1] + [None] * 1000

def call(f):
    while callable(f):
        f = f()
    return f
	
def fibo(n, cont=iden):
    if l[n] is not None: return cont(l[n])
    return lambda: fibo(n - 1, lambda v_1: l.__setitem__(n - 1, v_1) or (lambda: fibo(n - 2, lambda v_2: l.__setitem__(n - 2, v_2) or (lambda: cont(v_1 + v_2)))))
	
call(fibo(1000))
