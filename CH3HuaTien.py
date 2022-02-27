# Name: Tien Hua
# Program: Chapter 3 – Selections
# Description: Enter a paragraph description of the program (at least 5 sentences in your own words)


TITLE = "Welcome to Mini Calculator Program" 
LINE = "----------------------------------"

# Print program title
print(LINE)
print(TITLE)
print(LINE)

# Example input prompt for firstNum and secondNum
firstNum = int(input("Enter first number: "))
secondNum = int(input("Enter second number: "))

# Example input prompt for Operations
print("Operations: +, -, *, **, /, //, %")
opSymbol = input("Select operation: ") # /
print(LINE)

# Perform the operations based on the user's choice
# Use if / elif / else
# Addition (+)
if opSymbol == "+":
    print(firstNum, "+", secondNum, "=", firstNum+secondNum)
    print(LINE)
# Subtraction (-)
elif opSymbol == "-":
    print(firstNum, "-", secondNum, "=", firstNum-secondNum)
    print(LINE)
# Multiplication (*) 
elif opSymbol == "*":
    print(firstNum, "*", secondNum, "=", firstNum*secondNum)
    print(LINE)
# Exponentiation (**) 
elif opSymbol == "**":
    print(firstNum, "**", secondNum, "=", firstNum**secondNum)
    print(LINE)
# Division (/) 
elif opSymbol == "/":
    # Check the secondNum is zero or not
    if secondNum != 0:
        print(firstNum, "/", secondNum, "=", firstNum/secondNum)
        print(LINE)
    else:
        # Division by zero erro
        print("DIVISION BY ZERO ERRO")
        print(LINE)
# Floor division (//) 
elif opSymbol == "//":
    # Check the secondNum is zero or not
    if secondNum != 0:
        print(firstNum, "//", secondNum, "=", firstNum//secondNum)
        print(LINE)
    else:
        # Division by zero erro
        print("DIVISION BY ZERO ERRO")
        print(LINE)
# Modulus (%) 
elif opSymbol == "%":
    # Check the secondNum is zero or not
    if secondNum > 0:
        print(firstNum, "%", secondNum, "=", firstNum%secondNum)
        print(LINE)
    else:
        # Division by zero erro
        print("DIVISION BY ZERO ERRO")
        print(LINE)

else:
    # If the operator is other than +, -, * or /, error message is shown
    #  Invalid operator error
    print(opSymbol, "IS AN INVALID OPERATOR")
    print(LINE)

