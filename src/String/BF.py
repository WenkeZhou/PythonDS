# -*- coding: utf-8 -*-
__author__ = 'ghost'

"""
 BF算法是普通的模式匹配算法，BF算法的思想就是将目标串S的第一个字符与模式串P的第一个字符进行匹配，若相等，则继续比较S的第二个字符和P的第二个字符；
 若不相等，则比较S的第二个字符和P的第一个字符，依次比较下去，直到得出最后的匹配结果。
"""


def brute_force(s, t):
    """
        s是主串，t是字串，匹配成功返回匹配的位置，否则返回-1
    """
    len_s = len(s)
    len_t = len(t)
    if len_s == 0 or len_t == 0:
        raise ValueError, u'string is empty'

    i, j, pos = 0, 0, -1
    while i < len_s and j < len_t:
        if s[i] == t[j]:
            i += 1
            j += 1
        else:
            i = i - j + 1
            j = 0
    pos = j == len_t and i - len_t or -1
    return pos

if __name__ == '__main__':
    s = 'hello python elo'
    t = 'elo'

    print brute_force(s, t)