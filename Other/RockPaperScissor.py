"""
            rock    paper   scissors
rock          0       1        -1
paper         -1      0
scissors                       0

r -1
p 0
s 1


"""

rock = -1
paper = 0
scissors = 1

def outcome(p1, p2):

    if p1 - p2 == 0
        return "draw"
    elif p1 - p2 == 1
        return "player 1 wins"
    elif p1 - p2 != 1
        return "player 2 wins"

while True
    p1 = input("player 1: ").lower()
    p2 = input("player 2: ").lower()



    if p1 not in ["rock", "paper", "scissors"] and p2 not in ["rock", "paper", "scissors"]
        continue
    elif p1 == p2
        print("draw")
    else
        if p1 == "rock" and p2 == "paper"
            print()
