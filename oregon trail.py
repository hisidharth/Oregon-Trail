import random, os
health=5
cday=1
cmonth=3
food=500
distance_left=2000
days_left=0
hunting=["You killed a deer","You went fishing","You found a chicken"]
dangerevents=["You slipped on a frog","You fell", "You apporached a horse from behind"] 
gamestate=True

def dayspast():
    global cday,cmonth,danger,danger2,food,health,dangerevents
    month30=[4,6,9,11]
    month31=[3,5,7,8,10,12]
    day=+random.randint(2,5)
    print(day,"Have past")
    cday+=day
    danger=random.randint(10,20)
    danger2=random.randint(25,29)
    food-=int(cday)
    if cday>danger:
        print(random.choice(dangerevents))
        print("You have lost health")
        health-=1
        danger=99
    if cday>danger2:
        print(random.choice(dangerevents))
        print("You have lost health")
        health-=1
        danger2=88
    if cday >30:
        if cmonth in month30:
            cday=cday-30
            cmonth+=1
            danger=random.randint(10,20)
            danger=random.randint(25,29)
        else:
            cday=cday-31
            cmonth+=1
            danger=random.randint(10,20)
            danger=random.randint(25,29)
def hunt():
    global food, days_left
    food+=100
    print(random.choice(hunting))
    dayspast()
def rest():
    global health, days_left
    health+=1
    dayspast()
def travel():
    global distance_left, days_left
    distance_left-=random.randint(30,60)
    print("You have", distance_left, "miles to go")
    dayspast()
name=input("What is your name?")
while gamestate==True:
    print("The date is",str(cday)+"/"+str(cmonth)+". You have",str(distance_left),"miles left to travel. You have",str(food),"pounds of food left.") 
    choice=int(input(name+"WHAT DO YOU WANT TO DO? 1:TRAVEL, 2:HUNT, 3:REST, 4:QUIT, 5:Status"))
    if choice==int(2):
        hunt()
    if choice==int(3):
        rest()
        if health>5:
            print("You are full health")
    if choice==int(1):
        travel()
    if cmonth>12:
        print("you lost")
        os.system("pause")
        gamestate=False
    if distance_left<=0:
        print("You won")
        os.system("pause")
        gamestate=False
    if choice==int(5):
        print("The date is",str(cday)+"/"+str(cmonth)+". You have",str(distance_left),"miles left to travel. You have",str(food),"pounds of food left.") 
    if choice==int(4):
        gamestate=False
