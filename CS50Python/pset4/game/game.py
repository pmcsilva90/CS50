from random import randint

level = 0

while level <= 0:
    level = int(input("Level: "))

number = randint(1, level)

guess = int(input("Guess: "))

if guess == number:
    print("Just right!")
elif guess < number:
    print("Too small!")
else:
    print("Too large!")

