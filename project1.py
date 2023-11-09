# #question 
# '''you have a budget of 20000 to spend at a store .
# write a program that asks the user for the price of an item check if they can afford it and tell them the balance.
# using simple python syntax and write out the algorithm''' 

# #ALgorithm
# '''Algorithm:

# Initialize the budget to $20,000.
# Ask the user to enter the price of the item.
# Check if the item's price is less than or equal to the budget.
# If the item is affordable, calculate the balance by subtracting the item's price from the budget and display the balance.
# If the item is not affordable, inform the user that the item is too expensive for their budget.
# You can run this Python program, and it will prompt you to enter the price of the item.
# It will then determine if you can afford the item and calculate the remaining balance accordingly.'''

# #solution
# budget= 20000
# price= int(input('Enter the price of the item'))
# print('You can afford this item')
# balance= budget - price
# print('Your balance is',balance)

# #question Assignment 
# '''Write a program that convert a temperature in celsius to fahrenheit.
# Prompt the user for the temperature value.'''

# #Solution
# # Step 1: Ask the user to input the temperature in Celsius
# celsius = float(input("Enter the temperature in Celsius: "))

# # Step 2: Perform the conversion to Fahrenheit
# fahrenheit = (celsius * 9/5) + 32

# # Step 3: Display the result
# print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")


names = ["Alice", "Bob", "Anna", "David", "Eve"]
a_names = list(filter(lambda name: name.startswith('A'),names))
# Result: a_names = ["Alice", "Anna"]
print(tuple(a_names))


num=[23,5,67,333,445,345,100]
odd