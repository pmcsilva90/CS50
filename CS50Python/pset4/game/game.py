from random import randint

level = 0

while level <= 0:
    level = int(input("Level: "))

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

