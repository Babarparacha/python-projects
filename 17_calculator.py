def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divided(x, y):
    if y == 0:
        return "error! division by zero is not possible"
    return x / y

def main():
    print("Select an operation:")
    print("1 for addition")
    print("2 for subtraction")
    print("3 for multiplication")
    print("4 for division")
    
    while True:
        choice = input('Enter a number (1-4) to get the result: ')
        
        if choice not in ['1', '2', '3', '4']:
            print("Invalid input! Please enter a valid input.")
        else:
            break
        
    try:
        num1 = float(input("Enter first number: "))    
        num2 = float(input("Enter second number: "))    
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return
    
    if choice == "1":
        print(f"{num1} + {num2} = {add(num1, num2)}")    
    elif choice == "2":
        print(f"{num1} - {num2} = {subtract(num1, num2)}")    
    elif choice == "3":
        print(f"{num1} * {num2} = {multiply(num1, num2)}")    
    elif choice == "4":
        print(f"{num1} / {num2} = {divided(num1, num2)}")    

main()
