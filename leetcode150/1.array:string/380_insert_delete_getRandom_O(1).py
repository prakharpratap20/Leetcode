"""
Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. 
    Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. 
    Returns true if the item was present, false otherwise.
int getRandom() 
    Returns a random element from the current set of elements 
    (it's guaranteed that at least one element exists when this method is called). 
    Each element must have the same probability of being returned.
    
You must implement the functions of the class such that each 
function works in average O(1) time complexity.
"""

import random


class RandomizedSet:

    def __init__(self):
        self.data_map = {}
        self.data = []

    def insert(self, val):
        if val in self.data_map:
            return False
        self.data_map[val] = len(self.data)
        self.data.append(val)
        return True

    def remove(self, val):
        if not val in self.data_map:
            return False
        last_elem_in_list = self.data[-1]
        index_of_elm_to_remove = self.data_map[val]

        self.data_map[last_elem_in_list] = index_of_elm_to_remove
        self.data[index_of_elm_to_remove] = last_elem_in_list
        self.data[-1] = val
        self.data.pop()
        self.data_map.pop(val)
        return True

    def getRandom(self):
        return random.choice(self.data)


randomizedSet = RandomizedSet()
print(randomizedSet.insert(1))
print(randomizedSet.remove(2))
print(randomizedSet.insert(2))
print(randomizedSet.getRandom())
print(randomizedSet.remove(1))
print(randomizedSet.insert(2))
print(randomizedSet.getRandom())
