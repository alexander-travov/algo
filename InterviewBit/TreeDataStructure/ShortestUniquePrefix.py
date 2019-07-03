"""
Shortest Unique Prefix
======================

Find shortest unique prefix to represent each word in the list.

Example:

Input: [zebra, dog, duck, dove]
Output: {z, dog, du, dov}
where we can see that
zebra = z
dog = dog
duck = du
dove = dov
NOTE : Assume that no word is prefix of another. In other words, the representation is always possible.
"""

from __future__ import print_function


class Trie:
    def __init__(self, word_end=False):
        self.word_end = word_end
        self.children = {}

    def add(self, word):
        node = self
        for l in word:
            if l not in node.children:
                node.children[l] = Trie()
            node = node.children[l]
        node.word_end = True

    def __contains__(self, word):
        node = self
        for l in word:
            if l not in node.children:
                return False
            node = node.children[l]
        return node.word_end


    def prefix(self, word):
        next_letter_count = []
        node = self
        # Count number of splits at each letter
        for l in word:
            next_letter_count.append(len(node.children))
            node = node.children[l]
        # Go from last letter to the first split
        for i in range(len(word)-2, -1, -1):
            if next_letter_count[i] != 1:
                break
        return word[:i+1]


words = ['zebra', 'dog', 'duck', 'dove', 'zoo']
trie = Trie()
for w in words:
    trie.add(w)
print([trie.prefix(w) for w in words])
