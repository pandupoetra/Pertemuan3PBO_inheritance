#parent class
class Bird:
    def __init__(self):
        print("Birds is ready")
    def whoisThis(self):
        print("Birds")
    def swim(self):
        print("Swim faster")

#child class
class Penguin(Bird):
    def __init__(self):
        #call super() function
        super().__init__()
        print("Penguin is ready")
    def whoisThis(self):
        print("Penguin")
    def run (self):
        print("Run faster")

peggy=Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()