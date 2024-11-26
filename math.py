num1= float(input("Enter the first number: "))
num2= float(input("Enter the second number: "))
operation=input("Enter the operation (+, -, *, /): ") # type: ignore

# Perform the operation based on the user's input
if operation=="+":
    result=num1+num2
    print(f"{num1}+{num2}={result}")
elif operation=="-":
    result=num1-num2
    print(f"{num1}-{num2}={result}")
elif operation=="*":
    result=num1*num2
    print(f"{num1}*{num2}={result}")
elif operation=="/":
    if num2!=0:
     result=num1/num2
     print(f"{num1}/{num2}={result}")
    else:
       print("Error! Division by zero.")
else:
   print("Invalid operation! Please enter one of the following: +, -, *, /.")