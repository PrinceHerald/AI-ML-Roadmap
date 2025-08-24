inp = input("Enter Celsius or Fahrenheit: ")
if inp=="celsius":
    ce = float(input("Enter the Amount of Celsius: "))
    print(f"Celsius Converted to Fahrenheit is {(ce*(9/5))+32}")
elif inp=="fahrenheit":
    fa = float(input("Enter the Amount of Fahrenheit: "))
    print(f"fahrenheit Converted to Celsius is {(fa-32)*(5/9)}")