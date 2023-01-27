import os
import copy

def main():
    file = str(input("Enter file name: "))

    if os.path.exists(file):
        file = open(file, "a")
        mess = str(input("Enter what you want to encrypt: "))
        with file as f:
            f.writelines(cs(mess))
    else: 
        print("File does not exist")
        exit()

def cs(message, cipher = 3):
    enc_word = ""
    for l in message:
        coded_l = ord(l)
        shifted = coded_l + cipher
        enc_chr = chr(shifted)
        enc_word += enc_chr
    return enc_word

if __name__ == "__main__":
    main()       