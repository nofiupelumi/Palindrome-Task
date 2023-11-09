# QUESTION 1
# You are building a program to generate a personalized email msg. 
# The user pqrovides teir name and age .  
# write a program that takes these input and create.
# Hello<name> , you are age <age> years old.
'''
#SOLUTION 1
name= input('Enter your name: ')
age = input ('Enter your age: ')
email_msg= "hello {}, you are {} years old".format(name, age) # or f'hello {name} you are {age} years  old.
'''
#question 2
'''
you are developing a report generator you have data about sales including the product name uantity quantity_sold, and the total sales amount. 
create a program that  takes this data and generate a report in the following format:
Product:<product name>
quantity:<quantity sold>
Total sale:<total_sales_amount> in 2dp
'''

'''#NUMBER 2 SOLUUTION
product = input('enter the name:')
quantity_sold = input('enter the name:')
total_sales_amount= input('enter the name:')
Result =f'product:{product}\n Quantity:{quantity_sold}\n Total sale:#{round(total_sales_amount,2)}.'
print(Result)'''

#QUESTION 3
'''
You are building a URL generator . The user provides a domain name and a path . 
write a program that takes this input and create a complete URL.
Ensures the URL includes "https://" at the begining'
'''
# #NUMBER 3 SOLUUTION
# name = input('enter the name:')
# path = input('enter the name:')
# total_sales_amount= input('enter the name:')
# Result =f'"https://"{name}/{path}.'
# print(Result)

# QUESTION ASSIGNMENT 4
# You are developing a program  for a movie theatre to calculate ticket prices. 
# The user enters their age and the movie time(morning, afternoon , evening).
# The ticket pries are as follows
# -morning shows are #100 for all ages 
# -Afternoon shows are #150 adults(18 and BOVE )and  #100 for chilldren.
# Evening shows are #200 for adults
# and #100 for children. 
# Wrute a progrm to calculate and display the ticket price.

#SOLUTION 4
# age= input('Enter Age: ')
# movie_time=input('Enter Day(Morning,Afternoon,evening): ').lower()
# if movie_time == "morning":
#     print('Your ticket price is #100')
# elif age >=18 and movie_time=='afternoon':
#     print("Your ticket price is #150 ")
# elif age <18 and movie_time=='afternoon':
#     print("Your ticket price is #100 ")
# elif age <18 and movie_time=='evening':
#     print("Your ticket price is #100 ")
# elif age >=18 and movie_time=='evening':
#     print("Your ticket price is #100 ")
# else:
#     print('invalid input')

# QUESTION ASSIGNMENT 5
# YOU are building a program to determine the cost of a trip . 
# The user provide the distance of the trip in miles, and you need determine the cost  of the trip baased on the ffg criteria :
# Distance <=100miles :$5
# Distance <= 100miles and <=500miles:$8
# Distance >500miles:$10

# SOLUTION 5
# distance = input('enter distance in miles:')
# if distance <=100 :
#     print('cost of this is $5')
# elif distance>100:
#     print('cost of this is $8')
# elif distance<=500:
#     print('cost of this is $8')
# else:
#     print ('cost of a trip is $10')



# #QUESTION ASSIGNMENT 6
# YOU ARE BUILDING A GRADE CALCLATOR PROGRAM . 
# THE USER PROVIDES THEIR TEST SCORE (BTW 0-100), AND YOU NEED TO DETERMINE THEIR GRAADE BASED ON THE FFG:
# A:70-100
# B:60-69
# C:50-59
# D:40-49
# E:30-39
# F:0-29



#SOLUTION
# grade_calculator= int(input('Enter Number between (0-100):'))
# if 70<=grade_calculator<=100:
#     print ('Your Grade is A')
# elif 60<=grade_calculator<=69:
#      print ('Your Grade is B')
# elif 50<=grade_calculator<=59:
#      print ('Your Grade is C')
# elif 40<=grade_calculator<=49:
#     print ('Your Grade is D')
# elif 30<=grade_calculator<=39:
#     print ('Your Grade is E')
# elif 0<=grade_calculator<=29:
#    print ('Your Grade is F') 
# else:
#     print('invalid input') 