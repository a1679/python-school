import random

name = input("Hello! What is your name?")

print("Well, " + name + " I am thinking of a number between 1 and 20")

number = random.randint(1,20)


for i in range(1,7):
    guess = input("Take a guess: ")
    guess = int(guess)

    if guess == number:
        print(f"You got it correct on your, " + str(i) + " go!")
        break
    elif guess < number: 
        print(f"Your guess is too low. You have " + str(6-i) + " guesses left.")
    else:
        print(f"Your guess is too high.You have " + str(6-i) + " guesses left.")
    i + 1
    
    if i == 7:
        print("You did not get it right in 6 guesses.")
        print("My number was " + number + ">")

