from Functions import *
from Variables import *

print("Welcome to Public Key Cryptosystem Program.")
print("\n If you want to encipher a message press 0 and ENTER, to decipher, press 1 and ENTER")
check_user = int(input())

while(check_user != 0 and check_user != 1):
    print("Invalid numerical value. Enter 0 to encipher or 1 to decipher")
    check_user = int(input())

if(check_user == 0):
    import enciphering

if(check_user == 1):
    import deciphering

print("Thank you for using Public Key Cryptosystem Program")
