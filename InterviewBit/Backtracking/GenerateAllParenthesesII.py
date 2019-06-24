"""
Generate all Parentheses II
===========================

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses of length 2*n.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"
Make sure the returned list of strings are sorted.
"""

from __future__ import print_function
import sys


def generate_parentheses(n):
    if n == 0:
        yield ''
    else:
        for k in range(n):
            for par1 in generate_parentheses(n-k-1):
                for par2 in generate_parentheses(k):
                    yield '(' + par1 + ')' + par2


n = int(sys.argv[1]) if len(sys.argv)==2 else 4
for par in generate_parentheses(n):
    print(par)
