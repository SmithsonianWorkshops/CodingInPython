## Addendum: More on conditionals and operators

During class, we had to rush through the information on conditionals. We are providing this addendum to give you further information on how to use them. We will also introduce a few new useful operators.

### Nested conditionals (if statements)

Sometimes it can be useful to nest an `if` statement inside another. As an example, imagine that I want to check if a string is fewer than 10 characters, but I also want to check if particular characters are in that string and then conduct different operations based on particular characters that may or may not be in the string. Here is some example code to portray what I’m talking about:

```python
response = input("Please enter your last name: \n")

if len(response) < 10:
    if 'a' in response:
        print("Congratulations, your last name is fewer than 10 characters and"
            + " contains an a!")
    elif 'b' in response:
        print("Congratulations, your last name is fewer than 10 characters and"
            + " doesn't contain an a, but it does contain a b!")
    elif 'c' in response:
        print("Congratulations, your last name is fewer than 10 characters and"
            + " doesn't contain an a or a b, but it does contain a c!")
    elif 'd' in response or 'e' in response:
        print("Congratulations, your last name is fewer than 10 characters and"
            + " doesn't contain an a b or c, but it does contain d or e!")       
    else:
        print("I'm sorry, your last name is fewer than 10 characters, but it "
            + " doesn't contain an a, b, or c.")
else:
    print("I'm sorry, your name has 10 or more characters.")
```

In the code above, I am doing two things:

1. I am checking to see if the user's last name is fewer than 10 characters long.
2. Given that the string is fewer than 10 characters long, I am then checking for characters in the string to find out some important features about the user's last name.

Note that one `if` statement is inside the other. This is perfectly fine and can be a powerful way to figure out information about some input.

### Equality operators

In this example, I also use a new operator, the `<` operator. It works much like you might imagine. It allows you to determine whether one operand is "less than" the other. Similarly, you can use `>` for "greater than", `<=` for "less than or equal to", `>=` for "greater than or equal to", `==` for "equal to", and `!=` for "not equal to". This can be very useful when you are looking for a particular input. For example, you could do something like:

```python
yes_or_no = input("Do you like Python? Please enter [yes/no]")
```

Then you can check whether they correctly answered yes or no or other with an if/elif/else statement:

```python
if yes_or_no == 'yes':
    <do_something>
elif yes_or_no == 'no':
    <do_something>
else:
    print("Your input is invalid, you didn’t enter yes or no")
```

### Combination operators

You can also combine mulitple conditional statements together using the terms `and`, `or`, and `not`. 

You can see this in the 3rd elif statement in the last name example above. The statement checks to see if either a 'd' OR an 'e' are in the last name. With `or` statments, they evaluate to `True` even if both conditions are met. For example, if a 'd' is found in the last name, then the program will print the statement right away -- even if there is also an 'e' or more 'd's.

Another example can be seen in the first `if` statement of the [Week 2 Homework Skeleton](https://github.com/SmithsonianWorkshops/CodingInPython/blob/master/Week%202/week_2_homework.py): 

```python
#Next, we check that both of the numbers are actually integers.
if first_number.isnumeric() and second_number.isnumeric():
```

As we saw during class, trying to convert a non-numeric string to an integer causes an error, so we need to make sure that both input numbers are numeric. We use the `and` operator to do this.
