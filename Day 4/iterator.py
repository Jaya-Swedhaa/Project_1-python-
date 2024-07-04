'''class iteration:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

B = iteration()
C = iter(B)

for x in C:
  print(x)'''

tup = ('a', 'b', 'c', 'd', 'e')
 
# creating an iterator from the tuple
tup_iter = iter(tup)

for i in tup_iter:
    print(i)