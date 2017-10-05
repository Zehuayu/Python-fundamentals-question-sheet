import math

#z_next = z - ((z*z - x) / (2 * z))

def newtonsMethod(x,z):
    
    while True:
        tmp = z - ((z*z - x) / (2 * z))
        if(tmp == z or math.fabs(tmp-z)<0.000000000001):
            break
        z=tmp
    return tmp






#use the math_sqrt function
def math_sqrt(x):
    
    sqrt = math.sqrt(x)
    print("math.sqrt("+str(x)+") = "+str(sqrt))




x = 2
math_sqrt(x)

z=1.0
print(newtonsMethod(x,z))
