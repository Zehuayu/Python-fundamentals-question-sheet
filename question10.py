# reverse a string.



#  input a string
def getString ():
    string = input("input a string:\n")
    return string


#resource from https://stackoverflow.com/questions/931092/reverse-a-string-in-python
#reserve a string
def reverse (s):
    print("reverse string is  " +"'" + s[::-1]+"'")



String = getString()

print("you type string is" + "'" + String + "'")

reverse(String)




