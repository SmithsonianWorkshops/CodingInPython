# This program will act as a basic calculator. It will ask the user for 2
# integers, and an operation to perform.

# First, we use the input() function to request for 2 numbers and an operation.
operation = input("Choose whether you want to add, subtract, multiply or divide: ")
first_number = input("Please enter the first number you wish to " + operation + ":")
second_number = input("Please enter the second number you wish to " + operation + ":")

# Next, we check that both of the numbers are actually integers.
if first_number.isnumeric() and second_number.isnumeric():
    # Next, we must convert both of these numbers to integers, since input() 
    # defaults to accepting strings.
    first_number = int(first_number)
    second_number = int(second_number)

    if operation == 'add':
        answer = first_number + second_number

    elif opration == 'multiply':
        answer = first_number * second_number

    ### You need to fill in the rest of the operations, and print an error if
    ### their entry for operation isn't from our list.

    ### You also need to figure out the correct location to report back the 
    ### answer.


### You need to print an error message if their numbers are not integers.