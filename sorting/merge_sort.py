"""This is module which implements the merge sort algorithm"""
from random import randrange
import sys
import unittest



class MergeSort():
    """Class Which represents the Insertion sort"""
    
    def __init__(self, array, sorted_arr = False):
        self.array = array
        self._sorted_arr = False
    
    def __str__(self):
        return f'Array({self.array})'
    
    @property
    def sorted(self):
        return self._sorted_arr
    
    @sorted.setter
    def sorted(self, value):
        if self._sorted_arr is False and value is True:
            self._sorted_arr = value
        else:
            raise ValueError('Array is already sorted, you can set value once it is in sorted order')
    
    def __len__(self):
        return len(self.array)

    def divide(self, start, end):
        if(end-start <= 1 ):
            return 
        
        mid = start + ((end - start) //2)
        self.divide(start, mid) # 0-5 > 0-2 > 0-1 > 
        self.divide(mid, end)
        left = start ; right=mid
        #left array from arr[start:mid] & right array from arr[mid:end]
        #divide phase is done and combine them based on the sorting
        self.output = []
        print(f' left = {self.array[start:mid]}, right={self.array[mid:end]}')
        while(left < mid and right < end):
            if(self.array[left] <= self.array[right]):
                self.output.append(self.array[left])
                left+=1
            else:
                self.output.append(self.array[right])
                right+=1
                
        while(left < mid):
            self.output.append(self.array[left])
            left+=1
        
        while(right < end):
            self.output.append(self.array[right])
            right+=1
        
        index = 0
        for org_index in range(start, end):
            self.array[org_index] = self.output[index]
            index+=1
        
        print(f'start={start}, end= {end} , sorted= {self.array[start:end]}')
        
    def sort(self):
        """This function sorts the given array using the insertion sort"""
        if(len(self.array)<= 1):
            return self.array
        
        length = len(self)
        self.divide(start= 0, end = length)
        return self.array
        self.sorted = True




class TestMergeSort(unittest.TestCase):
    def test_sort_empty_array(self):
        sorter = MergeSort([])
        sorted_array = sorter.sort()
        self.assertEqual(sorted_array, [])

    def test_sort_single_element(self):
        sorter = MergeSort([1])
        sorted_array = sorter.sort()
        self.assertEqual(sorted_array, [1])

    def test_sort_sorted_array(self):
        sorter = MergeSort([1, 2, 3, 4, 5])
        sorted_array = sorter.sort()
        self.assertEqual(sorted_array, [1, 2, 3, 4, 5])

    def test_sort_reverse_array(self):
        sorter = MergeSort([5, 4, 3, 2, 1])
        sorted_array = sorter.sort()
        self.assertEqual(sorted_array, [1, 2, 3, 4, 5])

    def test_sort_unsorted_array(self):
        sorter = MergeSort([64, 25, 12, 22, 11])
        sorted_array = sorter.sort()
        self.assertEqual(sorted_array, [11, 12, 22, 25, 64])

    def test_sort_duplicates(self):
        sorter = MergeSort([4, 2, 2, 3, 3, 1])
        sorted_array = sorter.sort()
        self.assertEqual(sorted_array, [1, 2, 2, 3, 3, 4])

    

        

if __name__=="__main__":
    arr = [randrange(-10, 100) for i in range(20)] 
    sort = MergeSort(arr)
    print(f'Before sorting the array is {sort.array}')
    sort.sort()
    print(f'After sorting the array is {sort.array}')
    unit_testing = False | True
    if(unit_testing):
        unittest.main()
        
 
 