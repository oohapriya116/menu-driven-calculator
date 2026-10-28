def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def main():
    while True:
        print("1. Addition")
        print("2. Subtraction")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Result:", add(a, b))
        elif choice == "2":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Result:", subtract(a, b))
        elif choice == "3":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()