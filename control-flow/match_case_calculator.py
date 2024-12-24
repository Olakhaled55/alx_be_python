num1= float(input("Enter the first number: "))
num2= float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")
match operation:
 case"+":
  result=num1+num2
  print(F" the result is{result}.")
 case"-":
  result=num1-num2
  print(F" the result is{result}.")
 case"*":
  result=num1*num2
  print(F" the result is{result}.")
 case"/":
  result=num1/num2
  print(F" the result is{result}.")
  else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation selected. Please choose one of +, -, *, or /.")
