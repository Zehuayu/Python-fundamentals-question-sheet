def getFactionalSum(n):
    sum = 0
    for x in range(101):
       if sum == 0:
        sum = sum + x
       else:
        sum = sum * x
    return sum   

def getDigitSum(sum):
    # function to get digit sum, get each last digit by sum%10
    sumDigit=0
    while(sum):
        sumDigit +=  int(sum%10)
        sum /= 10
    return sumDigit    

#  n =100
n=100
sum = getFactionalSum(n)
print(str(n)+"! = "+str(sum))
# digit sum
sumDigit = getDigitSum(sum)
print("result is: " + str(sumDigit))