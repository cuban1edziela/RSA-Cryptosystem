#Project of the RSA cryptography system
#Last edit: 11.10.2021, Monday


import math
import random


def euclideanAlgoritm():

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




def coprimeChecker():

    gcd = int

    while(gcd != 1):


        intA = random.randint(1, 10000)                                #generate a random number. range must be changed at least 2k digit number 

        intB = random.randint(1, 10000)

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

    print("number", +p, "and", +q, "are coprime bc their gcd =", +gcd)
    
            
    
        





 

coprimeChecker()
