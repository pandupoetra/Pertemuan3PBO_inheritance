class Shape:
    width=0
    def __init__(self,width):
        self.width=width
        
class Square(Shape):
    name="Square"
    def get_area(self):
        return self.width**2
        
class Trianggle(Shape):
    name="Trianggle"
    height=0
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def get_area(self):
        return 0.5 * self.width * self.height

SquareX=Square(5)
print("Luas dari SquareX adalah =",SquareX.get_area())
TrianggleY=Trianggle(5,3)
print("Luas dari TrianggleY adalah =",TrianggleY.get_area())