#python program to print all positive numbers in a range
a ,b = -2, 19
for num in range (a,b+1):
    if num >= 0:
        print (num , end = " ")