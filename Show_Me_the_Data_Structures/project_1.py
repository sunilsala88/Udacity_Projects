from collections import OrderedDict

class LRU_Cache(object):

  def __init__(self, capacity):
    
    self._capacity=capacity
    self._map = OrderedDict()
    if capacity<=0:
      print("capacity cannot be zero")
    

  def get(self, key):
    if key in self._map:
      val=self._map.pop(key)
      self._map[key]=val
      return val
    return -1

  def set(self, key, value):
    if self._capacity<=0:
      print("Can't perform operations on 0 capacity")
      return
    if key in self._map:
      del self._map[key]
    self._map[key]=value
    if len(self._map)>self._capacity:
      self._map.popitem(last=False)  #it deletes the first element that was inserted in the map
  

    

our_cache = LRU_Cache(5)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

print(our_cache.get(1))
# returns 1
print(our_cache.get(2))
# returns 2
print(our_cache.get(9))
# returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))
# returns -1 because the cache reached it's capacity and 3 was the least recently used entry

# Edge Case:
our_cache = LRU_Cache(2)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(1, 10)
print(our_cache.get(1))
# should return 10
print(our_cache.get(2))
# should return 2

our_cache = LRU_Cache(0)
our_cache.set(1, 1)
# should print some message like "Can't perform operations on 0 capacity cache"
print(our_cache.get(1))
# should return -1
