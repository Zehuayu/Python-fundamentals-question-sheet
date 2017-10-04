#check a number whether bigger or smaller secret number
#iuput a number and give feedback that large and small, if input number is the same of secret number,
#  the result show true.


from random import randint

def getSecret():
    return randint(1,100)  #got a random number

def gussNumber(secret):

    flag = True

    tired = 0

    guessed = 0
    while(flag):

        guess = input("enter your guess number \n" )

        if (int(guess) > secret):
        
         print("it is too large")
    
        elif (int(guess) < secret):
        
         print("it is too small")  # campare to secret number
        
        else:
         print("you are correct!!")

         flag = False

         # avoid same number guessed more than one time consecutively
        if(guess != guessed):   
        
            tired += 1
            guessed = guess
    print("game end!! `.`  \n  you have tried "+str(tired)+" times!")




secret = getSecret()

gussNumber(secret)
        



