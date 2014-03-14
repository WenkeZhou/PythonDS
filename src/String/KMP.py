# -*- coding: utf-8 -*-
__author__ = 'ghost'

"""
"""

# C 风格求 next 数组. 字符串数组的索引从 1 开始


def get_next_c(t):
    T = [len(t)]
    T.extend(list(t))
    i, j = 1, 0
    next = [0] * len(t)
    while i < T[0]:
        if j == 0 or T[i] == T[j]:
            i += 1
            j += 1
            next[i - 1] = j
        else:
            j = next[j - 1]
    return next


def kmp_c(s, t, pos=0):
    len_s = len(s)
    len_t = len(t)
    # 求得 next 数组
    next = get_next_c(t)
    i, j, = pos, 0
    while i < len_s and j < len_t:
        if s[i] == t[j]:
            i += 1
            j += 1
        else:
            if j == 0:
                i += 1
                j = next[j]
            else:
                j = next[j] - 1
    pos = j == len_t and i - len_t or -1
    return pos


def KMPC(s, t, pos=0):

    len_s = len(s)
    len_t = len(t)
    if len_s == 0 or len_t == 0:
        raise ValueError, u'string is empty'

    T = [len_t]
    T.extend(list(t))
    i, j = 1, 0
    next = [0] * len(t)
    while i < T[0]:
        if j == 0 or T[i] == T[j]:
            i += 1
            j += 1
            next[i - 1] = j
        else:
            j = next[j - 1]

    i, j, = pos, 0
    while i < len_s and j < len_t:
        if s[i] == t[j]:
            i += 1
            j += 1
        else:
            if j == 0:
                i += 1
                j = next[j]
            else:
                j = next[j] - 1
    pos = i - len_t if j == len_t else -1
    return pos

# python 风格


def get_next(t):

    i, j = 0, -1
    next = [-1] * len(t)
    while i < len(t) - 1:
        if j == -1 or t[i] == t[j]:
            i += 1
            j += 1
            next[i] = j
        else:
            j = next[j]
    return next


def kmp(s, t, pos=0):
    next = get_next(t)
    i, j = pos, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j] or j == 0:
            i += 1
            j += 1
        else:
            j = next[j]

    pos = i - j if j == len(t) else -1
    return pos


def KMP(s, t, pos=0):

    len_s = len(s)
    len_t = len(t)
    if len_s == 0 or len_t == 0:
        raise ValueError, u'string is empty'

    # 生成 next 数组
    next = [-1] * len_t
    i, j = 0, -1

    while i < len_t - 1:
        if j == -1 or t[i] == t[j]:
            i += 1
            j += 1
            next[i] = j
        else:
            j = next[j]

    # 匹配
    i, j = pos, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j] or j == 0:
            i += 1
            j += 1
        else:
            j = next[j]

    pos = i - j if j == len(t) else -1
    return pos





if __name__ == '__main__':
    s = 'abcabe aaaaae abcabe'
    t = 'aaaaae'
    print get_next(t)
    print get_nexts(t)
    # print kmp_c(s, t, 8)
    # print KMP(s, t, 111)

