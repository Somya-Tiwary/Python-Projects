26# SIMPLE ARITHMETIC CALCULATOR
num1=int(input("enter the first number:="))
num2=int(input("enter the second number:="))
print("Select Choices :-\n"
      "A) Addition\n"
      "B) Substraction\n"
      "C) Division\n"
      "D) Multiplication\n")
      
choice=input("Select choices between (A-D)")

if (choice=="A"):
    print( num1, "+", num2, "=",num1+num2)
elif(choice=="B"):
    print(num1,"-",num2,"=",num1-num2)
elif(choice=="C"):
    print(num1,"*",num2,"=",num1*num2)
elif(choice=="D"):
    print(num1,"/",num2,"=",num1/num2)
else:
    print("Invalid Choice")
     
