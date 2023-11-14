# -*- coding:utf-8 -*-
# 用python实现排列组合C(n,m) = n!/m!*(n-m)!
# 自身节点影响力

def get_value(n):
    if n == 1:
        return n
    else:
        return n * get_value(n - 1)


def getValue(n, m):
    first = get_value(n)
    second = get_value(m)
    if n > m:
        third = get_value((n - m))
    else:
        third = second
    return first / (second * third)







