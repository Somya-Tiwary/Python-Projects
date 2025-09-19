import random
input_list=["Paper","Scissor","Rock"]
user_choice=input("Enter choice from Rock,Paper,Scissor=")
computer_choice=random.choice(input_list)
print("user choice=",user_choice)
print("computer choice = ",computer_choice)
if(computer_choice==user_choice):
    print("there is a tie")

elif(user_choice=="Rock"):
    if(computer_choice=="Paper"):
        print("Paper Wins")
    elif(computer_choice=="Scissor"):
        print("Rock Wins")

elif(user_choice=="Paper"):
    if(computer_choice=="Rock"):
        print("Paper Wins")
    elif(computer_choice=="Scissor"):
        print("Scissor Wins")

elif(user_choice=="Scissor"):
    if(computer_choice=="Paper"):
        print("Scissor Wins")
    elif(computer_choice=="Rock"):
        print("Rock Wins")


