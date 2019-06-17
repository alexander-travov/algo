#-*- coding: utf8 -*-
"""
Simplify Directory Path
=======================

Given an absolute path for a file (Unix-style), simplify it.

Examples:

path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"

Note that absolute path always begin with ‘/’ ( root directory )
Path will not have whitespace characters.
"""

from __future__ import print_function


def simplify(path):
    stack = []
    for d in path.split('/'):
        if not d or d == '.':
            continue
        elif d == '..':
            stack.pop()
        else:
            stack.append(d)
    return '/' + '/'.join(stack)


print(simplify("/a/./b/../../c/"))
