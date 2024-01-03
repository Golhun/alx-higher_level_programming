def uppercase(str):
    msg = ""
    for char in str:
        if ord(char) >= ord("a") and ord(char) <= ord("z"):
            chr_upper = chr(ord(char) -32)
        else:
            chr_upper = char
        msg += chr_upper
    print("{}".format(msg))

