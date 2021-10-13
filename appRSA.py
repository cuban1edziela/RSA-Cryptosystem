#Project of the RSA cryptography system
#Last edit: 12.10.2021, Tusday


import math
import random


def euclideanAlgoritmUSER():

    print("Enter the first integer: ")              #enering value of integers
    intA = int(input())

    while(intA == 0):                                 #check whether the value is not equal to 0                
        print("Invalid value of integer. Number cannot be equal to 0")
        print("Enter the valid value of the first integer: ") 
        intA = int(input())



    print("Enter the second integer: ")
    intB = int(input())

    while(intB == 0):
        print("Invalid value of integer. Number cannot be equal to 0")
        print("Enter the valid value of the second integer: ") 
        intB = int(input())



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



def primeGeneratorUSER():

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
            print("Your generated prime number is", +integer)
            break

def inverseCalculator(a, b):
    # a is the number you want the inverse for
    # b is the modulus

    r = -1
    B = b
    A = a
    eq_set = []
    full_set = []
    mod_set = []

    #euclid's algorithm
    while r!=1 and r!=0:
        r = b%a
        q = b//a
        eq_set = [r, b, a, q*-1]
        b = a
        a = r
        full_set.append(eq_set)

    for i in range(0, 4):
        mod_set.append(full_set[-1][i])

    mod_set.insert(2, 1)
    counter = 0

    #extended euclid's algorithm
    for i in range(1, len(full_set)):
        if counter%2 == 0:
            mod_set[2] = full_set[-1*(i+1)][3]*mod_set[4]+mod_set[2]
            mod_set[3] = full_set[-1*(i+1)][1]

        elif counter%2 != 0:
            mod_set[4] = full_set[-1*(i+1)][3]*mod_set[2]+mod_set[4]
            mod_set[1] = full_set[-1*(i+1)][1]

        counter += 1

    if mod_set[3] == B:
        return mod_set[2]%B
    return mod_set[4]%B


    # f=int(input("eneter 1st number"))
    # g=int(input("enter 2nd number"))


    # remainders = []
    # devisors = []
    # x = g                                       #g, the second value is the numver which we want to find inverse of

    # d, r = divmod(f,g)

    # while(r != 0):
    #     d, r = divmod(f,g)
        
    #     devisors.append(d)                                        #saving the values into lists 
    #     remainders.append(r)

    #     f = (f-r)//d
    #     g = r


        
    # print(devisors, "and", remainders, )






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

print("YOUR ENCIPHERING KEY IS:") 
print("K = (", n, ",", e, ")")                      #enciphering key consists of number 'n' (two primes multiplied) and the found number 'e'

    


#DECIPHERING KEY (SECRET)

phiofn = (p_1 - 1) * (q_1 - 1)

d = (inverseCalculator(e, phiofn))                                  #calculate the inverse of 'e' mod phi of n

print("YOUR DECIPHERING KEY IS:") 
print("K = (", n, ",", d, ")")   

    
    

    
    

