#question
# Task
# Given an integer, , perform the following conditional actions:

# If n is odd, print Weird
# If n is even and in the inclusive range2to5 of  to , print Not Weird
# If n is even and in the inclusive range6 of 20 to , print Weird
# If n is even and greater than , print Not Weird
# Input Format

# A single line containing a positive integer, .

# Constraints

# Output Format

# Print Weird if the number is weird. Otherwise, print Not Weird.

#answer

# if __name__ == '__main__':
#     n = int(input().strip())
#     if n % 2 != 0:
#         print('Weird')
#     elif n % 2 ==0 and n in range(2, 6):
#         print('Not Weird')
#     elif n % 2 ==0 and n in range(6, 21):
#         print('Weird')
#     elif n % 2 == 0 and n > 20:
#         print('Not Weird')

#question
# Consider a list (list = []). You can perform the following commands:

# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of n followed by  lines of commands where each command will be of the 7 types listed above.
# Iterate through each command in order and perform the corresponding operation on your list.

#SOLUTION
N = int(input())
list1 = []
for i in range(N):
        command = input().lower().split()
        if command[0] == 'insert':
            list1.insert(int(command[1]), int(command[2] ))
        elif command[0] == 'print':
            print(list1)
        elif command[0] == 'remove':
            list1.remove(int(command[1]))
        elif command[0] == 'append':
            list1.append(int(command[1]))
        elif command[0] == 'sort':
            list1.sort()
        elif command[0] == 'pop':
            list1.pop()
        elif command[0] == 'reverse':
            list1.reverse()