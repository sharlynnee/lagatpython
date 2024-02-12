n1 = float(input("Enter the first number:"))
n2 = float(input("Enter the Second Number:"))

operator = input("Enter operator:")

if operator == "+":
    print("Result is: ",n1+n2)
elif operator == "-":
    print("Result is: ",n1-n2)
elif operator == "*":
    print("Result is: ",n1*n2)
elif operator == "/":
    print("Result is: ",n1/n2)
else:
    print("Invalid operator")

