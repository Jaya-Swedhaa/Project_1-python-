class VehicalFactory():
    def vehical_name(self, name):
        if name=="car":
            return car()
        elif name=="truck":
            return truck()
        elif name=="bike":
            return bike()
        else:
            raise ValueError(f"there is no presence of such vehical called {name}")
        
class car:
    def cls(self):
        print("the vehical name is car")

class truck:
    def cls(self):
        print("the vehical name is truck")

class bike:
    def cls(self):
        print("the vehical name is bike")

factory = VehicalFactory()

player1 = factory.vehical_name("car")
player2 = factory.vehical_name("truck")
player3 = factory.vehical_name("bike")

player1.cls()
player2.cls()
player3.cls()