# -*- coding: utf8 -*-
"""
Hotel Reviews
=============

Given a set of reviews provided by the customers for different hotels and a string containing “Good Words”, you need to sort the reviews in descending order according to their “Goodness Value” (Higher goodness value first). We define the “Goodness Value” of a string as the number of “Good Words” in that string.

Note: Sorting should be stable. If review i and review j have the same “Goodness Value” then their original order would be preserved.

 You are expected to use Trie in an Interview for such problems 

Constraints:

1.   1 <= No.of reviews <= 200
2.   1 <= No. of words in a review <= 1000
3.   1 <= Length of an individual review <= 10,000
4.   1 <= Number of Good Words <= 10,000
5.   1 <= Length of an individual Good Word <= 4
6.   All the alphabets are lower case (a - z)
Input:

S : A string S containing "Good Words" separated by  "_" character. (See example below)
R : A vector of strings containing Hotel Reviews. Review strings are also separated by "_" character.
Output:

A vector V of integer which contain the original indexes of the reviews in the sorted order of reviews. 

V[i] = k  means the review R[k] comes at i-th position in the sorted order. (See example below)
In simple words, V[i]=Original index of the review which comes at i-th position in the sorted order. (Indexing is 0 based)
Example:

Input: 
S = "cool_ice_wifi"
R = ["water_is_cool", "cold_ice_drink", "cool_wifi_speed"]

Output:
ans = [2, 0, 1]
Here, sorted reviews are ["cool_wifi_speed", "water_is_cool", "cold_ice_drink"]
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


def sort_reviews(reviews, good_words):
    trie = Trie()
    for w in good_words.split('_'):
        trie.add(w)

    def num_matches(review):
        return sum(w in trie for w in review.split('_'))

    reviews.sort(key=num_matches, reverse=True)
    return reviews


print(sort_reviews(["water_is_cool", "cold_ice_drink", "cool_wifi_speed"], "cool_ice_wifi"))
