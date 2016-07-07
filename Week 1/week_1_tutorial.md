## Week 1 tutorial

This week, you will get started with your first Python program.

Open your text editor. In the text editor write:

```
print("Hello World!")
```

Now save the program to your desktop as ```HelloWorld.py```.

Open your terminal program and navigate to the directory where you saved the program. For example, on Mac, you would enter:

```
$ cd ~/Desktop
```

Now run your program:

```
$ python HelloWorld.py
```

The program should print ```Hello world!```

Congratulations, you have written your first Python program. Now we will do the same thing, but within the Python interpreter. To start the Python interpreter, simply issue the command:

```
$ python
```

Python should now be open and the terminal should look something like this:

```
Python 3.5.1 |Continuum Analytics, Inc.| (default, Jun 15 2016, 16:14:02) 
[GCC 4.2.1 Compatible Apple LLVM 4.2 (clang-425.0.28)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

Now we will do the same command that we did in our "Hello World!" program:

```
>>> print("Hello World!")
```

Again, Python will execute the instruction that you have given it, which is to print "Hello World!". 

Now you have experience executing commands from a script as well as executing commands from within the Python interpreter.

####Python as a calculator

Since you are within the Python interpreter now, go ahead and try to add a couple of numbers together. To do this, you will use an **operator**. In Python, there are many operators. They are used to do an "operation" on operands. For example in ```1+2 = 3```, ```1``` and ```2``` are operands and ```+``` is the operator. Let's go ahead and try using the addition operator ```+``` to add two numbers. Assuming you are still in the Python interpreter, go ahead and type in a number followed by the addition operator (```+```) and another number. When you press enter, Python will do the calculation and print out the result, e.g.:

```
Python 3.5.1 |Continuum Analytics, Inc.| (default, Jun 15 2016, 16:14:02) 
[GCC 4.2.1 Compatible Apple LLVM 4.2 (clang-425.0.28)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 5+4
9
>>>
```

Python also uses other operators, such as ```-``` for subtraction, ```*``` for multiplication, and ```/``` for division.

####Requesting input

In your Python program, you can request input. You do this with a built-in **function**. We will be discussing functions in depth later on in the course. For now, you should know that you can use a function to do something more complicated than a simple operator can do. In Python, you can identify a function because it usually includes a name, followed by parentheses. Today we will use a single built-in function called ```input()```. This function allows us to request input from the user.

Try it out by typing:

```
>>> input("What is your name?")
```

The program will ask you for your name. Feel free to enter it and see what happens.

Now try putting this command in a script. This time, we'll assign the output to a **variable**. We'll talk more about variables next week. For the purposes of this exercise, keep in mind that a variable holds information. In your text editor you would write something like this:

```
name = input("What is your name?")
```

In this case, the value of the input function will be assigned to the variable ```name```. If you want to print it out, you'll add another line that prints the variable. Notice that since it is a variable, I don't put quotes around it.

```
name = input("What is your name?")
print(name)
```

####Homework

Now that you know how to ask for input and have experience with the addition operator, you should have the tools to write a simple addition calculator.

For your homework, you will create a program that requests two numbers from the user and returns the sum of those numbers.

Good luck!


