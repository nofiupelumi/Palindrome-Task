[10/23, 3:24 PM] Nofiu Moruf: # # String formatting
# name = 'John'
# age = 20

# # # # string concatenation
# print('Hello ' + name + ' you are ' + str(age) + ' years old')

# # # # string interpolation
# print('Hello {} you are {} years old'.format(name, age))

# # # # string interpolation with index
# print('Hello {1} you are {0} years old'.format(age, name))

# # # # string interpolation with keyword arguments
# print('Hello {name} you are {age} years old'.format(name='James', age=25))

# # # # f-strings method
# print(f'Hello {name} you are {age} years old')

# school = 'ingryd academy'
# e = school[-8:-2]
# b = school[2:-8:2]
# print(e, len(e))
# print(b, len(b))

# # 2 decimal place example
# pi = 3.14159265
# print('Pi is', round(pi, 3)) # using round function
# # using string format to make it 2 dp
# print('Pi is {:.2f}'.format(pi))

# '''
# 2. You're developing a report generator. You have data about sales, including the
# product name, quantity sold, and total sales amount. Create a program that 
# takes this data and generate a report in the following format:
# Product: <product name>
# Quantity: <quantity sold>
# Total Sales: #<total sales amount> to 2 dp.

# 1. You're building a program to generate a personalized email msg. The user 
# provides their name and age. Write a program that takes these input and create 
# an email msg in the following format:  
# Hello  <name>, you are <age> years old.
# '''

# # code
# product = input('Enter product name: ')
# qty = input('Enter quantity: ')
# total_sales = float(input('Enter total sales: '))
# report = f"Product: {product}\nQuantity: {qty}\nTotal Sales: \
# #{round(total_sales, 2)}."
# print(report)

# # another string format task
# """
# You're building a URL generator. The user provides a domain name and a path.
# Write a program that takes these inputs and create a complete URL. Ensure the 
# URL includes "https://" at the beginning. 
# https://www.azlyrics.com/lyrics/bigdaddyweave/overwhelmed.html
# """

# # Control flow statements
# # if, if-else, if-elif-else, nested if
# # if statement
# # syntax:
# # if condition:
# #     code block
# #     code block

# # example:
# age = int(input('Enter your age: '))
# if age >= 18:
#     print('You are an adult.\nYou can vote')
    #print('You can vote')

# # if-else statement
# # syntax:
# # if condition:
# #     code block
# #     code block
# # else:
# #     code block
# #     code block

# # # example:
# age = int(input('Enter your age: '))
# if age >= 18:
#     print('You are an adult')
#     print('You can vote')
# else:
#     print('You are not an adult')
#     print('You cannot vote')

# # if-elif-else statement
# # syntax:
# # if condition:
# #     code block
# #     code block
# # elif condition:
# #     code block
# #     code block
# # else:
# #     code block
# #     code block

# # example:
# age = int(input('Enter your age: '))
# if age >= 18:
#     print('You are an adult')
#     print('You can vote')
# elif age >= 13:
#     print('You are a teenager')
#     print('You cannot vote')
# else:
#     print('You are a child')
#     print('You cannot vote')


# # male example
# coach = input('Enter your coach: ').lower()
# coach = coach.lower()
# if coach == 'pep':
#     print('Man city will win the league.\nThey\'ll win the ucl.')
# elif coach == 'ancelotti':
#     print('Madrid will win the league.\nThey will win the ucl.')
# elif coach == 'inzaghi':
#     print('Inter will win the league.\nThey will win the ucl.')
# else:
#     print('I don\'t know who will win the league.')


# female example
game = input('Enter your fav game: ').capitalize()
if game == 'Monopoly':
    print('Ire will win')
elif game == 'Squid':
    print('Joan will win')
elif game == 'Ludo':
    print('Francisca will win')
else:
    print('I don\'t know who will win') 


# # nested if statement
# # syntax:
# # if condition:
# #     code block
# #     code block
# #     if condition:
# #         code block
# #         code block
# #     else:
# #         code block
# #         code block
# # else:
# #     code block
# #     code block

# # example:
age = int(input('Enter your age: '))
if age >= 18:
    print('You are an adult')
    print('You can vote')
    if age >= 21:
        print('You can drive')
    else:
        print('You cannot drive')
