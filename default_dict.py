#use defaultdict when you want to have a default value either int or set or list, even though there are other way to do.
from collections import defaultdict
from random import randint


def dict_creation(n=20):
    occurences = defaultdict(list)
    for _ in range(20):
        number = randint(0,10)
        occurences[number].append(number)
    print(occurences)
    
    
if __name__=="__main__":
    dict_creation()
