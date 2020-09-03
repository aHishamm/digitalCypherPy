#encoding the message with a specific key
def encode(message, key):
    key = list(str(key))
    message = list(message)
    for i in range(len(message)):
        message[i] = str(chr((ord(message[i])) + (int(key[i % len(key)]))))
    return "".join(message)
#decoding the message with a specific key
def decode(message, key):
    message = list(message)
    key = list(str(key))
    for i in range(len(message)):
        message[i] = int(ord(message[i])) - int(key[i % len(key)])
    for i in range(len(message)):
        message[i] = chr(message[i])
    return "".join(message)
