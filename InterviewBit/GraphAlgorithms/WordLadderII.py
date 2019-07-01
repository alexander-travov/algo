"""
Word Ladder II
==============

Given two words (start and end), and a dictionary, find the shortest transformation sequence from start to end, such that:

You must change exactly one character in every transformation
Each intermediate word must exist in the dictionary
Example :

Given:

start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]

Return

[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
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
    prev_word = {start: ''}

    while q:
        w = q.popleft()
        for i, ls in enumerate(letter_sets):
            for l in ls - {w[i]}:
                candidate = w[:i] + l + w[i+1:]
                if candidate in dictionary and candidate not in prev_word:
                    q.append(candidate)
                    prev_word[candidate] = w

    w = end
    sequence = [w]
    while prev_word[w]:
        sequence.append(prev_word[w])
        w = prev_word[w]
    sequence.reverse()
    return sequence


print(word_ladder('hit', 'cog', ["hot","dot","dog","lot","log", "cog"]))
