def main():
    n = int(input("How many blocks do you want? "))
    o = input("Vertical or horizontal alignment? ")

    try:
       block(o)
    except ValueError:
        print("Not a number")

def block(s):
    if s in ["horizontal", "h"]:
        print("#", end="")
    elif s in ["vertical", "v"]:
        print("#")
    else:
        print("Error: Invalid Value")

                

main()    