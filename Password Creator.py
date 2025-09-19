Length=int(input("Enter the length of password to be created :="))
character=input("Enter the character to be used :=")
number=input("Enter the digit to be used := ")
word=input("Enter the desired word :=")
Password=character+number+word
print("Final Password is =",Password)
count=0
for i in Password:
    count=count+1
print("Length of the Password is =",count)
if (count==Length):
    print("Valid Password")
else:
    print("Invalid Password")
