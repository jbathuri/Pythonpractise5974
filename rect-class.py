class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)

width = int(input("Enter width: "))
height = int(input("Enter height: "))
print(f"area = {Rectangle(width, height).area()} sq.units")
print(f"perimeter = {Rectangle(width, height).perimeter()} units")