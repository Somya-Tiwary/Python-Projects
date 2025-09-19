
import random
easy_level=["car","bus","train","bike"]
medium_level=["tiger","elephant","wolf","lioness"]
hard_level=["chimpanzee","seahorse","orangutan","belugawhale"]
print("Welcome to the password guessing game")
print("Choose your level")
level=input("Enter difficulty = ").lower()
if(level=="easy"):
    secret=random.choice(easy_level)
elif(level=="medium"):
    secret=random.choice(medium_level)
elif(level=="hard"):
    secret=random.choice(hard_level)
else:
    print("Invalid choice !defaulting to easy level")
    secret=random.choice(easy_level)

attempts=0
print("Guess the word!\n")
while True:
    guess=input("Guess the word=")
    attempts+=1
    if(guess==secret):
        print(f"Congratulations! you found the word in {attempts} attempts " )
        break
    else:
        hint=" "
        for i in range(len(secret)):
            if(i<len(guess) and guess[i]==secret[i]):
                hint+=guess[i]
            else:
                hint+=" "
        print("HINT:"+ hint)
print("Game Over")
                
            

