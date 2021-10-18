import random


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

primeGeneratorUSER()