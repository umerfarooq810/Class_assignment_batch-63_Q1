

# 2-1. Simple Message: Assign a message to a variable, and then print that message.

message = ("Hello python Crash Course readeer!")
print(message)

# 2-2. Simple Messages: Assign a message to a variable, and print that message. 
# Then change the value of the variable to a new message, and print the new 
# message

message1 = ("Hello World, Python!")
print(message1)
message1 = ("New Message Alert!")
print(message1)

# 2-3. Personal Message: Use a variable to represent a person’s name, and print 
# a message to that person. Your message should be simple, such as, “Hello Eric, 
# would you like to learn some Python today

name = ("Umer farooq")
print(f"Hello {name}, would you like to learn some Python today?")

# 2-4. Name Cases: Use a variable to represent a person’s name, and then print 
# that person’s name in lowercase, uppercase, and title case.

my_name = ("Umer Farooq")

print("lowercase:", my_name.lower())
print("uppercase:", my_name.upper())
print("titlecase:", my_name.title())

# 2-5. Famous Quote: Find a quote from a famous person you admire. Print the 
# quote and the name of its author. Your output should look something like the 
# following, including the quotation marks:

quote = "The only limit to our realization of tomorrow is our doubts of today."
author = "Franklin D. Roosevelt"

print(f'"{quote}" :- {author}')

# 2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, represent the famous 
# person’s name using a variable called famous_person. Then compose your message
# and represent it with a new variable called message. Print your message

famous_person = "Albert Einstein"
message = f'"Life is like riding a bicycle. To keep your balance, you must keep moving." - {famous_person}'
print(message)

famous_person = "Einstein:-" 
message = (famous_person)+ " " + "Life is like riding a bicycle. To keep your balance, you must keep moving" 
print(message)


# 2-7. Stripping Names: Use a variable to represent a person’s name, and 
# include some whitespace characters at the beginning and end of the name. 
# Make sure you use each character combination, "\t" and "\n", at least once.
#  Print the name once, so the whitespace around the name is displayed. 
# Then print the name using each of the three stripping functions, lstrip(), 
# rstrip(), and strip().


name = "\tUmer Farooq\n"

print("Original name with whitespace:")
print(name)

print("\nName after lstrip() (leading whitespace removed):")
print(name.lstrip())

print("\nName after rstrip() (trailing whitespace removed):")
print(name.rstrip())

print("\n\nName after strip() (leading and trailing whitespace removed):")
print(name.strip())


# 2-8. File Extensions: Python has a removesuffix() method that works exactly  
# like removeprefix(). Assign the value 'python_notes.txt' to a variable called 
# filename. Then use the removesuffix() method to display the filename without 
# the file extension, like some file browsers do.

filename = "python_notes.txt"
filename_without_extension = filename.removesuffix(".txt")
print(filename_without_extension)


# 2-9. Number Eight: Write addition, subtraction, multiplication, and division 
# operations that each result in the number 8. Be sure to enclose your operations 
# in print() calls to see the results. You should create four lines that look like this:


print(5 + 3)

print(10 - 2)

print(4 * 2)

print(16 / 2)


# 2-10. Favorite Number: Use a variable to represent your favorite number. Then, 
# using that variable, create a message that reveals your favorite number. Print 
# that message


favorite_number = 7
message = f"My favorite number is {favorite_number}."
print(message)


favourite_number = input("Enter your favourite number:-")
message = "your favourite number is " + (favourite_number) 

print(message)


# 2-11. Adding Comments: Choose two of the programs you’ve written, and 
# add at least one comment to each. If you don’t have anything specific to write 
# because your programs are too simple at this point, just add your name and the 
# current date at the top of each program file. Then write one sentence describing 
# what the program does.



# Program 1: Greeting Message


# Author: [Your Name]
# Date: [Current Date]
# This program prints a greeting message to the user.

# Define the greeting message
greeting = "Hello, welcome to the Python program!"

# Print the greeting message
print(greeting)

# Program 2: Simple Calculation

number1 = 5
number2 = 3

sum_result = number1 + number2

print("The sum of", number1, "and", number2, "is", sum_result)

