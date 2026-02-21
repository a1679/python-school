import random
from word2number import w2n

def int_checker(min_val=1, max_val=100):
    while True:
        user_input = input("Take a guess: ").lower()

        try:
            number = w2n.word_to_num(user_input)
        except ValueError:
            try:
                number = int(user_input)
            except ValueError:
                print("That's not a valid number. Try again.")
                continue

        if min_val <= number <= max_val:
            return number
        else:
            print(f"Your number must be between {min_val} and {max_val}.")


name = input("Hello! What is your name? ")

print("Well, " + name + " I am thinking of a number between 1 and 100")

number = random.randint(1,100)


for i in range(1,21):
    guess = int_checker()
    
    
    if guess == number:
        print("You got it correct on your, " + str(i) + " go!")
        break
    elif guess < number: 
        print("Your guess is too low. You have " + str(20-i) + " guesses left.")
    else:
        print("Your guess is too high.You have " + str(20-i) + " guesses left.")
    i + 1
    
    if i == 7:
        print("You did not get it right in 20 guesses.")
        print("My number was " + number + ">")

