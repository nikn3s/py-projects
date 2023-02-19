from random import randint as pick

print("Welcome To the Dice Arcade Game!")
total = 0

while True:
    # Initialise a variable - stores random num.
    dice = pick(1, 6)
    # dice2 = pick(1, 6) 
    print("What you rolled: ", dice)
    consent = input("Want to roll again? ")
    total += dice

    if consent == "yes":
        # resumes the loop if the player agreed.
        continue;
    if total == 20:
        # If the player's total = 20, they win.
        print("You won!")
        break;
    else: 
        print("Total: ", total)
        break;

print("Thank you for playing!")

# What this project taught me? 
# I now got a deeper understanding where while loop may be useful.
