from random import randint

n = int(input("Select a maximum number: "))
number = int(randint(1, n))

def check():
    guess = int(input("Guess-a-number: "))
    if guess > number:
        print("Too high")
        check()
    if guess < number:
        print("Too Low")     
        check()
    else:
        print("You got it!")
        exit()


check()