import ctypes
import sys

class M(object):
  
  def public(self):
    print('Use tab to see me')
    
  def _private(self):
    print("You won't be able to Tab to see me")
    
m = M()

m._private()

class DynamicArray(object):
  
  def __init__(self):
    
    self.n = 0
    self.capacity = 1
    self.A = self.make_array(self.capacity)
    
  def __len__(self):
    return self.n
    
  def __getitem__(self, k):
    
    if not 0 <= k < self.n:
      return IndexError('K is out of bounds!')
      
    return self.A[k]

  def append(self, ele):
    if self.n == self.capacity:
      self._resize(2*self.capacity)   # 2x if capacity isn't enough
      
    self.A[self.n] = ele
    self.n += 1
      
  def _resize(self, new_cap):
    B = self.make_array(new_cap)
    
    for k in range(self.n):
      B[k] = self.A[k]
      
    self.A = B
    self.capacity = new_cap
    
  def make_array(self, new_cap):
    return (new_cap * ctypes.py_object)()

  def array_size(self, arr):
    return sys.getsizeof(arr)

arr = DynamicArray()
arr.append(1)
print(len(arr))

arr.append(2)
arr.append(3)
arr.append(4)
arr.append(5)

print(len(arr))
print(arr.array_size(arr))
print(arr[1])