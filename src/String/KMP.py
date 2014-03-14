# -*- coding: utf-8 -*-
__author__ = 'ghost'


def get_next(t):
    T = [len(t)]
    T.extend(list(t))
    i, j = 1, 0
    next = [0] * len(t)
    while i < T[0]:
        if j == 0 or T[i] == T[j]:
            i += 1
            j += 1
            next[i-1] = j
        else:
            j = next[j-1]
    return next

def kmp(s, t, pos=0):
    """
        s是主串，t是字串，匹配成功返回匹配的位置，否则返回-1
    """
    len_s = len(s)
    len_t = len(t)

    next = get_next(t)

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




if __name__ ==  '__main__':
    s = 'abcabd abcabeabcabe'
    t = 'abcabe'
    print get_next(t)

    print kmp(s, t)