else:
    print('You are a child')
    print('You cannot vote')
    if age >= 13:
        print('You can play fortnite')
    else:
        print('You cannot play fortnite')

# '''
# 1. You're building a grade calculator program. The user provides their test 
# score (btw 0 - 100), and you need to determine their grade based on the ffg
# criteria:
# A: 70 - 100
# B: 60 - 69
# C: 50 - 59
# D: 40 - 49
# E: 30 - 39
# F: 0 - 29

# 2. You're building a program to determine the cost of a trip. The user provides
# the distance of the trip in miles, and you need to determine the cost of the
# trip based on the ffg criteria:
# Distance <= 100 miles: $5
# Distance > 100 miles and <= 500 miles: $8
# Distance > 500 miles: $10

# 3. You're developing a program for a movie theater to calculate ticket prices.
# The user enters their age and the movie time (morning, afternoon or evening). 
# The ticket prices are as follows:
# - Morning shows are #100 for all ages.
# - Afternoon shows are #150 for adults (18 and above) and #100 for children.
# - Evening shows are #200 for adults and #100 for children.
# Write a program to calculate and display the ticket price. 
# '''

# # code
test_score = int(input('Enter your test score: '))
if test_score > 100:
    print('Not applicable. Stop lying!')
elif test_score >= 70:
    print('Your grade is A')
elif test_score >= 60:
    print('Your grade is B')
elif test_score >= 50:
    print('Your grade is C')
elif test_score >= 40:
    print('Your grade is D')
elif test_score >= 30:
    print('Your grade is E')
else:
    print('Your grade is F')


# # logical operators
# # and, or, not

# # example:
# # age = int(input('Enter your age: '))
# # if age >= 18 and age >= 21:
# #     print('You are an adult')
# #     print('You can vote')
# #     print('You can drive')
# # else:
# #     print('You are a child')
# #     print('You cannot vote')
# #     print('You cannot drive')

# # example:
# # age = int(input('Enter your age: '))
# # if age >= 18 or age >= 21:
# #     print('You are an adult')
# #     print('You can vote')
# #     print('You can drive')
# # else:
# #     print('You are a child')
# #     print('You cannot vote')
# #     print('You cannot drive')

# # example:
# # age = int(input('Enter your age: '))
# # if not age >= 18:
# #     print('You are a child')
# #     print('You cannot vote')
# #     print('You cannot drive')
# # else:
# #     print('You are an adult')
# #     print('You can vote')
# #     print('You can drive')
[10/23, 3:26 PM] Nofiu Moruf: # String formatting

# name = 'John'
# age = 20

# # string concatenation
# print('Hello ' + name + ' you are ' + str(age) + ' years old')

# # string interpolation
# print('Hello {} you are {} years old'.format(name, age))

# # string interpolation with index
# print('Hello {1} you are {0} years old'.format(age, name))

# # string interpolation with keyword arguments
# print('Hello {name} you are {age} years old'.format(name='James', age=25))

# # f-strings method
# print(f'Hello {name} you are {age} years old')

# 2 decimal place example
pi = 3.14159265
print('Pi is', round(pi, 2)) # using round function
# using string format to make it 2 dp
print('Pi is {:.2f}'.format(pi))

'''
1. You're developing a report generator. You have data about sales, including the
product name, quantity sold, and total sales amount. Create a program that 
takes this data and generate a report in the following format:

Product: <product name>
Quantity: <quantity sold>
Total Sales: #<total sales amount> to 2 dp.

2. You're building a program to generate a personalized email msg. The user 
provides their name and age. Write a program that takes these input and create 
an email msg in the following format:  

Hello  <name>, you are <age> years old.
'''

# code 
# report generator
# product_name = input('Enter product name: ')
# quantity_sold = int(input('Enter quantity sold: '))
# total_sales = float(input('Enter total sales: '))
# report = f"Product: {product_name}\nQuantity: {quantity_sold}\nTotal Sales: \
# #{total_sales:.2f}"
# print(report)

# print(f'Product: {product_name}')
# print(f'Quantity: {quantity_sold}')
# print(f'Total Sales: #{total_sales:.2f}')

