# This script defines three functions:

# calculate_average: This function takes a list of numbers as input and returns the average of the numbers. 
If the length of the list is zero, it prints “Invalid population” and returns None.
# calculate_standard_deviation: This function takes a list of numbers as input and returns the standard deviation of the numbers. 
# If the mean of the numbers is None, it returns None.
# main: This function holds the main logic of the program and prompts the user to enter the size of the population and the numbers in the population. 
# If the size of the population is zero, it prints “Invalid population” and exits the program.
# The calculate_average function calculates the sum of the numbers in the list and divides it by the length of the list to get the average. 
# If the length of the list is zero, it prints “Invalid population” and returns None.
#  The function includes a docstring that describes its arguments, return value, and behavior.

# The calculate_standard_deviation function first calculates the mean of the numbers using the calculate_average function. 
# If the mean is None, it returns None. 
# It then calculates the variance of the numbers by summing the squared differences between each number and the mean, and dividing by the length of the list.
#  Finally, it returns the square root of the variance to get the standard deviation.
#  The function includes a docstring that describes its arguments, return value, and behavior.

# The main function prompts the user to enter the size of the population and the numbers in the population.
#  If the size of the population is zero, it prints “Invalid population” and exits the program. 
# It then calculates the standard deviation of the numbers using the calculate_standard_deviation function and prints the result if it is not None. 
# The function includes a docstring that describes its behavior.

# When you run this script with the input you provided, it will output the following result:

# Size of population: 5
# Enter number 1: 56
# Enter number 2: 23
# Enter number 3: 12
# Enter number 4: 78
# Enter number 5: 34
# Expected output: 23.69


# questoin 3 explanation 
# This code defines a Python script that does the following:

# 1. Imports the `math` module to use the `sqrt` function for square root calculations.

# 2. Defines a function called `get_primes(n)` that takes an integer `n` as an input parameter and returns a list of prime numbers less than `n`.

# 3. Initializes a list called `primes` with the prime number 2 because 2 is the first prime number.

# 4. Checks if the input parameter `n` is less than 2, and if so, it returns an empty list since there are no prime numbers less than 2.

# 5. Uses a `for` loop to iterate through numbers from 3 up to `n - 1`. It checks each number to determine if it's a prime number.

# 6. For each number in the loop, it sets a boolean variable `is_prime` to `True` initially. It calculates the square root of the current number and stores it in the variable `sqrt_num` using the `math.sqrt()` function.

# 7. It then checks if the current number is divisible by any previously discovered prime numbers. It does this by iterating through the `primes` list and checking if the number is divisible by any of these prime numbers.

# 8. If it finds a prime number in the `primes` list that is greater than the square root of the current number, it breaks out of the loop because there's no need to check further. This is because if a number is divisible by any number larger than its square root, it must also be divisible by a smaller prime factor.

# 9. If the current number is found to be divisible by any prime number in the `primes` list, it sets `is_prime` to `False` and breaks out of the loop.

# 10. If the `is_prime` variable remains `True` after the loop, it means that the current number is prime, so it is added to the `primes` list.

# 11. Finally, the function returns the `primes` list, which contains all prime numbers less than the input parameter `n`.

# 12. The code then enters a loop that repeatedly prompts the user to enter a number greater than 2 until a valid input is received. It handles invalid inputs and non-integer inputs with a `try-except` block.

# 13. Once a valid input is obtained, the `get_primes()` function is called with the user's input, and the prime numbers less than the input number are calculated and stored in the `prime_numbers` list.

# 14. The script then prints the prime numbers less than the input number.

# In summary, this code allows the user to input a number greater than 2, and it calculates and displays all the prime numbers less than that input number using a function called `get_primes()`. It also handles input validation and error messages for the user.

# question2

# This code is a Python script that performs the following tasks:

# 1. `input_occupants()`: This function prompts the user to enter the number of houses with different numbers of occupants. It uses a loop to iterate through 8 different categories of occupants, from 0 to 7. For each category, it repeatedly prompts the user to input the number of houses with that specific number of occupants. It validates the input to ensure it's a non-negative integer and handles exceptions (ValueError) if the user enters invalid input. The valid input values are stored in a list called `occupants`. The function returns this list, containing the count of houses for each category.

# 2. `calculate_percentage(numbers, total, number)`: This function calculates the percentage of a specific number in a list of numbers. It takes three arguments: `numbers` (the list of numbers), `total` (the total number of houses), and `number` (the specific number for which you want to calculate the percentage). It calculates the percentage as `(number * 100) / total` and returns the result as a floating-point number.

# 3. `main()`: The main function of the script. It first calls `input_occupants()` to obtain the count of houses for each category of occupants. Then, it calculates the total number of houses in the `total_houses` variable by summing up the values in the `occupants` list.

# 4. The script then prints a table with three rows: "Occupants," "No. dwellings," and "Percentage."

# 5. For each of the 7 categories of occupants (from 0 to 6), it prints the count of houses for that category from the `occupants` list.

# 6. After printing all the counts for each category, it calculates and prints the percentage of houses for each category using the `calculate_percentage()` function.

# 7. The script is supposed to be executed when the Python file is run as the main program. However, there's an issue with the code here. The condition `if _name_ == "_main_":` should be replaced with `if __name__ == "__main__":` to correctly identify the script as the main program.

# In summary, this code collects data about the number of houses with different occupant categories, calculates the percentage for each category, and then displays this data in a table format.