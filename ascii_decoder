import argparse as ap

def getArgs():
    # creating parser for the program
    parser = ap.ArgumentParser(description="ASCII -> character converter")
    # creating required argument by the function ascii_file
    parser.add_argument("ascii_file", type=str, help="Enter ASCII chararcter/s")
    #obtaning the raw input
    args = parser.parse_args()
    # # obtaining the file name from user's argument
    file = args.ascii_file
    #creating empty character list to hold ASCII numbers
    char_list = []
    #opening the file.txt
    with open(file, "r") as f:
        for line in f:
            char_list.append(int(line.strip()))
    return char_list

def decodeASCII(charList:list[int]) -> str:
    asciiList = []
    for value in charList:
        temp = chr(value)
        asciiList.append(temp)
    output = ''.join(asciiList)
    return output

print(decodeASCII(getArgs()))
