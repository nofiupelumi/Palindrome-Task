class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Example usage:
circle = Circle(5)
rectangle = Rectangle(4, 6)

print(f"Area of the circle: {circle.area()}")
print(f"Area of the rectangle: {rectangle.area()}")
