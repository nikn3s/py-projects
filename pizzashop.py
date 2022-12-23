def clients(*names):
    # illiterate through the array of people
    people = (name for name in names)   
    return tuple(people)

try:
    count = int(input("How many clients?: ")) 
except ValueError:
    print("Please enter a number")
    exit()
# create a file to store names
names = tuple()
for i in range(count):
    name = input("Enter client name: ")
    # add each name to the array
    names += clients(name)

print(names)

# 22/12/2022 - Bug: The tuple 'people' returns a tuple with integer 0. I will fix this later
#How many clients?: 2
#Name:Alex
# (0,)
# Name:Gorgia 
# (0,) 

# 23/12/2022 - Everthing now works just fine; the function was easier to make than I thought
