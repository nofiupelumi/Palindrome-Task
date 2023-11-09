# # QUESTION1
# def calculate_average(numbers):
#     """
#     Calculate the average of a list of numbers.

#     Args:
#         numbers (list): A list of numbers.

#     Returns:
#         float: The average of the numbers, or None if the list is empty.
#     """
#     if len(numbers) == 0:
#         print("Invalid population")
#         return None
#     total = 0
#     for number in numbers:
#         total += number
#     return total / len(numbers)

# def calculate_standard_deviation(numbers):
#     """
#     Calculate the standard deviation of a list of numbers.

#     Args:
#         numbers (list): A list of numbers.

#     Returns:
#         float: The standard deviation of the numbers, or None if the list is empty.
#     """
#     mean = calculate_average(numbers)
#     if mean is None:
#         return None
#     variance = 0
#     for number in numbers:
#         variance += (number - mean) ** 2
#     variance /= len(numbers)
#     return variance ** 0.5

# def main():
#     """
#     Prompt the user to enter a list of numbers and calculate the standard deviation.

#     Returns:
#         None.
#     """
#     numbers = []
#     size = int(input("Size of population: "))
#     if size == 0:
#         print("Invalid population")
#         return
#     for i in range(size):
#         number = int(input(f"Enter number {i + 1}: "))
#         numbers.append(number)
#     standard_deviation = calculate_standard_deviation(numbers)
#     if standard_deviation is not None:
#         print("Expected output:", round(standard_deviation, 2))

# if __name__ == "__main__":
#     main()




# QUESTION2
# def input_occupants():
#     """
#     Prompt the user to enter the number of houses with different numbers of occupants.

#     Returns:
#         list: A list of integers representing the number of houses with different numbers of occupants.
#     """
#     occupants = []
#     for i in range(8):
#         while True:
#             try:
#                 num_houses = int(input(f"Enter the number of houses with {i} occupants: "))
#                 if num_houses >= 0:
#                     break
#                 else:
#                     print("Please enter a non-negative integer for the number of houses.")
#             except ValueError:
#                 print("Invalid input. Please enter a valid non-negative integer.")
#         occupants.append(num_houses)
#     return occupants

# def calculate_percentage(numbers, total, number):
#     """
#     Calculate the percentage of a number in a list of numbers.

#     Args:
#         numbers (list): A list of numbers.
#         total (int): The total number of houses.
#         number (int): The number to calculate the percentage of.

#     Returns:
#         float: The percentage of the number in the list of numbers.
#     """
#     percentage = (number * 100) / total
#     return percentage

# def main():
#     occupants = input_occupants()
#     total_houses = sum(occupants)
    
#     print("Occupants  0  1  2  3  4  5  6  >6")
#     print("No. dwellings  ", end="")
    
#     for i in range(7):
#         print(f"{occupants[i]}  ", end="")
#     print(f">6")
    
#     print("Percentage   ", end="")
#     for num_houses in occupants:
#         percentage = calculate_percentage(occupants, total_houses, num_houses)
        
#         print(f"{percentage:.1f}%  ", end="")
#     print()

# if __name__ == "__main__":
#     main()



# # QUESTION3
# import math

# def get_primes(n):
#     # Initialize the list of prime numbers with 2
#     primes = [2]
    
#     if n < 2:
#         return []  # If n is less than 2, there are no prime numbers to find
    
#     for num in range(3, n):
#         is_prime = True
#         sqrt_num = int(math.sqrt(num))  # Calculate the square root of the current number
        
#         # Check if the current number is divisible by any previously discovered prime numbers
#         for prime in primes:
#             if prime > sqrt_num:
#                 break  # No need to check factors larger than the square root of num
#             if num % prime == 0:
#                 is_prime = False
#                 break
        
#         if is_prime:
#             primes.append(num)  # If the current number is prime, add it to the list of primes
    
#     return primes

# while True:
#     try:
#         num = int(input("Enter a number greater than 2: "))
#         if num <= 2:
#             print("Please enter a number greater than 2.")
#         else:
#             break
#     except ValueError:
#         print("Invalid input. Please enter a valid whole number.")

# prime_numbers = get_primes(num)
# print("Prime numbers less than", num, ":")
# for prime in prime_numbers:
#     print(prime)



# # QUESTION4
# import math

# x1, y1 = 0, 0  # Initialize robot's current location at (0, 0)
# total_distance = 0
# step_counter = 0

# while True:
#     try:
#         x2 = int(input("Please insert destination X value: "))
#         y2 = int(input("Please insert destination Y value: "))
        
#         if x2 == 999 or y2 == 999:
#             break  # Exit the loop if the user inputs 999 for either x or y
        
#         # Calculate Euclidean distance and identify the direction of movement
#         distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
#         direction = ""
        
#         if y2 > y1:
#             direction += "Top "
#         elif y2 < y1:
#             direction += "Bottom "
        
#         if x2 > x1:
#             direction += "Right"
#         elif x2 < x1:
#             direction += "Left"
        
#         step_counter += 1
#         total_distance += distance
        
#         # Print the step information
#         print(f"Step {step_counter}: {distance:.2f} meters to {direction}")
        
#         # Update the current location for the next step
#         x1, y1 = x2, y2

#     except ValueError:
#         print("Invalid input. Please enter valid integer coordinates.")

# # Print the total distance traveled by the robot
# print("-----------------------------------------")
# print(f"Total distance (in meters) the robot has moved is: {total_distance:.2f}")
