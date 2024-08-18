"""This code implements hoarse partition"""
from random import randint

arr = [randint(0,100) for _ in range(10)]
print(arr)

start = 1 ; end = len(arr)-1
while(start <= end):
    if(arr[start] >= arr[0] and arr[end]<=arr[0]):
        arr[start], arr[end] = arr[end], arr[start]
        start+=1
        end-=1
        
    elif(arr[start] < arr[0]):
        start+=1
    
    else:
        end-=1 

arr[start-1], arr[0] = arr[0], arr[start-1]

print(arr)
