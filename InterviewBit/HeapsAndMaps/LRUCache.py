# -*- coding: utf8 -*-
"""
LRU Cache
=========

Design and implement a data structure for LRU (Least Recently Used) cache. It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least recently used item before inserting the new item.
The LRU Cache will be initialized with an integer corresponding to its capacity. Capacity indicates the maximum number of unique keys it can hold at a time.

Definition of “least recently used” : An access to an item is defined as a get or a set operation of the item. “Least recently used” item is the one with the oldest access time.

 NOTE: If you are using any global variables, make sure to clear them in the constructor. 
Example:

Input: 
    capacity = 2
    set(1, 10)
    set(5, 12)
    get(5)        returns 12
    get(1)        returns 10
    get(10)       returns -1
    set(6, 14)    this pushes out key = 5 as LRU is full. 
    get(5)        returns -1
"""

from __future__ import print_function
from time import time


class MinHeap:
    """
    Min Heap that can increase key for a given value.
    Assumes that all values are unique.
    """
    def __init__(self):
        self.kvs = []
        self.indices = {}

    def __len__(self):
        return len(self.kvs)

    def __str__(self):
        return str(self.kvs) + ' ' + str(self.indices)

    def _swap(self, i, j):
        k1, v1 = self.kvs[i]
        k2, v2 = self.kvs[j]
        self.kvs[i] = [k2, v2]
        self.kvs[j] = [k1, v1]
        self.indices[v1] = j
        self.indices[v2] = i

    def _sift_up(self, ind):
        if ind == 0:
            return
        parent = (ind-1) // 2
        if self.kvs[ind][0] < self.kvs[parent][0]:
            self._swap(ind, parent)
            self._sift_up(parent)

    def _sift_down(self, ind):
        left_ch = 2*ind + 1
        right_ch = 2*ind + 2
        if left_ch >= len(self.kvs):
            return
        min_ch = left_ch
        if (right_ch < len(self.kvs) and
            self.kvs[right_ch][0] < self.kvs[left_ch][0]):
            min_ch = right_ch
        if self.kvs[ind][0] > self.kvs[min_ch][0]:
            self._swap(ind, min_ch)
            self._sift_down(min_ch)

    def insert(self, key, value):
        self.kvs.append([key, value])
        ind = len(self.kvs)-1
        self.indices[value] = ind
        self._sift_up(ind)

    def get_min(self):
        if not self:
            return
        return self[0]

    def get_index(self, value):
        return self.indices.get(value, -1)

    def extract_min(self):
        if not self.kvs:
            return
        min_kv = self.kvs[0]
        del self.indices[min_kv[1]]
        last_kv = self.kvs.pop()
        if self.kvs:
            self.kvs[0] = last_kv
            self.indices[last_kv[1]] = 0
            self._sift_down(0)
        return min_kv

    def increase_key(self, value, new_key):
        ind = self.indices[value]
        self.kvs[ind][0] = new_key
        self._sift_down(ind)


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.time_heap = MinHeap()
        self.kv = {}

    def set(self, key, value):
        # update key access time
        if key in self.kv:
            self.time_heap.increase_key(time(), key)
        else:
            # remove the oldest key from cache
            if len(self.time_heap) == self.capacity:
                _, oldest_key = self.time_heap.extract_min()
                del self.kv[oldest_key]
            self.time_heap.insert(time(), key)
        self.kv[key] = value

    def get(self, key):
        if key not in self.kv:
            return None
        self.time_heap.increase_key(key, time())
        return self.kv[key]


c = LRUCache(2)
c.set(1, 10)
c.set(5, 12)
print(c.get(5))
print(c.get(1))
print(c.get(10))
c.set(6, 14)
print(c.get(5))
