"""This is a module for sorting the array using the Inserion sort"""
from random import randrange
import unittest


class InsertionSort():
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
    
    def sort(self):
        """This function sorts the given array using the insertion sort"""
        if(len(self.array)<= 1):
            return self.array
        
        length = len(self)
        for start in range(1,length):
            temp = self.array[start]
            while(start > 0 and temp < self.array[start-1]):
                self.array[start] = self.array[start-1]
                start-=1
            
            self.array[start] = temp 
        
        return self.array
                
                
       


class TestInsertionSort(unittest.TestCase):
    def test_sort_empty_array(self):
        sorter = InsertionSort([])
        sorted_array = sorter.sort()
        self.assertEqual(sorted_array, [])

    def test_sort_single_element(self):
        sorter = InsertionSort([1])
        sorted_array = sorter.sort()
        self.assertEqual(sorted_array, [1])

    def test_sort_sorted_array(self):
        sorter = InsertionSort([1, 2, 3, 4, 5])
        sorted_array = sorter.sort()
        self.assertEqual(sorted_array, [1, 2, 3, 4, 5])

    def test_sort_reverse_array(self):
        sorter = InsertionSort([5, 4, 3, 2, 1])
        sorted_array = sorter.sort()
        self.assertEqual(sorted_array, [1, 2, 3, 4, 5])

    def test_sort_unsorted_array(self):
        sorter = InsertionSort([64, 25, 12, 22, 11])
        sorted_array = sorter.sort()
        self.assertEqual(sorted_array, [11, 12, 22, 25, 64])

    def test_sort_duplicates(self):
        sorter = InsertionSort([4, 2, 2, 3, 3, 1])
        sorted_array = sorter.sort()
        self.assertEqual(sorted_array, [1, 2, 2, 3, 3, 4])

    

                    

if __name__=="__main__":
    arr = [randrange(-10, 100) for i in range(15)] 
    sort = InsertionSort(arr)
    print(f'Before sorting the array is {sort.array}')
    sort.sort()
    print(f'After sorting the array is {sort.array}')
    unit_testing = False | True
    if(unit_testing):
        unittest.main()
        
      
        
    