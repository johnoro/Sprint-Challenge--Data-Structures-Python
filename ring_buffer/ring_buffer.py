class RingBuffer:
  def __init__(self, capacity):
    if capacity < 0:
      raise ValueError('Capacity must be non-negative.')
    self.capacity = capacity
    self.current = 0
    self.len = 0
    self.storage = [None] * capacity

  def append(self, item):
    if self.len == self.capacity:
      if self.current == self.capacity:
        self.current = 0
      self.storage[self.current] = item
      self.current += 1
    else:
      self.storage[self.len] = item
      self.len += 1

  def get(self):
    return self.storage[:self.len]
