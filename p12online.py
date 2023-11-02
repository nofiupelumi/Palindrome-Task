#Assignment Solution
# Define a function to generate a Fibonacci sequence
def fibonacci_sequence(n):
    # Check if n is less than or equal to 0
    if n <= 0:
        return "Input must be a positive integer"
    # Handle the base cases when n is 1 or 2
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]

    # Initialize the Fibonacci sequence with the first two numbers
    sequence = [0, 1]
    # Generate the sequence until it reaches the desired length (n)
    while len(sequence) < n:
        # Calculate the next number and add it to the sequence
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
    # Return the generated sequence
    return sequence

# Get user input for n
n = input("Enter a positive integer for the Fibonacci sequence: ")
# Check if the input is composed of digits (positive integer)
if n.isdigit():
    n = int(n)
    # Call the Fibonacci sequence function and store the result
    sequence = fibonacci_sequence(n)
    # Check if the result is a list (valid sequence) or an error message
    if isinstance(sequence, list):
        # Print the Fibonacci sequence
        print(sequence)
    else:
        # Print the error message
        print(sequence)
else:
    # Handle the case when the input is not a valid positive integer
    print("Invalid input. Please enter a positive integer.")