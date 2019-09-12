"""
Possibility of finishing all courses given pre-requisites
=========================================================

There are a total of A courses you have to take, labeled from 1 to A.

Some courses may have prerequisites, for example to take course 2 you have to first take course 1, which is expressed as a pair: [1,2].

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Return 1 if it is possible to finish all the courses, or 0 if it is not possible to finish all the courses.

Input Format:

The first argument of input contains an integer A, representing the number of courses.
The second argument of input contains an integer array, B.
The third argument of input contains an integer array, C.
Output Format:

Return a boolean value:
    1 : If it is possible to complete all the courses.
    0 : If it is not possible to complete all the courses.
Constraints:

1 <= A <= 6e4
1 <= length(B) = length(C) <= 1e5
1 <= B[i], C[i] <= A
Example:

Input 1:
    A = 3
    B = [1, 2]
    C = [2, 3]

Output 1:
    1

Explanation 1:
    It is possible to complete the courses in the following order:
        1 -> 2 -> 3

Input 2:
    A = 2
    B = [1, 2]
    C = [2, 1]

Output 2:
    0

Explanation 2:
    It is not possible to complete all the courses.
"""

from __future__ import print_function


graph = {
    6: [1, 2],
    1: [2],
    2: [3],
    4: [5],
    5: [1],
}


def has_cycle(graph):
    used = {}

    def dfs(node, num):
        used[node] = num
        for n in graph.get(node, []):
            if n in used:
                if used[n] == num:
                    return True
            else:
                cycle = dfs(n, num)
                if cycle:
                    return True
        return False

    num = 1
    for n in range(1, len(graph)+1):
        if n not in used:
            cycle = dfs(n, num)
            if cycle:
                return True
            num += 1
    return False


print(has_cycle(graph))
