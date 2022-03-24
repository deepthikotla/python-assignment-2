#python program to print all odd numbers in a range
a, b = 4, 19
for num in range (a, b+1):
    if num % 2 != 0 :
        print( num , end =" ")