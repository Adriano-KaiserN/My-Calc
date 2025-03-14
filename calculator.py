#code that Creates a simple Python program that asks the user to 
# input two numbers and a mathematical operation (addition, subtraction, multiplication, or division).
def calculator():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    choice = input("Enter choice (1/2/3/4): ")
    
    if choice == '1':
        print("Result:", num1 + num2)
    elif choice == '2':
        print("Result:", num1 - num2)
    elif choice == '3':
        print("Result:", num1 * num2)
    elif choice == '4':
        if num2 == 0:
            print("Error! Division by zero.")
        else:
            print("Result:", num1 / num2)
    else:
        print("Invalid input")

if __name__ == "__main__":
    calculator()
