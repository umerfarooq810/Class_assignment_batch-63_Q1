

# 3-1. Names: Store the names of a few of your friends in a list called names . Print 
# each person’s name by accessing each element in the list, one at a time 


# First pattern.

names_list = ["Umer Farooq", "Umer Khalil", "Ali Bhai", "Ammar Yasir", "M.bilal"]
print("Your name is :" + names_list[0])
print("Your name is :" + names_list[1])
print("Your name is :" + names_list[2])
print("Your name is :" + names_list[3])
print("Your name is :" + names_list[4])

# Second pattern.

names_list_2 = ["Umer Farooq", "Umer Khalil", "Ali Bhai", "Ammar Yasir", "M.bilal"]
for name in names_list_2:
    print(name)


# 3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just 
# printing each person’s name, print a message to them . The text of each messages
# should be the same, but each message should be personalized with the person’s name.
 

greet_mess = ["Sir Zia Khan", "Sir Rehan", "Sir Muzhar", "Sir Usman"]

for name in greet_mess:
    print(f"Hello G, {name}! Hope you're having a great day!")


# 3-3. Your Own List: Think of your favorite mode of transportation, such as a 
# motorcycle or a car, and make a list that stores several examples . Use your list 
# to print a series of statements about these items, such as “I would like to own a 
# Honda motorcycle .”


transportations = ["Honda motorcycle", "Tesla car", "Yamaha bike", "BMW car"]

for transportation in transportations:
    print(f"I would like to own a {transportation}")


# 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who 
# would you invite? Make a list that includes at least three people you’d like to 
# invite to dinner . Then use your list to print a message to each person, inviting them to dinner.


# guests = ["Umer", "Qasim", "Shoaib"]

# for guest in guests:
#     print(f"Dear {guest}, I would be honored to have you join me for dinner.")


# 3-5. Changing Guest List: You just heard that one of your guests can’t make the 
# dinner, so you need to send out a new set of invitations . You’ll have to think of someone else to invite .
# • Start with your program from Exercise 3-4 . Add a print statement at the end of your program stating the name of the guest who can’t make it .
# • Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting .
# •	Print a second set of invitation messages, one for each person who is still in your list.


guests = ["Umer", "Qasim", "Shoaib"]

for guest in guests:
    print(f"Dear {guest}, I would be honored to have you join me for dinner.")

unavailable_guest = "Shoaib"
print(f"\nUnfortunately, {unavailable_guest} can't make it to dinner.")

guests[2] = "Subhan"

print("\nSending out new invitations:")
for guest in guests:
    print(f"Dear {guest}, I would be honored to have you join me for dinner.")


# 3-6. More Guests: You just found a bigger dinner table, so now more space is 
# available . Think of three more guests to invite to dinner .
#  •    Start with your program from Exercise 3-4 or Exercise 3-5 . Add a print statement to the end of your
#       program informing people that you found a bigger dinner table .
#  •	Use insert() to add one new guest to the beginning of your list .
#  •	Use insert() to add one new guest to the middle of your list .
#  •	Use append() to add one new guest to the end of your list .
#  •	Print a new set of invitation messages, one for each person in your list 


guests = ["Umer", "Qasim", "Shoaib"]

print("Good news! I found a bigger dinner table, so I can invite more people to dinner.\n")


guests.insert(0, "Hassan Bhai")       
guests.insert(2, "Ali Bhai")    
guests.append("Hammad")         

for guest in guests:
    print(f"Dear {guest}, I would be honored to have you join me for dinner.")


# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time 
# for the dinner, and you have space for only two guests .
#  •	Start with your program from Exercise 3-6 . Add a new line that prints a message saying that
#       you can invite only two people for dinner .
#  •	Use pop() to remove guests from your list one at a time until only two names remain in your list .
#       Each time you pop a name from your list, print a message to that person letting them know you’re
#       sorry you can’t invite them to dinner .
#  •	Print a message to each of the two people still on your list, letting them know they’re still invited .
#  •	Use del to remove the last two names from your list, so you have an empty list . Print your list to make sure
#       you actually have an empty list at the end of your program .
 

guests = ["umer", "Qasim", "Shoaib", "Subhan", "Hassan Bhai", "Ali Bhai"]

