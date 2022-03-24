#python program to print all negative numbers in a range 
a, b = -10, 19
for num in range (a, b+1):
    if num <= 0:
        print ( num , end = " ")