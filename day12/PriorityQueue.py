#!/usr/bin/env python3
"""
A very simple implementation of priority queue, which allows you to modify 
the priorities. It's not very efficient (aka. terribly slow) but works just fine
for graph algorithms.
"""

class PriorityQueue:
    def __init__(self) -> None:
        self.data = []
    
    def put(self, el):
        self.data.append(el)

    def get(self):
        ind = 0
        min_prio = self.data[ind][0] # minimum priority

        for i in range(len(self.data)):
            if self.data[i][0] < min_prio:
                ind = i
                min_prio = self.data[i][0]
        
        min_el = self.data[ind]
        del self.data[ind]
        return min_el
    
    def empty(self) -> bool:
        return len(self.data) == 0