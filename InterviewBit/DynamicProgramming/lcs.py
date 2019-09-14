"""
Longest Common Subsequence
==========================
"""

from __future__ import print_function


def lcs(a, b):
    n = len(a)
    m = len(b)

    dp = [[-1]*(m+1) for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 0
    for i in range(m+1):
        dp[0][i] = 0

    for i in range(1, n+1):
        for j in range(1, m+1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[n][m]


def lcs_memo(a, b, dp=None):
    n = len(a)
    m = len(b)

    if dp is None:
        dp = [[-1]*(m+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = 0
        for i in range(m+1):
            dp[0][i] = 0

    if dp[n][m] != -1:
        return dp[n][m]

    if a[n-1] == b[m-1]:
        l = 1 + lcs_memo(a[:-1], b[:-1], dp)
    else:
        l = max(lcs_memo(a[:-1], b, dp), lcs_memo(a, b[:-1], dp))

    dp[n][m] = l
    return l


print(lcs('ABCDGH', 'AEDFHR'))
print(lcs_memo('AGGTAB', 'GXTXAYB'))
