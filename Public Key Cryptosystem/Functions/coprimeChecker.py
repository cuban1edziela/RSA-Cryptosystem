import random


def coprimeChecker(k):

    gcd = 0

    while(gcd != 1):

        intA = k                              #generate a random number. range must be changed at least 2k digit number 
        intB = random.randint(1, 1000)

        whatleft = (intA % intB) 
        a = whatleft
        b = intB

        if(whatleft != 0):                                           #for numbers when a mod b is not equal to 0

            while(whatleft > 0):
                
                whatleft = (b % a)
                b = a

                if(whatleft == 0):
                    gcd = a             
                
                a = whatleft

    return intB