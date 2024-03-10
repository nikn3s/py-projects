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
    try:    
        with open(file, "r") as f:
            for line in f:
                char_list.append(int(line.strip()))
    except ValueError:
        return "Value Error: The file provided must contain just numbers"

    return char_list

def decodeASCII(charList:list[int]) -> str:
    try:
        asciiList = []
        for value in charList:
            temp = chr(value)
            asciiList.append(temp)
        output = ''.join(asciiList)
        return output
    except Exception as e:
        return f"{e}\nMake sure the file just contains numbers on seperate lines"

print(decodeASCII(getArgs()))
