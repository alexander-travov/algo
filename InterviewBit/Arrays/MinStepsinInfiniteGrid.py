"""
You are in an infinite 2D grid where you can move in any of the 8 directions:

 (x,y) to
    (x+1, y),
    (x - 1, y),
    (x, y+1),
    (x, y-1),
    (x-1, y-1),
    (x+1,y+1),
    (x-1,y+1),
    (x+1,y-1)

You are given a sequence of points and the order in which you need to cover the points.

Give the minimum number of steps in which you can achieve it. You start from the first point.
"""


from __future__ import print_function


def distance(start, stop):
    x0, y0 = start
    x1, y1 = stop
    return max(abs(x1-x0), abs(y1-y0))


def num_steps(points):
    num_steps = 0
    for i in range(len(points)-1):
        num_steps += distance(points[i], points[i+1])
    return num_steps


points = [(0, 0), (1, 1), (1, 2)]
print('Points:', points)
print('Num steps:', num_steps(points))
