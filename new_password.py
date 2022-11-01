from cs50 import get_int
from random import choice, randint
from sys import exit

def main():
    global length
    length = get_int("Provide a length: ")
    # prevent bugs
    if length <= 4:
        print("Password must be at least 5 characters")
    elif length > 16:
        print("Password must be at most 16 characters")
        exit()       
    # create empty variables
    global letters
    alphabet_lower = []
    alphabet_upper = []
    global randomNum

    # lowercase alphabet
    for i in range(97, 123):
        alphabet_lower.append(chr(i))
    # uppercase alphabet 
    for j in range(65, 91):
        alphabet_upper.append(chr(j))
    
    letters = alphabet_lower + alphabet_upper
    del alphabet_lower
    del alphabet_upper
    pass_gen()

def pass_gen():
    for i in range(length):
        print(randint(0, 10) and choice(letters) end="")
main()

# def get_length():
#   length = int(input("Choose length: "))
#   return 0 
