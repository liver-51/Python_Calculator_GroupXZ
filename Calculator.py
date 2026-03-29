def add(x, y):
    """Return the sum of two numbers."""
    return x + y

def subtract(x, y):
    """Return the difference of two numbers (x - y)."""
    return x - y

def multiply(x, y):
    """Return the product of two numbers."""
    return x * y

def divide(x, y):
    """Return the quotient of two numbers (x / y). Handles division by zero."""
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return x / y

def main():
    print("===== Python Calculator =====")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        # Get user's choice of operation
        choice = input("\nEnter choice (1/2/3/4): ")

        # Validate operation choice
        if choice not in ('1', '2', '3', '4'):
            print("❌ Invalid choice! Please select from 1, 2, 3, or 4.")
            continue

        # Get and validate input numbers
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("❌ Invalid input! Please enter valid numbers only.")
            continue

        # Perform calculation based on user choice
        try:
            if choice == '1':
                result = add(num1, num2)
                print(f"✅ {num1} + {num2} = {result}")
            elif choice == '2':
                result = subtract(num1, num2)
                print(f"✅ {num1} - {num2} = {result}")
            elif choice == '3':
                result = multiply(num1, num2)
                print(f"✅ {num1} * {num2} = {result}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"✅ {num1} / {num2} = {result}")
        except ZeroDivisionError as e:
            print(f"❌ Error: {e}")
            continue

        # Ask user if they want to perform another calculation
        while True:
            next_calculation = input("\nWould you like to perform another calculation? (yes/no): ").strip().lower()
            if next_calculation in ('yes', 'no'):
                break
            print("❌ Please enter 'yes' or 'no' only.")

        if next_calculation == 'no':
            print("👋 Thank you for using the calculator! Goodbye.")
            break

if __name__ == "__main__":
    main()
