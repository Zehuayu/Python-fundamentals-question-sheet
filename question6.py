##compare list number which is biggest and which is smallest


def getList(x):

    list = []

    for i in range(0,x):
     list.extend([int(input())])
    return list

def compare(list):
    max = list[0]# let first number compare to others
    for x in list:
        if (max < x):
            max = x


    min = list[0]# let first number compare to others
    for x in list:
          
           
        if (min > x):
            min = x



    print("maxmum number:" + str(max) + "   " + "minmum number:" + str(min))



list = getList(6)
print(str(list))

compare(list)
    
