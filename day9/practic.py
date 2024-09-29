list1 =[4,8,2,3]
list2 =[2,0,0,1]
for i in range(len(list1)):
    try:
        print(list1[i]/list2[i])
    except ZeroDivisionError: print("Нельзя делить на ноль")