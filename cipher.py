def ceasar_cipher(message, shift):
    # create a varible to store message
    enc_word = ""
    # loop over each letter in the word
    for l in message:
        # convert each letter into ascii code
        coded_l = ord(l)
        # shift the letter x steps
        shifted = coded_l + shift
        # convert into characters
        enc_chr = chr(shifted)
        # insert into previously created string
        enc_word += enc_chr

    return enc_word
        

mess = input("Message: ")
shift = int(input("Shift: "))

print(ceasar_cipher(mess, shift))
