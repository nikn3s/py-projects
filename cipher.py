def ceasar_cipher(message, cipher):
    enc_word = ""
    for l in message:
        coded_l = ord(l)
        shifted = coded_l + cipher
        enc_chr = chr(shifted)
        enc_word += enc_chr

    return enc_word
        

mess = input("Message: ")
shift = int(input("Shift: "))

print(ceasar_cipher(mess, shift))