print("Unfortunately, the new dinner table won't arrive in time. I can only invite two people for dinner.\n")

removed_guest = guests.pop()
print(f"Sorry, {removed_guest}, I can't invite you to dinner.")

removed_guest = guests.pop() 
print(f"Sorry, {removed_guest}, I can't invite you to dinner.")

removed_guest = guests.pop()
print(f"Sorry, {removed_guest}, I can't invite you to dinner.")

removed_guest = guests.pop()
print(f"Sorry, {removed_guest}, I can't invite you to dinner.")

print(f"Dear {guests[0]}, you're still invited to dinner.")
print(f"Dear {guests[1]}, you're still invited to dinner.")

del guests[0]  
del guests[0]  

print("\nFinal guest list:", guests)


# 3-8. Seeing the World: Think of at least five places in the world you’d like to visit .
#  •	Store the locations in a list . Make sure the list is not in alphabetical order .
#  •	Print your list in its original order . Don’t worry about printing the list neatly, just print it as a raw Python list .
#  •	Use sorted() to print your list in alphabetical order without modifying the actual list . 
#  •	Show that your list is still in its original order by printing it .
#  •	Use sorted() to print your list in reverse alphabetical order without chang ing the order of the original list .
#  •	Show that your list is still in its original order by printing it again .
#  •	Use reverse() to change the order of your list . Print the list to show that its order has changed .
#  •	Use reverse() to change the order of your list again . Print the list to show it’s back to its original order . 
#  •	Use sort() to change your list so it’s stored in alphabetical order . Print the list to show that its order has been changed .
#  •	Use sort() to change your list so it’s stored in reverse alphabetical order . 
#       Print the list to show that its order has changed 


places = ["Pakistan", "Japan", "Norway", "New Zealand", "Brazil", "Iceland"]
print("Original list:", places)

print("Alphabetical order:", sorted(places))

print("Original list after sorted():", places)

print("Reverse alphabetical order:", sorted(places, reverse=True))

print("Original list after reverse sorted():", places)

places.reverse()
print("List after reverse():", places)

places.reverse()
print("List after reversing again:", places)

places.sort()
print("List after sort():", places)

places.sort(reverse=True)
print("List after sort(reverse=True):", places)


# 3-9. Dinner Guests: Working with one of the programs from Exercises 3-4 through 3-7 (page 46),
# use len() to print a message indicating the number of people you are inviting to dinner. 
 

guests = ["umer", "Qasim", "Shoaib"]

print(f"I am inviting {len(guests)} people to dinner.")


# 3-10. Every Function: Think of something you could store in a list . For example, you could make a list of mountains, 
# rivers, countries, cities, languages, or any thing else you’d like . Write a program that creates a list containing 
# these items and then uses each function introduced in this chapter at least once.
 

cities = ["Paris", "Tokyo", "New York", "London", "Sydney"]

print("Original list:", cities)

print("Number of cities:", len(cities))

print("Cities in alphabetical order:", sorted(cities))

print("Original list after sorted():", cities)

print("Cities in reverse alphabetical order:", sorted(cities, reverse=True))

print("Original list after reverse sorted():", cities)

cities.reverse()
print("List after reverse():", cities)

cities.reverse()
print("List after reversing again:", cities)

cities.sort()
print("List after sort():", cities)

cities.sort(reverse=True)
print("List after sort(reverse=True):", cities)

cities.append("Barcelona")
print("List after append():", cities)

cities.insert(2, "Berlin")
print("List after insert():", cities)

removed_city = cities.pop()
print(f"Removed city: {removed_city}")
print("List after pop():", cities)

del cities[1]
print("List after del():", cities)

cities.clear()
print("List after clear():", cities)

# 3-11. Intentional Error: If you haven’t received an index error in one of your 
# programs yet, try to make one happen . Change an index in one of your programs
# to produce an index error . Make sure you correct the error before closing the program. 


# fruits = ["Apple", "Banana", "Cherry"]

# # This will cause an IndexError
# print(fruits[5]) 

fruits_1 = ["Apple", "Banana", "Cherry"]

# Correctly access an index within the range of the list
print(fruits_1[1]) 
