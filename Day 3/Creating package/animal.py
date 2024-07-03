class Dog: 
  def __init__(self): 
    self.breed = ['German shepheard', 'Bulldog', 'Labrador', 'Pomernian'] 
    
  def db(self): 
    print('Available breeds of the Dog: ') 
    for B in self.breed: 
      print('\t%s ' % B) 

class cat:

  def __init__(self):
    self.breed = ['Persian','Birman','Serberian','Burmila']

  def cb(self):
    print('Available breeds of the cat: ')
    for c in self.breed:
      print('\t%s'%c)