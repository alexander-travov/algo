"""
Substring Concatenation
=======================

You are given a string, S, and a list of words, L, that are all of the same length.

Find all starting indices of substring(s) in S that is a concatenation of each word in L exactly once and without any intervening characters.

Example :

S: "barfoothefoobarman"
L: ["foo", "bar"]
You should return the indices: [0,9].
(order does not matter).
"""

from __future__ import print_function
from collections import Counter


def find_words(text, words):
    word_len = len(words[0])
    num_words = len(words)
    word_set = set(words)

    indices = []

    for offset in range(word_len):
        word_count = Counter()

        for i in range(offset, len(text), word_len):
            word = text[i: i+word_len]
            if word in word_set:
                word_count[word] += 1

            start = i - (num_words-1)*word_len

            if len(word_count) == num_words:
                indices.append(start)

            if i // word_len + 1 >= num_words:
                prev_word = text[start: start+word_len]
                if prev_word in word_set:
                    word_count[prev_word] -= 1
                    if not word_count[prev_word]:
                        del word_count[prev_word]

    return indices


s = "barfoofoothebarjthoefoobarfooman"
print(s)
print(find_words(s, ["foo", "bar"]))
