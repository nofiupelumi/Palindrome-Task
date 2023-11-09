# # #Let's start by explaining the methods you listed for Python sets:

# # #1. #`union`: Returns a new set that contains all the unique elements from both sets.

# # #Example 1:
# # #python
# # set1 = {1, 2, 3}
# # set2 = {3, 4, 5}
# # union_set = set1.union(set2)
# # print(union_set)  # Output: {1, 2, 3, 4, 5}


# # #Example 2:
# # #python
# # set1 = {1, 2, 3}
# # set2 = {3, 4, 5}
# # union_set = set2.union(set1)
# # print(union_set)  # Output: {1, 2, 3, 4, 5}
# # 2. `intersection`: Returns a new set that contains the common elements between two sets.

# # Example 1:
# # python
# # set1 = {1, 2, 3}
# # set2 = {3, 4, 5}
# # intersection_set = set1.intersection(set2)
# # print(intersection_set)  # Output: {3}


# # Example 2:
# # python
# # set1 = {1, 2, 3}
# # set2 = {2, 3, 4}
# # intersection_set = set1.intersection(set2)
# # print(intersection_set)  # Output: {2, 3}


# # 3. `intersection_update`: Updates the set with the common elements between two sets.

# # Example 1:
# # python
# # set1 = {1, 2, 3}
# # set2 = {3, 4, 5}
# # set1.intersection_update(set2)
# # print(set1)  # Output: {3}


# # Example 2:
# # python
# # set1 = {1, 2, 3}
# # set2 = {2, 3, 4}
# # set1.intersection_update(set2)
# # print(set1)  # Output: {2, 3}

# # 4. `symmetric_difference`: Returns a new set with elements that are in either set, but not in both.

# # Example 1:
# # python
# # set1 = {1, 2, 3}
# # set2 = {3, 4, 5}
# # symmetric_difference_set = set1.symmetric_difference(set2)
# # print(symmetric_difference_set)  # Output: {1, 2, 4, 5}


# # Example 2:
# # python
# # set1 = {1, 2, 3}
# # set2 = {2, 3, 4}
# # symmetric_difference_set = set1.symmetric_difference(set2)
# # print(symmetric_difference_set)  # Output: {1, 4}


# # 5. `symmetric_difference_update`: Updates the set with elements that are in either set, but not in both.

# # Example 1:
# # python
# # set1 = {1, 2, 3}
# # set2 = {3, 4, 5}
# # set1.symmetric_difference_update(set2)
# # print(set1)  # Output: {1, 2, 4, 5}


# # Example 2:
# # python
# # set1 = {1, 2, 3}
# # set2 = {2, 3, 4}
# # set1.symmetric_difference_update(set2)
# # print(set1)  # Output: {1, 4}


# # 6. `difference`: Returns a new set with elements that are in the first set but not in the second set.

# # Example 1:
# # python
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# difference_set = set1.difference(set2)
# print(difference_set)  # Output: {1, 2}


# # Example 2:
# # python
# set1 = {1, 2, 3}
# set2 = {2, 3, 4}
# difference_set = set1.difference(set2)
# print(difference_set)  # Output: {1}


# # 7. `difference_update`: Updates the set with elements that are in the first set but not in the second set.

# # Example 1:
# # python
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# set1.difference_update(set2)
# print(set1)  # Output: {1, 2}

# # Example 2:
# # python
# set1 = {1, 2, 3}
# set2 = {2, 3, 4}
# set1.difference_update(set2)
# print(set1)  # Output: {1}


# # 8. `issubset`: Returns `True` if all elements of the first set are present in the second set.

# # Example 1:
# # python
# set1 = {1, 2}
# set2 = {1, 2, 3, 4}
# print(set1.issubset(set2))  # Output: True


# # Example 2:
# # python
# set1 = {1, 2, 3}
# set2 = {4, 5, 6}
# print(set1.issubset(set2))  # Output: False


# # 9. `issuperset`: Returns `True` if all elements of the second set are present in the first set.

# #Example 1:
# set1 = {1, 2, 3, 4}
# set2 = {1, 2}
# print(set1.issuperset(set2))  # Output: True


# # Example 2:
# # python
# set1 = {1, 2, 3}
# set2 = {4, 5, 6}
# print(set1.issuperset(set2))  # Output: False


# # 10. `isdisjoint`: Returns `True` if the two sets have no common elements.

# # Example 1:
# # python
# set1 = {1, 2, 3}
# set2 = {4, 5, 6}
# print(set1.isdisjoint(set2))  # Output: True


# # Example 2:
# # python
# # set1 = {1, 2, 3}
# # set2 = {3, 4, 5}
# # print(set1.isdisjoint(set2))  # Output: False


# # Now let's move on to explaining tuple unpacking:

# # Tuple unpacking is a feature in Python that allows you to assign the values of a tuple to multiple variables in a single line of code. It works by matching the elements of the tuple with the variables provided.

