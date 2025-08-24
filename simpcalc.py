x = int(input("Enter the First Operand: "))
y = int(input("Enter the Second Operand: "))
op = input("Enter the Operator: ")
if op=="+":
    print(f"The Addition of two numbers is {x+y}")
elif op=="-":
    print(f"The Subtraction of two numbers is {x-y}")
elif op=="*":
    print(f"The Multiplication of two numbers is {x*y}")
elif op=="/":
    print(f"The Division of two numbers is {x/y}")
elif op=="%":
    print(f"The Remainder of {x} divided by {y} is {x%y}")
elif op=="//":
    print(f"The Floor division of two numbers is {x//y}")