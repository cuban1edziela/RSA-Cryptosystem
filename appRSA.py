#Project of the RSA cryptography system
#Last edit: 10.10.2021, Sunday


import math


def euclideanAlgoritm():

    print("Enter the first integer: ")              #enering value of integers
    intA = int(input())

    while(intA == 0):                                 #check whether the value is not equal to 0                
        print("Invalid value of integer.")
        print("Enter the valid value of the first integer: ") 
        intA = int(input())



    print("Enter the second integer: ")
    intB = int(input())

    while(intB == 0):
        print("Invalid value of integer.")
        print("Enter the valid value of the second integer: ") 
        intB = int(input())


    if(intA > intB):
        whatleft = (intA % intB) #reszta z dzielenia
        a = intA
        b = intB
        gcdterm = 0

        if(whatleft != 0):                                           #for numbers when a mod b is not equal to 0

            while(whatleft > 0):
                print(whatleft)
                a = whatleft
                whatleft = (b % a)
                b = a

                if(whatleft == 0):
                    gcd = gcdterm

                gcdterm = whatleft
                
                
            print("GCD of", "[", + intA, ";", + intB, "]", "is equal to: ", + gcd)

        else:
            gcd = (a/b)
            print("GCD of", "[", + intA, ";", + intB, "]", "is equal to: ", + b)




    # elif (intA == intB):
    #     print("GCD of", "[", + intA, ";", + intB, "]", "is equal to: ", + intA)
    




    # else:
    #       whatleft = (intB % intA) #reszta z dzielenia
    #     a = intA
    #     b = intB
    #     gcdterm = 0

    #     if(whatleft != 0):                                           #for numbers when a mod b is not equal to 0

    #         while(whatleft > 0):
    #             print(whatleft)
    #             a = whatleft
    #             whatleft = (b % a)
    #             b = a

    #             if(whatleft == 0):
    #                 gcd = gcdterm

    #             gcdterm = whatleft
                
                
    #         print("GCD of", "[", + intA, ";", + intB, "]", "is equal to: ", + gcd)

    #     else:
    #         gcd = (b/a)
    #         print("GCD of", "[", + intA, ";", + intB, "]", "is equal to: ", + b)
          
        
        

        

 
euclideanAlgoritm()

