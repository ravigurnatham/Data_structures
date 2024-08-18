"""This code codes up the lomuto partition algorithm which calculates the correct positioin of a number"""
from random import randint

arr = [randint(0,100) for _ in range(10)]
print(arr)



def lomuto(arr):
    """function for implementing the lomuto partition algorithm"""
    pivot = arr[0]
    print(f'pivot element is {pivot}')
    #Numbers which are less than or equals to pivot stay left side and greater elements on green side
    #since pivot is already equal to itself we can start smaller or pivot index and bigger index from next number
    smaller = 0
    for green in range(smaller+1, len(arr)):
        if(arr[green] >= pivot):
            continue
        else:
            smaller += 1
            arr[smaller], arr[green] = arr[green], arr[smaller]
        print(arr)
    
    arr[0], arr[smaller] = arr[smaller], arr[0]
    print(arr)
            

if __name__=="__main__":
    lomuto(arr)