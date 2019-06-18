"""
Redundant Braces
================

Write a program to validate if the input string has redundant braces?
Return 0/1

0 -> NO
1 -> YES
Input will be always a valid expression

and operators allowed are only + , * , - , /

Example:

((a + b)) has redundant braces so answer will be 1
(a + (a + b)) doesn't have have any redundant braces so answer will be 0
"""

from __future__ import print_function
import string


OPERATOR, OPERAND, OPEN_PAREN = range(3)


def has_redundant_braces(exp):
    stack = []
    for symb in exp:
        if symb in '+-*/':
            stack.append(OPERATOR)
        elif symb in string.ascii_letters + string.digits:
            stack.append(OPERAND)
        elif symb == '(':
            stack.append(OPEN_PAREN)
        elif symb == ')':
            if (len(stack) < 4 or
                stack.pop() != OPERAND or
                stack.pop() != OPERATOR or
                stack.pop() != OPERAND or
                stack.pop() != OPEN_PAREN):
                return False
            stack.append(OPERAND)
    return True


for exp in ('((a + b))', '(a + (a + b))'):
    print(exp, has_redundant_braces(exp))
