class Animal:
    location = "earth"


class Dog(Animal):
    has_fur = True

    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.is_cute = True



dog = Dog("Sparky", "brown")

# new_dog = Dog("Bob", "white")

# print(dog.name, dog.color)

# (dog.is_cute)


# print(dog.has_fur)
# print(dog.color)

# print(new_dog.color, new_dog.name, new_dog.is_cute)

# new_dog.color = "black"
# new_dog.is_cute = False
# print(new_dog.color, new_dog.name, new_dog.is_cute)

# dog.has_fur = False
# print(dog.has_fur, new_dog.has_fur)



print(dog.location)























# class Rectangle:
#     """A rectangle."""

#     def __init__(self, length, width):
#         """Create a rectangle."""

#         self.length = length
#         self.width = width

#     def calculate_area(self):
#         """Return the area of the rectangle."""

#         return self.length * self.width


# class Square(Rectangle):
#     """A square."""

#     """Squares have equal sides, so Square should have an __init__ method that takes in one argument — a number used to set the value of both self.length and self.width

#     Square should override its parent’s calculate_area method. Square’s version of calculate_area needs to do some extra validation to make sure that the area is valid for a square (becuase it’s possible that a user could have accidentally updated the square’s length or width and the sides are no longer the same length).

#     A square is valid if its length and width are equal

#     If the square is valid, return the area of the square

#     If the square is invalid, raise a ValueError that says "Invalid square.", for example:

#     raise ValueError("Invalid square.")"""

#     def __init__(self, length, width):
#         self.length = length
#         self.width = length


#     def calculate_sq_area(self):

#         if self.length == self.width:
#             return self.length * self.width
#         else:
#             raise ValueError("Invalid square.")

# shape = Square(5, 5)

# shape = shape.calculate_area

# print(shape)