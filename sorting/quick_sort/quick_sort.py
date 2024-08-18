"""quick algo"""
from random import randint

class Quicksort:
    """Implements the quicksort algorithm"""
    def __init__(self, nums) -> None:
        self.nums = nums
        self.length = len(self)
    
    def __len__(self):
        return len(self.nums)

    
    def sort(self, start=0, end=None):
        """Main sorting code runs here"""
        if(end is None):
            end=self.length
        
        if((end-start)<=1):
            return 
        
        smaller = start
        pivot_value = self.nums[start]
        for bigger in range(start+1, end):
            if(self.nums[bigger] > pivot_value):
                continue
            else:
                smaller+=1
                self.nums[smaller], self.nums[bigger]=self.nums[bigger], self.nums[smaller]
        
        self.nums[smaller], self.nums[start] = self.nums[start], self.nums[smaller]
        
        self.sort(start, smaller)
        self.sort(smaller+1, end)
    
    def is_sorted(self, lst):
        """check if the array is sorted or not"""
        return lst == sorted(lst)





count = 0
for i in range(10000):
    nums = [randint(-100000,20000) for _ in range(100) ]   
    quick = Quicksort(nums)
    quick.sort()
    if(quick.is_sorted(quick.nums)):
        count+=1

print(count)