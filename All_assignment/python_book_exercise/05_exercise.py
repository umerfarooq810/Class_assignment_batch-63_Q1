

# # 5-1. Conditional Tests: Write a series of conditional tests . Print a statement describing each test 
# # and your prediction for the results of each test . Your code should look something like this: 

print("Is 10 greater than 5? I predict True.")
print(10 > 5)

print("\nIs 7 less than 3? I predict False.")
print(7 < 3)

word = "hello"
print("\nIs the word equal to 'hello'? I predict True.")
print(word == "hello")

print("\nIs the word not equal to 'world'? I predict True.")
print(word != "world")

print("\nIs 8 greater than or equal to 8? I predict True.")
print(8 >= 8)

print("\nIs 15 less than or equal to 10? I predict False.")
print(15 <= 10)

language = "Python"
print("\nIs 'Python' not equal to 'python'? I predict True.")
print(language != "python")

print("\nIs 3 + 2 equal to 5? I predict True.")
print((3 + 2) == 5)

fruits = ['apple', 'banana', 'orange']
print("\nIs 'apple' in the list of fruits? I predict True.")
print('apple' in fruits)

print("\nIs 'grape' not in the list of fruits? I predict True.")
print('grape' not in fruits)


# #  5-2. More Conditional Tests: You don’t have to limit the number of tests you create to 10 .
# #       If you want to try more comparisons, write more tests and add them to conditional_tests.py . 
# #       Have at least one True and one False result for each of the following:

# #  •	Tests for equality and inequality with strings
# #  •	Tests using the lower() function
# #  •	Numerical tests involving equality and inequality, greater than and less than, 
# #       greater than or equal to and less than or equal to
# #  •	Tests using the and keyword and the or keyword
# #  •	Test whether an item is in a list
# #  •	Test whether an item is not in a list  


# # Tests for equality and inequality with strings
string1 = "Hello"
string2 = "World"
print("Test 1: Is string1 == 'Hello'? I predict True.")
print(string1 == "Hello")

print("\nTest 2: Is string2 != 'World'? I predict False.")
print(string2 != "World")

# # Tests using the lower() function
name = "Alice"
print("\nTest 3: Is name.lower() == 'alice'? I predict True.")
print(name.lower() == 'alice')

print("\nTest 4: Is name.lower() == 'bob'? I predict False.")
print(name.lower() == 'bob')

# # Numerical tests involving equality, inequality, greater than, less than, etc.
num1 = 10
num2 = 20
print("\nTest 5: Is num1 == 10? I predict True.")
print(num1 == 10)

print("\nTest 6: Is num1 != 10? I predict False.")
print(num1 != 10)

print("\nTest 7: Is num2 > num1? I predict True.")
print(num2 > num1)

print("\nTest 8: Is num1 >= 15? I predict False.")
print(num1 >= 15)

# # Tests using the 'and' keyword and 'or' keyword
age = 25
print("\nTest 9: Is age > 20 and age < 30? I predict True.")
print(age > 20 and age < 30)

print("\nTest 10: Is age < 20 or age > 30? I predict False.")
print(age < 20 or age > 30)

# # Test whether an item is in a list
fruits = ['apple', 'banana', 'orange']
print("\nTest 11: Is 'banana' in fruits? I predict True.")
print('banana' in fruits)

print("\nTest 12: Is 'grape' in fruits? I predict False.")
print('grape' in fruits)

# # Test whether an item is not in a list
print("\nTest 13: Is 'mango' not in fruits? I predict True.")
print('mango' not in fruits)

print("\nTest 14: Is 'apple' not in fruits? I predict False.")
print('apple' not in fruits)


# #  5-3.Alien Colors #1: Imagine an alien was just shot down in a game.Create a variable called 
# #  alien_color and assign it a value of 'green', 'yellow', or 'red'.

# #  •	Write an if statement to test whether the alien’s color is green.If it is, print
# #       a message that the player just earned 5 points .
# #  •	Write one version of this program that passes the if test and another that fails. 
# #       (The version that fails will have no output.)


# # Version 1: The if test passes (alien color is green)
alien_color = 'green'
if alien_color == 'green':
    print("The player just earned 5 points!")

# Version 2: The if test fails (alien color is not green)
alien_color = 'yellow'
if alien_color == 'green':
    print("The player just earned 5 points for encountering a yellow alien!")


# 5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and write an 
# if-else chain .
#  •	If the alien’s color is green, print a statement that the player just earned 5 points 
#       for shooting the alien .  
#  •	If the alien’s color isn’t green, print a statement that the player just earned 10 points .
#  •	Write one version of this program that runs the if block and another that runs the else block.


# Version 1: The if block runs (alien color is green) 
alien_color = 'green'

if alien_color == 'green':
    print("The player just earned 5 points for shooting the alien!")
else:
    print("The player just earned 10 points!")

# Version 2: The else block runs (alien color is not green)
alien_color = 'red'

if alien_color == 'green':
    print("The player just earned 5 points for shooting the alien!")
else:
    print("The player just earned 10 points!")


# 5-5.Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif else chain . 

