def ascii_caesar_shift(message, distance):
    encrypted = ""
    for char in message:
        a = ord(char)
        value = ord(char) + distance
        if value <= 33: # non-printable characters in ascii
            value -= 33
        encrypted += chr(value % 128) #128 for ASCII
    return encrypted
    
mess = str(input("Masukkan pesan yg terenkrip: "))
print(ascii_caesar_shift(mess, -18))