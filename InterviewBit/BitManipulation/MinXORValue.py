"""
Min XOR value
=============

Given an array of N integers, find the pair of integers in the array which have minimum XOR value. Report the minimum XOR value.

Examples :
Input
0 2 5 7
Output
2 (0 XOR 2)
Input
0 4 7 9
Output
3 (4 XOR 7)

Constraints:
2 <= N <= 100 000
0 <= A[i] <= 1 000 000 000

Solution
--------

1. We can build trie for "words" consisting of 32 bits for every number.

As we add words to the trie, we keep:
- the maximum height from root at which occured the last node split.
- the minimum XOR value of 2 "word" endings that start at that node.


We can see, that if such split occurs nearer to the root, the resulting XOR value would be greater.

Time complexity: O(n), extra space O(n).

2. As we see from the trie solution, min XOR is guaranteed to be between the adjacent numbers if they are sorted.
So we can sort array and find min XOR with linear search.

Time complexity: O(n log(n)), extra space O(1).
"""
