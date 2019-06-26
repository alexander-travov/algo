"""
Points on the Straight Line
===========================

Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

Sample Input :

(1, 1)
(2, 2)
Sample Output :

2
You will be given 2 arrays X and Y. Each point is represented by (X[i], Y[i])

Solution
--------

At each point P we find the direction to every other point and save
in hash map the count of points with the same direction.

For points (x1, y1) and (x2, y2) direction (x2-x1, y2-y1).
Tricky part is to simplify various directions, so that (4,2), (6,3) and (-2,-1) will be the same (2,1) direction.
You need to calculate gcd of x, y and simplify (x,y) -> (x/gcd, y,gcd).

Don't forget to add the amount of the same points (direction (0,0)) to every non-zero direction count
because they are on the same line too.

Time complexity O(N^2), space complexity O(N)
"""

from __future__ import print_function
from collections import Counter


def gcd(a, b):
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a%b
    return a


def standardize_direction(x, y):
    if x == 0:
        if y == 0:
            return (0, 0)
        else:
            return (0, 1)
    elif y == 0:
        return (1, 0)
    
    sign = -1 if x*y < 0 else 1
    x = abs(x)
    y = abs(y)
    d = gcd(x, y)
    return (sign*x/d, y/d)


def max_points_on_line(points):
    max_count = 0
    for p1 in points:
        x1, y1 = p1
        dir_count = Counter()
        for p2 in points:
            x2, y2 = p2
            direction = standardize_direction(x2-x1, y2-y1)
            dir_count[direction] += 1
        # If all points are same
        same_count = dir_count[0, 0]
        if same_count > max_count:
            max_count = same_count
        del dir_count[0, 0]
        for d, count in dir_count.items():
            if count + same_count > max_count:
                max_count = count + same_count
    return max_count


print(max_points_on_line([
    (1, 1), (-1, 1), (2, -2),
    (3, 3), (1, 1), (-4, -4)
]))
