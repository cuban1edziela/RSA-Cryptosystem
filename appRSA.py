#Project of the RSA cryptography system
#Last edit: 18.10.2021, Monday


import math
import random



def euclideanAlgoritmNUMBER(f, g):

    intA = f

    intB = g

 

    whatleft = (intA % intB) #reszta z dzielenia
    a = whatleft
    b = intB
    gcdterm = 0
    
    if(whatleft != 0):                                           #for numbers when a mod b is not equal to 0

        while(whatleft > 0):
            
            whatleft = (b % a)
            b = a

            if(whatleft == 0):
                gcd = a             
            
            a = whatleft
    
            
        print("GCD of", "[", + intA, ";", + intB, "]", "is equal to: ", + gcd)

    else:
        gcd = (a/b)
        print("GCD of", "[", + intA, ";", + intB, "]", "is equal to: ", + b)



def coprimeChecker(k):

    gcd = int

    while(gcd != 1):


        intA = k                              #generate a random number. range must be changed at least 2k digit number 

        intB = random.randint(1, 1000)



        whatleft = (intA % intB) 
        a = whatleft
        b = intB
        gcdterm = 0

        if(whatleft != 0):                                           #for numbers when a mod b is not equal to 0

            while(whatleft > 0):
                
                whatleft = (b % a)
                b = a

                if(whatleft == 0):
                    gcd = a             
                
                a = whatleft

    p = intA
    q = intB

    return q
    

def coprimeCheckerE(k, e):

    gcd = int

    while(gcd != 1):


        intA = k                              #generate a random number. range must be changed at least 2k digit number 

        intB = e



        whatleft = (intA % intB) 
        a = whatleft
        b = intB
        gcdterm = 0

        if(whatleft != 0):                                           #for numbers when a mod b is not equal to 0

            while(whatleft > 0):
                
                whatleft = (b % a)
                b = a

                if(whatleft == 0):
                    gcd = a             
                
                a = whatleft

    p = intA
    q = intB

    return q




def inverseCalculator(a, b):

    inverse = pow(a, -1, b)

    return inverse



def messageLength(message, length):
    messageLength, remainder = divmod(len(message), length)
    if(remainder != 0):
        messageLength += 1
        return messageLength
    return messageLength



def primeGeneratorNUMBER():

    integer = random.randint(100, 1000)
    dev = 2


    while(dev != integer):

        left = integer % dev 

        if(left == 0):  
           # print("wrong number was", +integer)                    #it regenerates the number when a number mod int is equal to 0
            integer = random.randint(100, 1000)
            dev = 1
            
        
        dev = dev + 1
        

        if(dev == integer):
            return integer
            break



#Program beginning



#26-letter alphabet

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
cipheredMessage = []
k = 3                                               # 3 letter plaintext message units 
l = 4                                               # 4 letter cipghertext message units



#ENCIPHERING KEY (PUBLIC)
p_1 = primeGeneratorNUMBER()
q_1 = primeGeneratorNUMBER()

n = (p_1 * q_1)                                     #calculate 'n'

ep = coprimeChecker((p_1 - 1))
eq = coprimeChecker((q_1 - 1))

while(ep != eq):                                    #generate two prime numbers and check if for their (values - 1) exists the same coprime number equal 1
    p_1 = primeGeneratorNUMBER()
    q_1 = primeGeneratorNUMBER()

    ep = coprimeChecker((p_1 - 1))
    eq = coprimeChecker((q_1 - 1))

e = ep

#print("'e' for number", +p_1, "and number", +q_1, "equals", +e)   

print("\n YOUR ENCIPHERING KEY IS:") 
print("K = (n =", n, ",", "e =", e, ")")                      #enciphering key consists of number 'n' (two primes multiplied) and the found number 'e'


#DECIPHERING KEY (SECRET)

phiofn = (p_1 - 1) * (q_1 - 1)

d = (inverseCalculator(e, phiofn))                                  #calculate the inverse of 'e' mod phi of n

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

    print("your umber is equal: ", encipheringFunction)

    z = l - 1                                                         #new variable 'z' exponent gets value of ciphered text units -1 

    for i in range(l):                                                  
        
        q, r = divmod(encipheringFunction, (len(alphabet)**z))        #deviding with remainder number evaluated by enciphering function, then for l letter ciphertext units 

        cipheredMessage.append(alphabet[q])

        z -=  1 
        encipheringFunction = r



for x in cipheredMessage:
    stringCipheredMessage += x


print(" \n Your enciphered message is:", stringCipheredMessage)
print(" \n Don't forget to give your deciphering key to your recipent! ")



#DECIPHERING

USERciphermessage = input("Enter a message you want to decipher: ")                   #entering the required values
n = int(input("\n Enter the 'n' value of the key:"))
d = int(input("\n Enter the 'd' value of the key:"))

ciphermessageList = [(USERciphermessage[i:i+l]) for i in range(0, len(USERciphermessage), l)] 


ciphermessagelength = messageLength(USERciphermessage, 4)

cipherednumber = 0

ciphermessage = ' '

for i in range(ciphermessagelength):
    ciphermessage = ciphermessageList[i]
    cipherednumber = 0
    
    
    z = l - 1   

    
    for x in range(len(ciphermessage)):
        index = alphabet.index(ciphermessage[x])
        cipherednumber += (index * (len(alphabet)**z))
        z -= 1                          

    
    decipherednumber = pow(cipherednumber, d, n)

print(cipherednumber)