# personalized email msg
# name = input('Enter your name: ')
# age = int(input('Enter your age: '))
# email_msg = 'Hello {}, you are {} years old.'.format(name,age)
# print(email_msg)

# another string format task
"""
You're building a URL generator. The user provides a domain name and a path.
Write a program that takes these inputs and create a complete URL. Ensure the 
URL includes "https://" at the beginning. 
"""


# Control flow statements
# if statement
# syntax:
# if condition:
#     code block
#     code block

# example:
# age = int(input('Enter your age: '))
# if age >= 18:
#     print('You are an adult.\nYou can vote')
#     #print('You can vote')

# if-else statement
# syntax:
# if condition:
#     code block
#     code block
# else:
#     code block
#     code block

# example:
# age = int(input('Enter your age: '))
# if age >= 18:
#     print('You are an adult')
#     print('You can vote')
# else:
#     print('You are not an adult')
#     print('You cannot vote')

# if-elif-else statement
# syntax:
# if condition:
#     code block
#     code block
# elif condition:
#     code block
#     code block
# else:
#     code block
#     code block

# example:
# age = int(input('Enter your age: '))
# if age >= 18:
#     print('You are an adult')
#     print('You can vote')
# elif age >= 13:
#     print('You are a teenager')
#     print('You cannot vote')
# else:
#     print('You are a child')
#     print('You cannot vote')

#coach = input('Enter your coach: ').lower()
#coach = coach.lower()
# if coach == 'pep':
#     print('Man city will win the league.\nThey\'ll win the ucl.')
# elif coach == 'ancelotti':
#     print('Madrid will win the league.\nThey will win the ucl.')
# elif coach == 'inzaghi':
#     print('Inter will win the league.\nThey will win the ucl.')
# else:
#     print('I don\'t know who will win the league.')


#game = input('Enter your fav game: ').capitalize()

# if game == 'Monopoly':
#     print('Hikmat will win')
# elif game == 'Squid':
#     print('Omowunmi will win')
# elif game == 'Ludo':
#     print('Oluwaferanmi will win')
# else:
#     print('I don\'t know who will win') 


# nested if statement
# syntax:
# if condition:
#     code block
#     code block
#     if condition:
#         code block
#         code block
#     else:
#         code block
#         code block
# else:
#     code block
#     code block

# example:
# age = int(input('Enter your age: '))
# if age >= 18:
#     print('You are an adult')
#     print('You can vote')
#     if age >= 21:
#         print('You can drive')
#     else:
#         print('You cannot drive')
# else:
#     print('You are a child')
#     print('You cannot vote')
#     if age >= 13:
#         print('You can play fortnite')
#     else:
#         print('You cannot play fortnite')

'''
1. You're building a grade calculator program. The user provides their test 
score (btw 0 - 100), and you need to determine their grade based on the ffg
criteria:
A: 70 - 100
B: 60 - 69
C: 50 - 59
D: 40 - 49
E: 30 - 39
F: 0 - 29

2. You're building a program to determine the cost of a trip. The user provides
the distance of the trip in miles, and you need to determine the cost of the
trip based on the ffg criteria:
Distance <= 100 miles: $5
Distance > 100 miles and <= 500 miles: $8
Distance > 500 miles: $10

3. You're developing a program for a movie theater to calculate ticket prices.
The user enters their age and the movie time (morning, afternoon or evening). 
The ticket prices are as follows:
- Morning shows are #100 for all ages.
- Afternoon shows are #150 for adults (18 and above) and #100 for children.
- Evening shows are #200 for adults and #100 for children.
Write a program to calculate and display the ticket price. 
'''

# code
test_score = int(input('Enter your test score: '))

if test_score > 100:
    print('Not applicable. Stop lying!')
elif test_score >= 70:
    print('Your grade is A')
elif test_score >= 60:
    print('Your grade is B')
elif test_score >= 50:
    print('Your grade is C')
elif test_score >= 40:
    print('Your grade is D')
elif test_score >= 30:
    print('Your grade is E')
else:
    print('Your grade is F')


# logical operators
# and, or, not

# example:
# age = int(input('Enter your age: '))
# if age >= 18 and age >= 21:
#     print('You are an adult')
#     print('You can vote')
#     print('You can drive')
# else:
#     print('You are a child')
#     print('You cannot vote')
#     print('You cannot drive')

