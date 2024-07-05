class fruit:
    def cls(self):
        raise NotImplementedError()
    
class started(fruit):
    def cls(self):
        return "This is "

class banana(fruit):
    def __init__(self, ban):
        self.ban = ban
    def cls(self):
        return self.ban.cls()+"banana"
    
class kiwi(fruit):
    def __init__(self, kiw):
        self.kiw=kiw
    def cls(self):
        return self.kiw.cls()+"Kiwi"

x = started()
y = banana(x)
z=kiwi(x)
print(y.cls())
print(z.cls()) 

