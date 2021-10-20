#Part of the programm which enciphers user's message
#Version 2.1
#Last edit: 20.10.2021 
#By Kuba Niedziela

                                      
from Functions import *                                 #Importing functions and easy changable variables
from Variables import *



#ENCIPHERING KEY (PUBLIC)              
p_1 = primeGenerator()                                  #randomly generating two prime numbers 'p, q' and two numbers 'e' coprime to their values -1
q_1 = primeGenerator()
ep = coprimeChecker((p_1 - 1))
eq = coprimeChecker((q_1 - 1))

while(ep != eq):                                        #from RSA math theorem, we know that number 'e' must be coprime to both 'p' and 'q' numbers less than 1
    p_1 = primeGenerator()                              #in this loop, numbers are generated unitl the number 'e' is found 
    q_1 = primeGenerator()
    ep = coprimeChecker((p_1 - 1))
    eq = coprimeChecker((q_1 - 1))

n = (p_1 * q_1)                                         #again, from RSA math theorem, we know that number n is (p*q), so we calculate 'n'
e = ep                                                  #now 'ep' is substituted to the variable 'e' which will be used later on 

print("\n YOUR ENCIPHERING KEY IS:") 
print("K = (n =", n, ",", "e =", e, ")")                #enciphering key consists of number 'n' and the found number 'e'

#--------------------------------------------------------

#DECIPHERING KEY (SECRET)
phi_of_n = (p_1 - 1) * (q_1 - 1)                        #calculating the Euler's function for number 'n'. 'p' and 'q' are prime hence we can calculate the function by multiplying their values -1                                                

d = pow(e, (-1), phi_of_n)                              #from RSA math theorem, we have to calculate the inverse of 'e' mod phi of n, (Euler's function of n)

print("\n YOUR DECIPHERING KEY IS:") 
print("K = (n =", n, ",","d =", d, ")")                 #deciphering key consists of number 'n' and the inverse of 'n', called 'd'
   
#--------------------------------------------------------

#ENCIPHERING PROCESS

message = input("\n \n Enter your message:")            #User enters message to encipher

indicator = k                                           #indicator gets the number letters in a plaintext unit
ciphered_message = []                                   #ciphered message list holds single letters, while ciphered message string will return a whole word      
ciphered_message_string = ' '
initialTextNumber = k -1                                #adding variables to be able to change number 'k' of letters on plaintext unit
k = initialTextNumber 

#dividing user's message into groups of k letters
messageList = [(message[i:i+indicator]) for i in range(0, len(message), indicator)]                  


for i in range(messageLength(message, indicator)):

    message = messageList[i]                             #enciphering each letter at the time by getting its index and calculating ciphered number
    encipheringNumber = 0                                #detailed information on how the system works can be found in RSA math description on the web
                                                                     
    for i  in range(len(message)):                                  

        index = alphabet.index(message[i])                                                            

        encipheringNumber = encipheringNumber + (index * (len(alphabet)**k))        

        if(k == 0):
            k = initialTextNumber                         #changing the exponent to its initial value if it gets to 0 in case of longer texts 
        else:   
            k = k -1        

    encipheringFunction = pow(encipheringNumber, e, n)    #evaluating the enciphering function

    z = l - 1                                             #new variable 'z' exponent gets value of ciphered text units -1 

    for i in range(l):                                                  
        q, r = divmod(encipheringFunction, (len(alphabet)**z))        

        if(q > len(alphabet)):                            #deviding with remainder number evaluated by enciphering function, then for l letter ciphertext units 
            q = pow(q, 1, len(alphabet))

        ciphered_message.append(alphabet[q])
        z -=  1 
        encipheringFunction = r


for x in ciphered_message:
    ciphered_message_string += x

print(" \n Your enciphered message is:", ciphered_message_string)
print(" \n Don't forget to give your deciphering key to your recipent! ")

