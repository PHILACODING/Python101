# Define the functions needed: add, sub, mul, div
# Print option to the user
# Ask for values
# Call the functions
# While loop to continue the program until the user wants to exit.

def add(a, b):
    answer = sum((a,b))
    #print( str(a) + " + " + str(b) + " = " + str(answer))
    print(f"\n {a} + {b} = { answer}\n")


def sub(a, b):
    answer = a -b
    print(f"\n {a} - {b} = { answer}\n")


def mul(a, b):
    answer = a * b
    print(f"\n{a} * { b} = {answer}\n")

def div(a, b):
    answer = a / b
    print(f"\n{a} / { b} = {answer}\n")

while True:
    print("\nWhat would you like to do?")
    print('A. Addition')
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print('E. Exit\n')

    choice = input("Please enter your choice: ")

    if choice == "a" or choice == 'A':
        print('Addition')
        a = int(input('Enter your first number: '))
        b = int(input("Enter your second number: "))
        add(a,b)

    elif choice == "b" or choice == "B":
        print('Subtraction')
        a = int(input('Enter your first number: '))
        b = int(input("Enter your second number: "))
        sub(a,b)

    elif choice == 'c' or  choice == "C":
        print('Multiplication')
        a = int(input('Enter your first number: '))
        b = int(input("Enter your second number: "))
        mul(a,b)

    elif choice =='d' or choice == "D":
        print("Division")
        a = int(input('Enter your first number: '))
        b = int(input("Enter your second number: "))
        div(a,b)

    elif choice == 'e' or choice == "E":
        print("\nProgram ended" )
        quit()

    


