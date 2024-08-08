"""This is a module for sorting the array using the selection sort"""
from random import randrange
import unittest


class SelectionSort():
    """Class Which represents the Selection sort"""
    
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
        """This function sorts the given array"""
        length =len(self)
        for outer in range(length):
            minimum = outer
            for inner in range(outer+1, length):
                if(self.array[inner] < self.array[minimum]):
                    minimum = inner 
            
            self.array[minimum], self.array[outer] = self.array[outer], self.array[minimum]

        return self.array


class TestSelectionSort(unittest.TestCase):
    def test_sort_empty_array(self):
        sorter = SelectionSort([])
        sorted_array = sorter.sort()
        self.assertEqual(sorted_array, [])

    def test_sort_single_element(self):
        sorter = SelectionSort([1])
        sorted_array = sorter.sort()
        self.assertEqual(sorted_array, [1])

    def test_sort_sorted_array(self):
        sorter = SelectionSort([1, 2, 3, 4, 5])
        sorted_array = sorter.sort()
        self.assertEqual(sorted_array, [1, 2, 3, 4, 5])

    def test_sort_reverse_array(self):
        sorter = SelectionSort([5, 4, 3, 2, 1])
        sorted_array = sorter.sort()
        self.assertEqual(sorted_array, [1, 2, 3, 4, 5])

    def test_sort_unsorted_array(self):
        sorter = SelectionSort([64, 25, 12, 22, 11])
        sorted_array = sorter.sort()
        self.assertEqual(sorted_array, [11, 12, 22, 25, 64])

    def test_sort_duplicates(self):
        sorter = SelectionSort([4, 2, 2, 3, 3, 1])
        sorted_array = sorter.sort()
        self.assertEqual(sorted_array, [1, 2, 2, 3, 3, 4])

    

                    

if __name__=="__main__":
    arr = [randrange(-10, 100) for i in range(15)] 
    sort = SelectionSort(arr)
    print(f'Before sorting the array is {sort.array}')
    sort.sort()
    print(f'After sorting the array is {sort.array}')
    unit_testing = False | True
    if(unit_testing):
        unittest.main()
        
      
        
    