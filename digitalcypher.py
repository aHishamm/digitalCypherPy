#encoding the message with a specific key
def encode(message, key):
    key = list(str(key))
    message = list(message)
    for i in range(len(message)):
        message[i] = str((ord(message[i]) - 96) + (int(key[i % len(key)])))
        #message[i] = str(chr((ord(message[i])) + (int(key[i % len(key)]))))
    return " ".join(message)
#decoding the message with a specific key
def decode(message, key):
    message = message.split(' ')
    key = list(str(key))
    for i in range(len(message)):
        message[i] = int(message[i]) - int(key[i % len(key)])
    for i in range(len(message)):
        message[i] = chr(message[i] + 96)
    return "".join(message)


#string = encode("Hello World",1231)

#print(decode(string,1231))