# example:
# age = int(input('Enter your age: '))
# if age >= 18 or age >= 21:
#     print('You are an adult')
#     print('You can vote')
#     print('You can drive')
# else:
#     print('You are a child')
#     print('You cannot vote')
#     print('You cannot drive')

# example:
# age = int(input('Enter your age: '))
# if not age >= 18:
#     print('You are a child')
#     print('You cannot vote')
#     print('You cannot drive')
# else:
#     print('You are an adult')
#     print('You can vote')
#     print('You can drive')

# for else
# syntax:
# for item in iterable:
#     code block
#     code block
# else:
#     code block
#     code block

# example:
# for i in range(5):
#     print(i)
# else:
#     print('Loop completed')

# while else
[10/23, 3:26 PM] Nofiu Moruf: '''
Write a program that convert a temperature in celcius to fahrenheit.
The program should prompt the user for the temperature value.
'''

# Solution:

# Code (mtd 1):
# celcius = float(input("Enter a temperature in celcius: "))
# fahrenheit = (celcius * 9/5) + 32
# print("Temperature in fahrenheit is: ", fahrenheit)

# # mtd 2
# celcius = float(input("Enter a temperature in celcius: "))
# fahrenheit = (celcius * 1.8) + 32
# print("Temperature in fahrenheit is: ", fahrenheit)

z = input('Enter a number: ')
y = input('Enter another number: ')
x = z + y
print(x)

# Strings
name = 'John Doe'
#print(name)
school = "Moringa School"
#print(school)
club = '''Moringa School's Club'''
#print(club)

# String Concatenation
first_name = 'John'
last_name = 'Doe'

full_name = first_name + ' ' + last_name
print(full_name)

# # Strings are arrays
# # Accessing characters in a string
# print(full_name[5])

# # Slicing
# print(full_name[2:5])

# x = full_name[:5]
# print(x, 'size is =>', len(x))

# y = full_name[:4]
# print(y, 'size is =>',len(y))

# print(full_name[2:])

# # Negative Indexing
# print('-ve indexing =>',full_name[-4:-1]) # space Do
# print('+ve indexing =>',full_name[4:1]) # this is wrong according to number line system
# print('+ve indexing =>',full_name[1:4]) # this is right according to number line system

# print(full_name[-7:-3])
# answer: ohn 

# a = full_name[-6]
# print(a)
# x = full_name[:-6]
# y = full_name[:-6:-2]
# print(x, len(x))
# print(y, len(y))

# school = 'ingryd academy' # space acade
# a = school[-8:-2]
# print('a => ',a, len(a))
# b = school[-2:-8:-3] 
# print('b => ',b, len(b))
# c = school[-8:-2:3]
# print('c => ', c, len(c))
# d = school[::-1]
# print('d => ',d, len(d))

# String Methods
print(full_name.upper())
print(full_name.lower())
print(full_name.capitalize())
print(full_name.title())
print(full_name.swapcase())

print()
# Check if a string is in upper case
print(full_name.isupper())
print(full_name.islower())
print(full_name.istitle())
print(full_name.isalpha()) 
print(full_name.isdigit())
print(full_name.isalnum())
print(full_name.isspace())
print(full_name.startswith('J'))
print(full_name.endswith('E'))
print(full_name.find('oe'))
print(full_name.count('o'))


# Substring search
print('this is the substring search: ', full_name.index('Doe'))
sentence = 'I love programming'
sentence2 = 'This is ingryd, academy. We\'re learning, python programming.'
key = 'prog'
print('key is found in index: ', sentence.find(key))

# string split method
c = sentence2.split()
print('this is the efault split without delimeter: ',c)
print(c[3])

# split with a delimiter
print('this is the split with delimeter: ', sentence2.split(','))

# sting replace method
print(sentence2.replace('ingryd', 'Moringa'))

# Palindrome task
# what is a palindrome? 
# A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward as forward, 
# such as madam, racecar, lawal.

# solution

'''
1. accept word from user
2. convert it to lower case, reverse the word and remove spaces
3. compare the word and the reversed word
4. if they are the same, then it is a palindrome
5. else, it is not a palindrome
6. print the result
'''
# mtd 1:
word = input('Enter a word: ')

