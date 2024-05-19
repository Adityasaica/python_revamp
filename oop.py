a=3
print(type(a))
# class is a structure to create a object
# 
# variables were called as attributes and function was called as methods

class Robot:
    # create a constructor
    def __init__(self,name,version):
        self.name=name
        self.version=version
        self.temp=25.0
    def say_hi(self):
        print(f"hi my name is {self.name}")

    def init_hardware(self):
        print("init hardware")

    def print_info(self):
        self.say_hi()
        print(f"versionnumber is {self.version}")


print("test")
# we need to create a object for to see theactual usage of the abjects

myrobot=Robot("adithya","1.05")

myrobot.say_hi()
myrobot.print_info()
print(myrobot.name)

