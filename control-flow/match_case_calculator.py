num1= float(input("Enter the first number: "))
num2= float(input("Enter the second number: "))
operation= input(choose the operation (+, -, *, /):)
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
 print("Cannot divide by zero.")
 case_:
 print("invalid operation please choose one of +, -, *, /.")

       
