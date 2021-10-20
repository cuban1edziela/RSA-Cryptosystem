#Part of the programm which deciphers user's message. 

#Importing functions and easy changable variables
from Functions import *
from Variables import *

#User enters required information: ciphered message and two values of the key
user_ciphered_message = input("Enter a message you want to decipher: ")                   
n = int(input("\n Enter the 'n' value of the key:"))
d = int(input("\n Enter the 'd' value of the key:"))

#Ciphered message is splited into 'l' letter ciphertext units. T
#The value of 'l' can be easly changed in Variables folder
ciphered_messageList = [(user_ciphered_message[i:i+l]) for i in range(0, len(user_ciphered_message), l)] 


ciphermessage = ' '
decipheredMessage = []
deciphered_message_string = ' '

for i in range(messageLength(user_ciphered_message, 4)):
    ciphermessage = ciphered_messageList[i]
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

        if(q > len(alphabet)):
            q = pow(q, 1, len(alphabet))

        decipheredMessage.append(alphabet[q])

        decipherednumber = r

        if(exponent == 0):
            exponent = k-1
        else:
            exponent -= 1



for x in decipheredMessage:
    deciphered_message_string += x

print("\n Deciphered message is", deciphered_message_string)