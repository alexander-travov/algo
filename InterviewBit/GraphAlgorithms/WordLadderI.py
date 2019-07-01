"""
Word Ladder I
=============

Given two words (start and end), and a dictionary, find the length of shortest transformation sequence from start to end, such that:

You must change exactly one character in every transformation
Each intermediate word must exist in the dictionary
Example :

Given:

start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note that we account for the length of the transformation path instead of the number of transformation itself.
"""

from __future__ import print_function
from collections import deque


def word_ladder(start, end, dictionary):
    n = len(start)

    letter_sets = [set() for _ in range(n)]
    for w in dictionary:
        for i, l in enumerate(w):
            letter_sets[i].add(l)

    q = deque()
    q.append(start)
    num_changes = {start: 0}

    while q:
        w = q.popleft()
        nc = num_changes[w]
        print(w, nc)

        for i, ls in enumerate(letter_sets):
            for l in ls - {w[i]}:
                candidate = w[:i] + l + w[i+1:]
                if candidate == end:
                    return nc+1
                if candidate in dictionary and candidate not in num_changes:
                    q.append(candidate)
                    num_changes[candidate] = nc+1

    return -1


print(word_ladder('hit', 'cog', ["hot","dot","dog","lot","log", "cog"]))
