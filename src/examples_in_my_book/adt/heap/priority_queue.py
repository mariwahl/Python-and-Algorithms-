#!/usr/bin/python3

# Mari von Steinkirch @ 2013
# mari.wahl9@gmail.com

import heapq


class PriorityQueue(object):
    """ A priority queue class. """
    def __init__(self):
        self._queue = []
        self._index = 0  # Comparing same priority level
    
    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item)) 
        self._index += 1
    
    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "Item({!r})".format(self.name)


def test_PriorityQueue():
    """ push and pop are all O(logN) """
    q = PriorityQueue()
    q.push(Item('test1'), 1)
    q.push(Item('test2'), 4)
    q.push(Item('test3'), 3)
    assert(str(q.pop()) == "Item('test2')")
    print('Tests passed!'.center(20, '*'))


if __name__ == '__main__':
    test_PriorityQueue()