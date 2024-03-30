def main():

    while True:
        p1 = input("player 1: ").lower()
        if p1 not in ["rock", "paper", "scissors"]:
            continue
        else:
            match p1:
                case "rock":
                    p1 = -1
                    break
                case "paper":
                    p1 = 0
                    break
                case "scissors":
                    p1 = 1
                    break
            break

    while True:
        p2 = input("player 2: ").lower()
        if p2 not in ["rock", "paper", "scissors"]:
            continue
        else:
            match p2:
                case "rock":
                    p2 = -1
                    break
                case "paper":
                    p2 = 0
                    break
                case "scissors":
                    p2 = 1
                    break
            break

    print(outcome(p1, p2))

def outcome(p1, p2):

    if p1 - p2 == 0:
        return "draw"
    elif p1 - p2 == 1:
        return "player 1 wins"
    else:
        return "player 2 wins"

main()
