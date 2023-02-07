# Simple Calculator

try:
    while True:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        print("""
        *** Enter your choice ***
        +, -, * /
        """)

        choice = input("Enter your choice: ")

        if choice == "+":
            print(f"The addition of {a} and {b} is {a+b}")

        elif choice == "-":
            print(f"The subtraction of {a} and {b} is {a-b}")

        elif choice == "*":
            print(f"The multiplication of {a} and {b} is {a*b}")

        elif choice == "/":
            print(f"The divison of {a} and {b} is {a/b}")

        else:
            print("Invalid Choice !!!")
            break
except Exception as e:
    print(e)
