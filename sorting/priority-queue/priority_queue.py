"""This module implements priority queue which implements the queue with priority"""
from random import randint

class Heap():
    """Implements all the functionality related to the heap functions"""
    def __init__(self, values) -> None:
        self.values = values
        
    def __len__(self):
        return len(self.values)
    
    
    def heapification(self, index):
        """does the heapification for the given index"""
        length  = len(self)
        if(index >= length):
            return 
        
        node_value = self.values[index]
        left_child = (2 * index ) + 1 
        right_child = (2 * index ) + 2
        left_value = float('-inf')
        right_value = float('-inf')
        if(left_child < length):
            left_value = self.values[left_child]
            
        if(right_child < length):
            right_value = self.values[right_child]
            
        if(left_value > right_value and left_value > node_value):
            self.values[index], self.values[left_child]=self.values[left_child], self.values[index]
            self.heapification(left_child)
        elif(right_value > left_value and right_value > node_value):
            self.values[index], self.values[right_child]=self.values[right_child], self.values[index]
            self.heapification(right_child)
        else:
            return
                
            
    
    
    def heapify(self):
        """This function does the heapification of the queue"""
        length = len(self)
        for index in range(length-1, -1, -1):
            self.heapification(index)
        
    def insert_heapification(self,index):
        """does the heapification for the inserted value at the final index from leaf to root.."""
        value = self.values[index]
        if(index <=0):
            return 
        parent_index = (index-1) // 2
        if(self.values[parent_index] < value):
            self.values[parent_index], self.values[index] =  self.values[index],  self.values[parent_index]
            self.insert_heapification(parent_index)
        else:
            return
    
         
    
    def insert(self, value):
        """inserts the value into heap"""
        self.values.append(value)
        index = len(self)-1
        self.insert_heapification(index)
        
    
    def extract_max(self):
        """Extracts the maxmimum value from the queue"""
        max_value = self.values[0]
        end_value =self.values.pop()
        if(len(self.values) > 0):
            self.values[0] = end_value
            self.heapification(0)
        return max_value
    

if __name__=="__main__":
    temp = [randint(0,10000) for _ in range(10)]
    print(temp)
    heap = Heap(temp)
    heap.heapify()
    print(heap.values)    
    heap.insert(1000000)
    print(heap.values)    

    # for _ in range(11):
    #     print(heap.extract_max())
        

 