#!/usr/bin/python3

class Square:
    
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def area(self):
        """Calculate area of the square"""
        return self.width * self.width

    def perimeter(self):
        """Calculate perimeter of the square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print(s.area())
    print(s.perimeter())
