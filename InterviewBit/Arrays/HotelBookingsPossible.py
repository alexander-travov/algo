"""
Hotel Bookings Possible
=======================

A hotel manager has to process N advance bookings of rooms for the next season.
His hotel has K rooms. Bookings contain an arrival date and a departure date.
He wants to find out whether there are enough rooms in the hotel to satisfy the demand.
Write a program that solves this problem in time O(N log N) .

Input:

First list for arrival time of booking.
Second list for departure time of booking.
Third is K which denotes count of rooms.

Output:

A boolean which tells whether its possible to make a booking.
Return 0/1 for C programs.
O -> No there are not enough rooms for N booking.
1 -> Yes there are enough rooms for N booking.
Example :

Input :
        Arrivals :   [1 3 5]
        Departures : [2 6 8]
        K : 1

Return : False / 0

At day = 5, there are 2 guests in the hotel. But I have only one room.

Solution
--------

First, we sort arrays of arrivals and departures - O(NlogN)
Then, we create a mergesort-like procedure with two iterators and keep a counter of guests,
so when we get time from arrivals, we increment a counter, and
when we get time from departures, we decrement a counter.

If it never exceeds K, then there are enough rooms in hotel.
"""

from __future__ import print_function


def bookings_possible(arr, dep, k):
    arr.sort()
    dep.sort()
    
    num_rooms_busy = 0

    arr_iter = iter(arr)
    dep_iter = iter(dep)

    a = next(arr_iter, None)
    d = next(dep_iter, None)

    while True:
        # All arrivals are processed
        if a is None:
            break

        # Guest arrives
        if a < d:
            num_rooms_busy += 1
            if num_rooms_busy > k:
                return False
            a = next(arr_iter, None)
        # Guest departures
        else:
            num_rooms_busy -= 1
            d = next(dep_iter, None)
    return True


for arr, dep, k in (
        ([1, 3, 5], [2, 6, 8], 1),
    ):
    print(arr, dep, k, bookings_possible(arr, dep, k))
