##Write a function that tests whether a string is a palindrome.
#resouce from https://stackoverflow.com/questions/952110/recursive-function-palindrome-in-python
def palindrome():
 a = str(input("enter the string:"))
 b=len(a)
 c=0
 for i in range(b):
    if a[i]==a[-(i+1)]:
        c=c+1
 if c==b:
    print (a,"is polindrome")
 else:
    print (a,"is not polindrome")



palindrome()