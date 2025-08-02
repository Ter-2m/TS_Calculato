# Asking user for num1(Integer)
num1=int(input())
#Asking for operation(+,-,/,*)
operation=input(+,-,/,*)
#Asking for num2
num2=int(input())
#Conditions
if operation == '+'
 result=num1 + num2
elif operation == '-'
 result==num1 - num2
elif operation == '*'
 result=num1*num2
elif operation=='/'
 if num2 != 0:
  result=num1/num2
  else:
      print("INFINITY")
 # Display result
 print(f"{num1}{operation}{num2} is:{result}")
  
   