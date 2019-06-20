"""
Palindrome List
===============

Given a singly linked list, determine if it is a palindrome.
Return 1 or 0 denoting if its a palindrome or not, respectively.

Notes:

Expected solution is linear in time and constant in space.
For example,

List 1-->2-->1 is a palindrome.
List 1-->2-->3 is not a palindrome.
"""

from __future__ import print_function
from linked_list import Node


def is_palindrome(l):
    n = len(l)
    head, tail = l.split(n//2 - 1)
    head = head.reverse()
    if n % 2:
        result = head==tail.next
    else:
        result = head==tail
    head = head.reverse()
    head.join(tail)
    return result


for l in (
    Node.from_iterable([1, 2, 3, 2, 1]),
    Node.from_iterable([1, 2, 3, 2, 3]),
    Node.from_iterable([1, 2, 3, 3, 2, 1]),
    Node.from_iterable([1, 2, 3, 3, 2, 3])
):
    print(is_palindrome(l), l)