# convert to lower case
word = word.upper()
print('word is now lowered: ', word)

# reverse the word
reversed_word = word[::-1]
print('reversed word is: ', reversed_word)

# remove spaces
word = word.replace(' ', '')
print('word is now spaceless: ', word)

# compare the word and the reversed word
if word == reversed_word:
    print('The word is a palindrome')
else:
    print('The word is not a palindrome')

#print('noon' == 'Noon')

# mtd 2: 
word = input('Enter a word: ') # ask user for word
word = word.lower().replace(' ', '') # convert to lower case and remove spaces
print('converted word: ', word)
is_palindrome = word == word[::-1] # compare the word and the reversed word
print(is_palindrome)
print('The word is a palindrome => ', is_palindrome) if is_palindrome else print('The word  \
                                                        is not a palindrome => ', is_palindrome)

# sring formatting


# give an introductory class on functions
# functions
# what is a function?
# a function is a block of code that performs a specific task
# it is also called a method
# it is also called a procedure
# it is also called a subroutine
# it is also called a subprogram

# why do we use functions?
# to avoid repetition of code
# to improve code readability
# to improve code maintainability
# to improve code reusability
# to improve code testability
# to improve code efficiency

# how do we create a function?
# syntax:
# def function_name():
#     function body
#     function body
#     function body
#     function body

# how do we call a function?
# syntax:
# function_name()

# example:
# def say_hello():
#     print('Hello World')

# say_hello()

# def say_hello():
#     print('Hello World')

# say_hello()

# functions with parameters
# def say_hello(name):
#     print('Hello', name)

# say_hello('John')
# say_hello('Jane')

# functions with default parameters
# def say_hello(name='John'):
#     print('Hello', name)

# say_hello()
# say_hello('Jane')

# functions with return values
# def say_hello(name='John'):
#     return 'Hello ' + name

# print(say_hello())
# print(say_hello('Jane'))

# functions with multiple parameters
# def say_hello(first_name, last_name):
#     return 'Hello ' + first_name + ' ' + last_name

# print(say_hello('John', 'Doe'))

# functions with keyword arguments
# def say_hello(first_name, last_name):
#     return 'Hello ' + first_name + ' ' + last_name

# print(say_hello(last_name='Doe', first_name='John'))

# functions with arbitrary arguments
# def say_hello(*names):
#     for name in names:
#         print('Hello', name)

# say_hello('John', 'Jane', 'Doe', 'Mary')  

# functions with arbitrary keyword arguments
# def say_hello(**names):
#     for key, value in names.items():
#         print('Hello', key, value)

# say_hello(first_name='John', last_name='Doe', middle_name='Jane', maiden_name='Mary')

# functions with arbitrary keyword arguments
# def say_hello(**names):
#     for key, value in names.items():
#         print('Hello', key, value)

# say_hello(first_name='John', last_name='Doe', middle_name='Jane', maiden_name='Mary')

# functions
[10/23, 3:27 PM] Nofiu Moruf: # Python fundamentals
​
a = -200
print(a, type(a))
a = 'Nigeria is cool'
print(a, type(a))
a = 789.67
print(a, type(a))
a = False
print(a, type(a))
a = 4 + 3j
print(a, type(a))
a = None
print(a, type(a))
​
# Operators
x = 45/9
y = 5 * 3
z = x == y
​
print(z, type(z))
​
​
'''
You have a budget of #20000 to spend at a store.
Write a program that asks the user for the price 
of an item, checks if they can afford it and 
tells them the balance left.
'''      
​
budget = 20000
item_price = int(input('Enter the price of the item: '))
if budget >= item_price:
    balance = budget - item_price
    print('Your balance is #',balance)
    print('You can afford the item. Thanks!')
​

#ANOTHER ONE
'''
Data Structures; Lists
it's an array that holds values/data of different types.
it's grouped with a square bracket and it's mutable and ordered.
it's a heterogenous data structure
values in the lists are indexed 
they're iterable and they allow duplicates
it's a sequence of data that are separated by commas.
'''

# A simple todo-list app

# create an empty todo list
todo_list = []

