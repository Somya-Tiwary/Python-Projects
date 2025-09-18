import random
subjects=["Shahrukh Khan ","Nirmala Sitharaman ","Salman Khan ","MSDhoni "]
actions=["Sleeps on road ","Dances on stage ","Sells fruits ","celebrates "]
Places_or_thing=["in Mumbai ","outside his home ","near Taj Mahal ","across the street "]
while True:
    subject=random.choice(subjects)
    action=random.choice(actions)
    Places=random.choice(Places_or_thing)
    headline=f"BREAKING NEWS:{subject }{action }{Places }"
    print("\n"+headline)
    user_input=input("Enter your choice")
    if user_input=="no":
        break
print("Thanks for using Fake news generator")
print("GoodBye")