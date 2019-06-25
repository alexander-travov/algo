"""
Longest Substring Without Repeat
================================

Given a string, 
find the length of the longest substring without repeating characters.

Example:

The longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3.

For "bbbbb" the longest substring is "b", with the length of 1.
"""

from __future__ import print_function


def max_substr_without_repeat(string):
    # If we know the alphabet beforehand, we can use
    # some other struct to guarantee perfect hashing
    # F.e. array for ASCII strings.
    last_occurence = {}
    max_len = 0
    start = -1
    cur_len = 0

    for i, letter in enumerate(string):
        pos = last_occurence.get(letter, -1)

        # If we didn't encounter that letter
        # or we saw it very far to the left last time
        # add it to the current substring.
        # Otherwise, shrink current substring
        if pos == -1 or i-pos > max_len:
            cur_len += 1
        else:
            cur_len = i-pos

        last_occurence[letter] = i

        if cur_len > max_len:
            max_len = cur_len
            start = i - cur_len + 1
        cur_substr = string[i-cur_len+1:i+1]
        max_substr = string[start:start+max_len]
        print(letter, cur_substr, max_substr)

    return max_substr


print(max_substr_without_repeat('babcdbefghe'))
