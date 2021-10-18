message = input("\n \n Enter your message:")

indicator = 3


messageLength, remainder = divmod(len(message), 3)
if(remainder != 0):
    messageLength += 1
    
print("message length equals", messageLength)


k = 3

messageList = [(message[i:i+indicator]) for i in range(0, len(message), indicator)]



for i in range(messageLength):

    message = messageList[i]
    print(message)


    

