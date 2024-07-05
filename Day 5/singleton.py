class mark:
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
            cls.instance.high_mark = 0
        return cls.instance
    
    def new_mark(self, new_m):
        if new_m > self.high_mark:
            self.high_mark = new_m
            print(f"the highest mark is {self.high_mark}")
        else:
            print("no difference")

mark1 = mark()
mark1.new_mark(70)

mark2 = mark()
mark2.new_mark(100)

mark3 = mark()
mark3.new_mark(80)

print(f"overall highest mark{mark1.high_mark}")