#  •  If the alien is green, print a message that the player earned 5 points .
#  •  If the alien is yellow, print a message that the player earned 10 points .
#  •  If the alien is red, print a message that the player earned 15 points .
#  •  Write three versions of this program, making sure each message is printed 
#     for the appropriate color alien.


# Version 1: The alien is green (5 points)
alien_color = 'green'

if alien_color == 'green':
    print("The player earned 5 points!")
elif alien_color == 'yellow':
    print("The player earned 10 points!")
elif alien_color == 'red':
    print("The player earned 15 points!")

# Version 2: The alien is yellow (10 points)
alien_color = 'yellow'

if alien_color == 'green':
    print("The player earned 5 points!")
elif alien_color == 'yellow':
    print("The player earned 10 points!")
elif alien_color == 'red':
    print("The player earned 15 points!")

# Version 3: The alien is red (15 points)
alien_color = 'red'

if alien_color == 'green':
    print("The player earned 5 points!")
elif alien_color == 'yellow':
    print("The player earned 10 points!")
elif alien_color == 'red':
    print("The player earned 15 points!")


# # 5-6.Stages of Life: Write an if-elif-else chain that determines a person’s stage of life . 
# # Set a value for the variable age, and then:
# # •	If the person is less than 2 years old, print a message that the person is a baby .
# # •	If the person is at least 2 years old but less than 4, print a message that the person is a toddler .  
# # •	If the person is at least 4 years old but less than 13, print a message that the person is a kid .
# # •	If the person is at least 13 years old but less than 20, print a message that the person is a teenager .
# # •	If the person is at least 20 years old but less than 65, print a message that the person is an adult .
# # •	If the person is age 65 or older, print a message that the person is an elder. 


age = 17

if age < 2:
    print("The person is a baby.")
elif age >= 2 and age < 4:
    print("The person is a toddler.")
elif age >= 4 and age < 13:
    print("The person is a kid.")
elif age >= 13 and age < 20:
    print("The person is a teenager.")
elif age >= 20 and age < 65:
    print("The person is an adult.")
else:
    print("The person is an elder.")


# # 5-7.  Favorite Fruit: Make a list of your favorite fruits, and then write a series of independent
# # if statements that  check for certain fruits in your list .

# # •	Make a list of your three favorite fruits and call it favorite_fruits .
# # •	Write five if statements . Each should check whether a certain kind of fruit is in your list . 
# #   If the fruit is in your  list, the if block should print a statement, such as You really like bananas! 


favorite_fruits = ['apple', 'banana', 'mango']

if 'apple' in favorite_fruits:
    print("You really like apples!")

if 'banana' in favorite_fruits:
    print("You really like bananas!")

if 'strawberry' in favorite_fruits:
    print("You really like strawberries!")

if 'mango' in favorite_fruits:
    print("You really like mangoes!")

if 'grape' in favorite_fruits:
    print("You really like grapes!")


# # 5-8. Hello Admin: Make a list of five or more usernames, including the name 'admin'.Imagine you are
# # writing code that will print a greeting to each user after they log in to a website . Loop through
# # the list, and print a greeting to each user:
# # •	If the username is 'admin', print a special greeting, such as Hello admin, would you like to
# #   see a status report?  
# # •	Otherwise, print a generic greeting, such as Hello Eric, thank you for logging in again. 

usernames = ['Admin', 'Umer', 'Aoun', 'Umair', 'Ammar']

for username in usernames:
    if username == 'Admin':
        print("Hello Admin, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in again.")


#  5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is not empty .

#  •	If the list is empty, print the message We need to find some users!
#  •	Remove all of the usernames from your list, and make sure the correct message is printed.


usernames = ['admin', 'john', 'jane']
usernames.clear()

if not usernames:
    print("We need to find some users!")
else:
    for username in usernames:
        print(f"Hello {username}, welcome back!")
print()


# 5-10. Checking Usernames: Do the following to create a program that simulates how websites ensure that 
# everyone has a unique username. 
# •	Make a list of five or more usernames called current_users .
# •	Make another list of five usernames called new_users . Make sure one or two of the new usernames
#   are also in the current_users list .
# •	Loop through the new_users list to see if each new username has already been used . If it has, 
#   print a message that the person will need to enter a new username . If a username has not  been 
#   used, print a message saying that the username is available .
# •	Make sure your comparison is case insensitive . If 'John' has been used, 'JOHN' should not be 
#   accepted.


current_users = ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve']
new_users = ['alice', 'Frank', 'charlie', 'mitchel', 'Hannah']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Username '{new_user}' is already taken. Please choose a different username.")
    else:
        print(f"Username '{new_user}' is available.")


# 5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such as 1st or 2nd .
#  Most ordinal numbers end in th, except 1, 2, and 3 . 

# •	Store the numbers 1 through 9 in a list .
# •	Loop through the list .
# •	Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number.Your 
#   output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", and each result should be on a separate line.


numbers = list(range(1, 10))

for number in numbers:

    if number == 1:
        ordinal = f"{number}st"
    elif number == 2:
        ordinal = f"{number}nd"
    elif number == 3:
        ordinal = f"{number}rd"
    else:
        ordinal = f"{number}th"
    
    print(ordinal)
