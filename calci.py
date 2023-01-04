#   HOW TO BUILD A SIMPLE CALCULATOR IN PYTHON 


# 1. ADD
# 2. SUBTRACT
# 3. MULTIPLY
# 4. DIVIDE


print("select an operation to perform: ")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")

operation = input()


if opration == "1":
    num1 = input("enter first number: ")
    num2 = input("enter second number: ")
    print("the sum is " + str(int(num1) + int(num2)))
elif opration == "2":
    num1 = input("enter first number: ")
    num2 = input("enter second number: ")
    print("the difference is " + str(int(num1) - int(num2)))
elif opration == "3":
    num1 = input("enter first number: ")
    num2 = input("enter second number: ")
    print("the product is " + str(int(num1) * int(num2)))
elif opration == "4":
    num1 = input("enter first number: ")
    num2 = input("enter second number: ")
    print("the result is " + str(int(num1) / int(num2)))
else:
    print("invalid entry")
