#Ask for user input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

#Perform operations
match operation:
    case '+':
        print(f"The result is: {num1 + num2}")
    case '-':
        print(f"The result is: {num1 - num2}")
    case '*':
        print(f"The result is: {num1 * num2}")
    case '/':
        if num2 != 0:
            print(f"The result is: {num1 / num2}")
        else:
            print("Error! Division by 0 not allowed")
    case _:
        print("Invalid operation!")
