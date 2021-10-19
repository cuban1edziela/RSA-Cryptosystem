
def messageLength(message, length):
    messageLength, remainder = divmod(len(message), length)
    if(remainder != 0):
        messageLength += 1
        return messageLength
    return messageLength


l = 4
k = 3

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

#DECIPHERING

USERciphermessage = input("Enter a message you want to decipher: ")                   #entering the required values
n = int(input("\n Enter the 'n' value of the key:"))
d = int(input("\n Enter the 'd' value of the key:"))

ciphermessageList = [(USERciphermessage[i:i+l]) for i in range(0, len(USERciphermessage), l)] 
ciphermessagelength = messageLength(USERciphermessage, 4)
cipherednumber = 0
ciphermessage = ' '
decipheredMessage = []
deciphered_message_string = ' '

for i in range(ciphermessagelength):
    ciphermessage = ciphermessageList[i]
    cipherednumber = 0
    exponent = k - 1 
    
    z = l - 1   

    
    for x in range(len(ciphermessage)):
        index = alphabet.index(ciphermessage[x])
        cipherednumber += (index * (len(alphabet)**z))
        z -= 1                          


    decipherednumber = pow(cipherednumber, d, n)

    for i in range(k):
        number_multiplicative = len(alphabet)**exponent

        q, r = divmod(decipherednumber, number_multiplicative)

        decipheredMessage.append(alphabet[q])

        decipherednumber = r

        if(exponent == 0):
            exponent = k-1
        else:
            exponent -= 1



for x in decipheredMessage:
    deciphered_message_string += x

print("\n Deciphered message is", deciphered_message_string)