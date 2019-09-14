"""
Edit Distance
=============

Given two strings A and B, find the minimum number of steps required to convert A to B. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character


Input Format:

The first argument of input contains a string, A.
The second argument of input contains a string, B.
Output Format:

Return an integer, representing the minimum number of steps required.
Constraints:

1 <= length(A), length(B) <= 450
Examples:

Input 1:
    A = "abad"
    B = "abac"

Output 1:
    1

Explanation 1:
    Operation 1: Replace d with c.

Input 2:
    A = "Anshuman"
    B = "Antihuman"

Output 2:
    2

Explanation 2:
    => Operation 1: Replace s with t.
    => Operation 2: Insert i.
"""

from __future__ import print_function


def edit_distance(a, b):
    n = len(a)
    m = len(b)

    dp = [[-1]*(m+1) for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = i
    for i in range(m+1):
        dp[0][i] = i

    for i in range(1, n+1):
        for j in range(1, m+1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(
                    dp[i-1][j],   # delete
                    dp[i][j-1],   # insert
                    dp[i-1][j-1], # replace
                )

    return dp[n][m]


def ed_memo(a, b, dp=None):
    n = len(a)
    m = len(b)

    if dp is None:
        dp = [[-1]*(m+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = i
        for i in range(m+1):
            dp[0][i] = i

    if dp[n][m] != -1:
        return dp[n][m]

    if a[-1] == b[-1]:
        l = ed_memo(a[:-1], b[:-1], dp)
    else:
        l = 1 + min(
            ed_memo(a[:-1], b, dp),     # delete
            ed_memo(a, b[:-1], dp),     # insert
            ed_memo(a[:-1], b[:-1], dp) # replace
        )

    dp[n][m] = l
    return l


print(edit_distance('Anshuman', 'Antihuman'))
print(ed_memo('Anshuman', 'Antihuman'))
