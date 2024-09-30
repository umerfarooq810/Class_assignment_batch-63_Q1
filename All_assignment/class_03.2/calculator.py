



def calculator():
    
    print("Welcome to the calculator!")
    print("please select an operation:")
    print("1. Addition")
    print("2. subtraction")
    print("3. multiplication")
    print("4. division")

    choice = input("enter your choice (1-4):")

    num1 = float(input("enter the first  number:"))
    num2 = float(input("enter the second number:"))

    if choice == '1':
        result = num1 + num2
        print("result:", result)

    elif choice == '2':
        result = num1 - num2
        print("result:", result)

    elif choice == '3':
        result = num1 * num2
        print("result:", result)

    elif choice == '4':
        if num2 == 0:
            print("Error:Division by zero")
        else:
            result = num1 / num2
            print("result:", result)
    else:
        print("Invalid choice. Please try again")

calculator()