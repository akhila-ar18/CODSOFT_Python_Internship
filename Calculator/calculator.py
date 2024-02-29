# Addition Operation
def add(a, b):
    return a + b

# Subtraction Operation
def subtract(a, b):
    return a - b

# Multiplication Operation
def multiply(a, b):
    return a * b

# Division Operation
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

print("\n        CALCULATOR ")
print("*****************************")
print("Select an operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("*****************************")

while True:
    choice = input("Enter your choice: ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
        else:
            print("Invalid choice. Please enter a valid choice between 1 and 5.")

    repeat = input("Do you want to perform another calculation? (yes/no): ")
    if repeat.lower() != 'yes':
        print("Exiting...")
        break
