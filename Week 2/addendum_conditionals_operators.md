## Addendum: More on conditionals and operators

During class, we had to rush through the information on conditionals. We are providing this addendum to give you further information on how to use them. We will also introduce a few new useful operators.

#### Nested conditionals (if statements)

Sometimes it can be useful to nest an `if` statement inside another. As an example, imagine that I want to check if a string is fewer than 10 characters, but I also want to check if particular characters are in that string and then conduct different operations based on particular characters that may or may not be in the string. Here is some example code to portray what I’m talking about:

```
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

#### New operators

In this example, I also use a new operator, the `<` operator. It works much like you might imagine. It allows you to determine whether one operand is "less than" the other. Similarly, you can use `>` for "greater than", `<=` for "less than or equal to", `>=` for "greater than or equal to", `==` for "equal to", and `!=` for "not equal to". This can be very useful when you are looking for a particular input. For example, you could do something like:

```
yes_or_no = input("Do you like Python? Please enter [yes/no]")
```

Then you can check whether they correctly answered yes or no or other with an if/elif/else statement:

```
if yes_or_no == 'yes':
    <do_something>
elif yes_or_no == 'no':
    <do_something>
else:
    print("Your input is invalid, you didn’t enter yes or no")
```