# for item in range(len(todo_list)):
#     print(item)

# print()
# for zita in todo_list:
#     print(zita)

clubs = ['Chelsea', 'Barca']
print(clubs)

#clubs[2] = 'Napoli'
#print(f'clubs is now {clubs}')
# new_clubs = ('Arsenal', 'Spurs')
# clubs.extend(new_clubs)
# print(f'clubs => {clubs}')

# new_clubs = clubs
# print(f'new_clubs => {new_clubs}')

# main_clubs = clubs.copy()
# print(f'main_clubs => {main_clubs}')

# # # modify clubs list obj
# clubs[1] = 'Real Madrid'
# clubs.append('Liverpool')
# clubs.delete('Chelsea')

# del new_clubs[1]

# print(f'\nclubs is now => {clubs}\n')
# print(f'new_clubs is now => {new_clubs}\n')
# print(f'main_clubs is now => {main_clubs}')


nums = [1,23, 4, 6.7, 90, 234, 89.6, 4002]
max_num = max(nums)
nums.sort(reverse=True)
print(nums[-1])
print(max_num)



# while True:
#     print('\n**WELCOME TO MY TODO APP**\n')
#     # display the todo list
#     print('Here are your uncompleted task(s):\n')
#     for index, value in enumerate(todo_list, start=1):
#         print(f'{index}. {value}')
    
#     # get user choice
#     choice = input('\nWhat do you want to do? (add, complete, edit, delete, quit): ').lower()
    
#     # check for user choice and perform necessary operation
#     if choice == 'quit':
#         print('Thank you for using my todo app. Goodbye!')
#         break
#     elif choice == "add":
#         task = input('Enter a task: ').lower()
#         # add user task to the list
#         todo_list.append(task)
#     elif choice == 'complete':
#         user_index = int(input('Enter the index of the task you want to complete: '))
#         # check if index is valid
#         if user_index > len(todo_list):
#             print('Invalid index! Please, enter a smaller index .')
#         # check for -ve or 0 index
#         elif user_index <= 0:
#             print('Invalid index! Please, enter an index greater than 0.')
#         # check for valid index, complete task and remove from list
#         elif 1 <= user_index <= len(todo_list):
#             todo_list.pop(user_index - 1)
#     else:
#         print('Invalid choice! Please, enter a valid choice.')

#ANOTHER ONE
'''
Data Structures; Lists
it's an array that holds values/data of different types.
it's grouped with a square bracket and it's mutable and ordered.
it's a heterogenous data structure
values in the lists are indexed 
they're iterable and they allow duplicates
it's a sequence of data that are separated by commas.
'''

# A simple todo-list app

# create an empty todo list
todo_list = []

# for item in range(len(todo_list)):
#     print(item)

# print()
# for zita in todo_list:
#     print(zita)

clubs = ['Chelsea', 'Barca']
print(clubs)

#clubs[2] = 'Napoli'
#print(f'clubs is now {clubs}')
# new_clubs = ('Arsenal', 'Spurs')
# clubs.extend(new_clubs)
# print(f'clubs => {clubs}')

# new_clubs = clubs
# print(f'new_clubs => {new_clubs}')

# main_clubs = clubs.copy()
# print(f'main_clubs => {main_clubs}')

# # # modify clubs list obj
# clubs[1] = 'Real Madrid'
# clubs.append('Liverpool')
# clubs.delete('Chelsea')

# del new_clubs[1]

# print(f'\nclubs is now => {clubs}\n')
# print(f'new_clubs is now => {new_clubs}\n')
# print(f'main_clubs is now => {main_clubs}')


nums = [1,23, 4, 6.7, 90, 234, 89.6, 4002]
max_num = max(nums)
nums.sort(reverse=True)
print(nums[-1])
print(max_num)


'''
Data Structures; Lists
it's an array that holds values/data of different types.
it's grouped with a square bracket and it's mutable and ordered.
it's a heterogenous data structure
values in the lists are indexed 
they're iterable and they allow duplicates
it's a sequence of data that are separated by commas.
'''

# A simple todo-list app

# create an empty todo list
todo_list = []

# for item in range(len(todo_list)):
#     print(item)

# print()
# for zita in todo_list:
#     print(zita)

