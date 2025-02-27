# Write a python program multiple inheritance from 3 different classes named, test 1, test 2, test 3.Where test 1 as a class variable, test 2 instance variable, test 3 as no variable.

class Test1:
    x = 10
    def __init__(self,y):
        print("Test1 class")
        self.y = y
    def show(self):
        print(self.x, self.y)
class Test2:
    def __init__(self,z =30):
        print("Test2 class")
        self.z = z
    def show(self):
        print(self.z)
class Test3:
    def __init__(self):
        print("Test3 class")
    def show(self):
        print(self.x, self.y, self.z)
class Test(Test1, Test2, Test3):
    def __init__(self, y, z):
        Test1.__init__(self, y)
        Test2.__init__(self, z)
        Test3.__init__(self)
        self.x = 20
        self.y = y
        self.z = z
    def show(self):
        print(self.x, self.y, self.z)
obj = Test(40,50)
obj.show()


