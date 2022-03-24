#python program to to multiply all numbers in the list 
def multiplyList (myList):
    result =1
    for x in myList :
        result = result *x
    return result
List1 = [4,5,6]    
print(multiplyList(List1))       