# # Example 1:
# # python
# tuple1 = (1, 2, 3)
# a, b, c = tuple1
# print(a, b, c)  # Output: 1 2 3


# # Example 2:
# # ```python
# tuple2 = ("apple", "banana", "cherry")
# fruit1, fruit2, fruit3 = tuple2
# print(fruit1, fruit2, fruit3)  # Output: apple banana cherry


# # In the first example, the values `(1, 2, 3)` are assigned to the variables `a`, `b`, and `c` respectively.
# # #In the second example, the values `("apple", "banana", "cherry")` are assigned to the variables `fruit1`, `fruit2`, and `fruit3` respectively. 
# # Tuple unpacking is a convenient way to assign multiple values from a tuple to individual variables.


# In Python, variable scope refers to the region of a program where a particular variable is accessible or can be used. Python has two main types of variable scopes: global scope and local scope. Additionally, there is also an enclosing or non-local scope, which comes into play when you have nested functions or classes.

# Global Scope:

# A variable defined in the global scope is accessible throughout the entire Python program.
# Variables declared at the top level of a Python script or module, outside of any function or class, are in the global scope.
# Global variables are accessible from any part of your code, including functions, classes, and modules.
# To declare a global variable, you simply define it at the top level of your code:

# Local Scope:

# A variable defined in a local scope is only accessible within a specific function or block of code where it is defined.
# Local variables have a limited lifespan; they are created when the function is called and destroyed when the function exits.
# When you create a variable inside a function, it is by default considered a local variable:

# Enclosing (Non-Local) Scope:

# This scope comes into play when you have nested functions. It is used for variables that are not in the local or global scope but are in an intermediate outer scope.
# If a variable is not found in the local scope, Python searches in the enclosing scope, which is usually the scope of the containing function.
# An enclosing variable can be read within a nested function, but if you want to modify it, you must use the nonlocal keyword.

# So, in summary:

# Global scope encompasses the entire program and includes variables defined at the top level.
# Local scope pertains to a specific function or block of code, and it includes variables defined within that block.
# Enclosing (non-local) scope is used in nested functions when a variable is not found in the local scope but is in an intermediate outer scope.
# These scopes help organize and manage variable access and ensure that variables are kept separate when necessary, minimizing potential naming conflicts and making code more maintainable.



# Functions with Arbitrary Arguments (*args):

# When you want to pass a variable number of non-keyword arguments to a function, you can use *args.
# This allows you to call the function with any number of positional arguments.

# Example 1:
# def print_args(*args):
#     for arg in args:
#         print(arg)

# print_args(1, "Hello", [3, 4], "World")
# # Output: 1
# #         Hello
# #         [3, 4]
# #         World
#  def calculate_average(*args):
#     if len(args) > 0:
#         return sum(args) / len(args)
#     else:
#         return 0

# avg = calculate_average(10, 20, 30)
# # avg is 20.0


# Functions with Arbitrary Keyword Arguments (**kwargs):

# **kwargs allows you to pass a variable number of keyword arguments to a function. It collects keyword arguments as a dictionary.

# Example 1:
# def print_kwargs(**kwargs):
#     for key, value in kwargs.items():
#         print(key, value)

# print_kwargs(name="Alice", age=30, city="New York")
# # Output: name Alice
# #         age 30
# #         city New York
# def print_person_info(**kwargs):
#     if "name" in kwargs and "age" in kwargs:
#         print(f"Name: {kwargs['name']}, Age: {kwargs['age']}")

# print_person_info(name="Bob", age=25, city="San Francisco")
# # Output: Name: Bob, Age: 25


# Functions with Default Parameter Values:

# You can set default values for function parameters. These defaults are used when the caller doesn't provide a value for the parameter.

# Example 1:
# def greet(name="Guest"):
#     print(f"Hello, {name}!")

# greet("Alice")  # Output: Hello, Alice!
# greet()          # Output: Hello, Guest!
# def power(base, exponent=2):
#     return base ** exponent

# result1 = power(2, 3)   # result1 is 8
# result2 = power(5)     # result2 is 25
#  Functions with List as an Argument:

# You can pass a list as an argument to a function. 
# The function can then operate on the list.

# Example 1:
# def process_numbers(numbers):
#     for num in numbers:
#         print(num)

# num_list = [1, 2, 3, 4]
# process_numbers(num_list)
# # Output: 1
# #         2
# #         3
# #         4
# def find_max(numbers):
#     return max(numbers)

# num_list = [7, 2, 9, 1, 4]
# max_value = find_max(num_list)
# # max_value is 9

# Recursion:

# Recursion is a technique where a function calls itself. It is often used to solve problems that can be broken down into smaller, similar subproblems.

# Example 1:
# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

# fib_5 = fibonacci(5)  # fib_5 is 5
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)

# result = factorial(5)  # result is 120