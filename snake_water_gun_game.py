
import random

'''
For water : -1
For snake : 0
For gun   : 1
'''

userStr = input("Enter your choice: Snake (s), Water (w), Gun (g): ")

computer = random.choice([-1, 0, 1])

Dict = {
    "w": -1,
    "s": 0,
    "g": 1
}

revDict = {
    -1: "water",
    0: "snake",
    1: "gun"
}

if userStr not in Dict:
    print("Something went wrong")
else:
    userDict = Dict[userStr]
    showChoice = revDict[userDict]

    print(f"You chose {showChoice}")
    print(f"Computer chose {revDict[computer]}")

    if userDict == computer:
        print("Game is tie")
    elif (userDict == 0 and computer == -1) or \
         (userDict == -1 and computer == 1) or \
         (userDict == 1 and computer == 0):
        print("You win")
    else:
        print("You lose")
