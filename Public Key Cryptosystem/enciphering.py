from Functions import *
from Variables import *





cipheredMessage = []

#ENCIPHERING KEY (PUBLIC)
p_1 = primeGenerator()
q_1 = primeGenerator()
ep = coprimeChecker((p_1 - 1))
eq = coprimeChecker((q_1 - 1))


while(ep != eq):                                    #generate two prime numbers and check if for their (values - 1) exists the same coprime number equal 1
    p_1 = primeGenerator()
    q_1 = primeGenerator()
    ep = coprimeChecker((p_1 - 1))
    eq = coprimeChecker((q_1 - 1))

n = (p_1 * q_1)                                     #calculate 'n'
e = ep

print("\n YOUR ENCIPHERING KEY IS:") 
print("K = (n =", n, ",", "e =", e, ")")             #enciphering key consists of number 'n' (two primes multiplied) and the found number 'e'


#DECIPHERING KEY (SECRET)

phiofn = (p_1 - 1) * (q_1 - 1)

print("phi of n equals", phiofn)

d = pow(e, (-1), phiofn)                                 #calculate the inverse of 'e' mod phi of n

print("\n YOUR DECIPHERING KEY IS:") 
print("K = (n =", n, ",","d =", d, ")")   

    
#ENCIPHERING PROCESS

message = input("\n \n Enter your message:")

indicator = k
stringCipheredMessage = ' '
encipheringNumber = 0
initialTextNumber = k -1
k = initialTextNumber

messagelength = messageLength(message, 3)   

messageList = [(message[i:i+indicator]) for i in range(0, len(message), indicator)]                 #dividing user's message into groups of 3 letters 


for i in range(messagelength):

    message = messageList[i]
    encipheringNumber = 0    
    multiplicative = 0                                                                    #recalling every group of 3 letters until the whole message is enciphered

    for i  in range(len(message)):                                  

        index = alphabet.index(message[i])                              #recalling the number in alphabet list of chars entered by user 

        multiplicative = len(alphabet)**k                               #length of used alphabet times number of plaintext units 

        encipheringNumber = encipheringNumber + (index * multiplicative)        

        if(k == 0):
            k = initialTextNumber                                        #changing the exponent to its initial value if it gets to 0 in case of longer texts 
        else:   
            k = k -1

    encipheringFunction = pow(encipheringNumber, e, n)                #evaluating the enciphering function

    z = l - 1                                                         #new variable 'z' exponent gets value of ciphered text units -1 

    for i in range(l):                                                  
        q, r = divmod(encipheringFunction, (len(alphabet)**z))        #deviding with remainder number evaluated by enciphering function, then for l letter ciphertext units 

        if(q > len(alphabet)):
            q = pow(q, 1, len(alphabet))

        cipheredMessage.append(alphabet[q])
        z -=  1 
        encipheringFunction = r


for x in cipheredMessage:
    stringCipheredMessage += x

print(" \n Your enciphered message is:", stringCipheredMessage)
print(" \n Don't forget to give your deciphering key to your recipent! ")

