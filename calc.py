user_input = input("The operation you would like to use (+,-,*,/): ")
num1 = int(input("The users first number: "))
num2 = int(input("The users second number: "))

def add(num1, num2):
    return num1 + num2 

def minus(num1, num2):
    return num1 - num2

def mutiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2



if user_input == "+":
    print(add(num1, num2))
    
elif user_input == "-":
    print(minus(num1, num2))

elif user_input == "*":
    print(mutiply(num1, num2))

elif user_input == "/":
    print(divide(num1, num2))
    
else:
    print(f"The operator you give is not right {user_input}")

