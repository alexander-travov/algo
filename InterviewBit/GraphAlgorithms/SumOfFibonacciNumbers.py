"""
Sum Of Fibonacci Numbers
========================

How many minimum numbers from fibonacci series are required such that sum of numbers should be equal to a given Number N?
Note: repetition of number is allowed.

Example:

N = 4
Fibonacci numbers : 1 1 2 3 5 .... so on
here 2 + 2 = 4
so minimum numbers will be 2
"""

from __future__ import print_function
from collections import deque


def num_fib(n):
    # First lets find all Fibonacci numbers less or equal that n.
    fib = [1, 2]
    while fib[-1] <= n:
        fib.append(fib[-1] + fib[-2])
    fib.pop()
    fib.reverse()

    # Organize search in a BFS like manner.
    # We can go from n to n-fib1, n-fib2 ... n-fibk
    # We should find minimum number of such transitions that get us to zero.

    q = deque()
    num_subtractions = [-1] * (n+1)
    addendums = [[] for _ in range(n+1)]
    q.append(n)
    num_subtractions[n] = 0

    while q:
        k = q.popleft()
        ns = num_subtractions[k]
        for f in fib:
            if k-f >= 0 and num_subtractions[k-f] == -1:
                num_subtractions[k-f] = ns+1
                addendums[k-f] = addendums[k] + [f]
                if k-f == 0:
                    break
                q.append(k-f)

    return num_subtractions[0], addendums[0]


print(num_fib(4000))
