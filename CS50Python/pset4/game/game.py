from random import randint

level = 0

while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except ValueError:
        pass


number = randint(1, level)

while True:
    guess = int(input("Guess: "))

    if guess == number:
        print("Just right!")
        break
    elif guess < number:
        print("Too small!")
    else:
        print("Too large!")

