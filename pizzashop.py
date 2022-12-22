def clients(*names):
    people =list()
    for name in range(len(names)):
        people.append(name)
    return tuple(people) 
try:
    count = int(input("How many clients?: ")) 
except ValueError:
    print("Please enter a number")

for person in range(count):
    dude = input("Name:")
    print(clients(dude))

# 22/12/2022 - Bug: The tuple 'people' returns a tuple with integer 0. I will fix this later
#How many clients?: 2
#Name:Alex
# (0,)
# Name:Gorgia 
# (0,)