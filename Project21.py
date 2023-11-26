#Working with modules e.g  datetime & random

import random

# Get a random integer from the range 5 to 15 (exclusive)
random_number = random.randrange(5, 15)
print("Random Number between 5 and 14:", random_number)

import random

colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple']

# Get a random sample of 3 colors from the list
random_colors = random.sample(colors, 3)
print("Random Sample of 3 Colors:", random_colors)

import random

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Shuffle the list of numbers
random.shuffle(numbers)
print("Shuffled List:", numbers)

import random

# Generate a random floating-point number between 1.0 and 10.0
random_float = random.uniform(1.0, 10.0)
print("Random Floating-Point Number between 1.0 and 10.0:", random_float)

import random

options = ['apple', 'banana', 'cherry', 'date', 'fig', 'grape', 'kiwi', 'orange', 'pear', 'watermelon']

random_fruit = random.choice(options)
print("Randomly Chosen Fruit:", random_fruit)

import random

random_number = random.randint(1, 10)
print("Random Number between 1 and 10:", random_number)




from datetime import datetime

current_datetime = datetime.now()
print("Current Datetime:", current_datetime)

from datetime import date

today_date = date.today()
print("Today's Date:", today_date)

from datetime import datetime

date_string = "2023-01-01"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d")
print("Parsed Date:", parsed_date)

from datetime import datetime

current_datetime = datetime.now()
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted Datetime:", formatted_datetime)

from datetime import datetime, timedelta

today = datetime.now()
future_date = today + timedelta(days=7)
print("Future Date:", future_date)

from datetime import time

current_time = time(12, 30, 0)
print("Current Time:", current_time)

#list of 20 numbers between 0-100