clubs = ['Chelsea', 'Barca']
print(clubs)

#clubs[2] = 'Napoli'
#print(f'clubs is now {clubs}')
# new_clubs = ('Arsenal', 'Spurs')
# clubs.extend(new_clubs)
# print(f'clubs => {clubs}')

# new_clubs = clubs
# print(f'new_clubs => {new_clubs}')

# main_clubs = clubs.copy()
# print(f'main_clubs => {main_clubs}')

# # # modify clubs list obj
# clubs[1] = 'Real Madrid'
# clubs.append('Liverpool')
# clubs.delete('Chelsea')

# del new_clubs[1]

# print(f'\nclubs is now => {clubs}\n')
# print(f'new_clubs is now => {new_clubs}\n')
# print(f'main_clubs is now => {main_clubs}')


nums = [1,23, 4, 6.7, 90, 234, 89.6, 4002]
max_num = max(nums)
nums.sort(reverse=True)
print(nums[-1])
print(max_num)



# while True:
#     print('\n**WELCOME TO MY TODO APP**\n')
#     # display the todo list
#     print('Here are your uncompleted task(s):\n')
#     for index, value in enumerate(todo_list, start=1):
#         print(f'{index}. {value}')
    
#     # get user choice
#     choice = input('\nWhat do you want to do? (add, complete, edit, delete, quit): ').lower()
    
#     # check for user choice and perform necessary operation
#     if choice == 'quit':
#         print('Thank you for using my todo app. Goodbye!')
#         break
#     elif choice == "add":
#         task = input('Enter a task: ').lower()
#         # add user task to the list
#         todo_list.append(task)
#     elif choice == 'complete':
#         user_index = int(input('Enter the index of the task you want to complete: '))
#         # check if index is valid
#         if user_index > len(todo_list):
#             print('Invalid index! Please, enter a smaller index .')
#         # check for -ve or 0 index
#         elif user_index <= 0:
#             print('Invalid index! Please, enter an index greater than 0.')
#         # check for valid index, complete task and remove from list
#         elif 1 <= user_index <= len(todo_list):
#             todo_list.pop(user_index - 1)
#     else:
#         print('Invalid choice! Please, enter a valid choice.')


#ANOTHER ONE
# Sets are arrays that stores heterogenous data types.
# They make use of curly braces.
# They are unordered and immutable(can't be changed).
# Also, duplicates are not allowed, you can add or remove items from a set but you can't change it.
# """fruits ={'banana','orange','orange', 'water melon'}type(fruits)fruitsfruitsDams = {'ingryd',False, 25, 0.7, 1, 0,True, 'man utd', 'garri', 'data_science', 'sugar'} DamsDamsDams[5]Dams= list(Dams)DamsDamsDams[-1] = 'akamu'DamsDams = set(Dams)Damsfor item in Dams:  print(item,type(item))True == 1True == 00.7 in DamsDams.add('fransisca')DamsDams.update([5,6,8])DamsDams#Discard methodDams.discard('fransisca')Dams#Remove methodDams.remove('man utd')Dams#Discard methodDams.discard('akamu')DamsDams.add('akamu sugar')DamsDams.pop()Dams#Discard methodDams.discard('boy')Dams#Remove methodDams.remove('girl')DamsDams.clear()Damsdel DamsDams'''Read up on the following set methods:union, intersection, intersection_update, symmetric_difference, symmetric_difference_update,difference, difference_update, issubset, issuperset, isdisjoint.give 2 examples each of the methods listed above'''"""Tuples: they are arrays that stores heterogenous data.They are indexed, immutables, ordered, and they allow duplicates."""my_tuple = (1,2,3, 'apple', 'book')type(my_tuple)my_tuplemy_tuple[2]sub_tuple = my_tuple[:-1](sub_tuple)my_tuple = list(my_tuple)my_tuplemy_tuple[3] = 'banana'my_tuplemy_tuple[3:4]#my_tuple[2:2] = my_tuple[3:4]#my_tuplemy_tuple[4:4] = my_tuple[1:2]my_tuplemy_tuple[4:4] = my_tuple[1:2]
# my_tuplemy_tuple[3:3] = my_tuple[2:3]
# my_tuple
