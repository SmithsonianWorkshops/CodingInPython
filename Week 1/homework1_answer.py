#We use the input() function to request for 2 numbers
first_number = input("What is the first number to add? ")
second_number = input("What is the second number to add? ")

#Next, we must convert both of these numbers to integers, since input() 
#defaults to accepting strings.
first_number = int(first_number)
second_number = int(second_number)

#Next, we add the 2 numbers together, and save that to the variable 
#sum_of_numbers. Note that variable name "sum" is a reserved Python word, so we
#cannot use that as our variable name.
sum_of_numbers = int(first_number) + int(second_number)

#Finally, we print sum_of_numbers so that the user can see the answer.
print(sum_of_numbers)