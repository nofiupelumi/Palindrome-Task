# '''Abstraction in Python is a fundamental concept in object-oriented programming that allows you to simplify complex systems by hiding unnecessary details while exposing only the relevant information. 
#     It helps you manage the complexity of your code and makes it easier to work with.
#      Abstraction can be achieved through classes and methods.
#      Here are two examples to explain abstraction in Python:'''

# # Abstraction using Classes and Methods:
# # python
# # Define a base class 'Shape.'
# class Shape:
#     # Define an abstract method 'area' for calculating the shape's area.
#     def area(self):
#         pass

# # Define a subclass 'Circle' that inherits from the 'Shape' base class.
# class Circle(Shape):
#     # Constructor method for initializing a circle with a given 'radius.'
#     def __init__(self, radius):
#         self.radius = radius

#     # Implementation of the 'area' method specific to circles.
#     def area(self):
#         # Calculate and return the area of the circle using the formula.
#         return 3.14 * self.radius * self.radius

# # Define another subclass 'Rectangle' that also inherits from 'Shape.'
# class Rectangle(Shape):
#     # Constructor method for initializing a rectangle with 'length' and 'width.'
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     # Implementation of the 'area' method specific to rectangles.
#     def area(self):
#         # Calculate and return the area of the rectangle using length and width.
#         return self.length * self.width

# # Example usage:
# # Create an instance of the 'Circle' class with a radius of 5 units.
# circle = Circle(5)

# # Create an instance of the 'Rectangle' class with a length of 4 units and width of 6 units.
# rectangle = Rectangle(4, 6)

# # Calculate and print the area of the circle.
# print(f"Area of the circle: {circle.area()}")

# # Calculate and print the area of the rectangle.
# print(f"Area of the rectangle: {rectangle.area()}")
# ''' In this example, we define an abstract base class Shape with an abstract method area().
#   Subclasses Circle and Rectangle inherit from the Shape class and provide concrete implementations of the area() method.
#   This abstraction allows us to work with different shapes using a common interface while encapsulating the specific details of each shape.'''

# #EXAMPLE 2
# # Abstraction with a Vehicle Class:
# # Define a base class named 'Vehicle.'
# class Vehicle:
#     # Constructor method to initialize 'make' and 'model' attributes.
#     def __init__(self, make, model):
#         self.make = make
#         self.model = model

#     # Abstract method for starting the engine, to be implemented in subclasses.
#     def start_engine(self):
#         pass

# # Define a subclass 'Car' that inherits from the 'Vehicle' base class.
# class Car(Vehicle):
#     # Implementation of the 'start_engine' method specific to cars.
#     def start_engine(self):
#         # Return a message indicating the engine start for a car with make and model.
#         return f"Starting the engine of {self.make} {self.model} car."

# # Define another subclass 'Boat' that also inherits from the 'Vehicle' base class.
# class Boat(Vehicle):
#     # Implementation of the 'start_engine' method specific to boats.
#     def start_engine(self):
#         # Return a message indicating the engine start for a boat with make and model.
#         return f"Starting the engine of {self.make} {self.model} boat."

# # Example usage:
# # Create an instance of the 'Car' class with make "Toyota" and model "Camry."
# car = Car("Toyota", "Camry")

# # Create an instance of the 'Boat' class with make "Sea Ray" and model "Sundancer."
# boat = Boat("Sea Ray", "Sundancer")

# # Call the 'start_engine' method for the car and print the result.
# print(car.start_engine())

# # Call the 'start_engine' method for the boat and print the result.
# print(boat.start_engine())

# '''In this example, we have an abstract base class Vehicle with an abstract method start_engine(). 
# Subclasses Car and Boat inherit from the Vehicle class and provide specific implementations of the start_engine() method.
# This abstraction allows us to interact with different types of vehicles using a common interface, even though the implementation of starting the engine is different for cars and boats.'''