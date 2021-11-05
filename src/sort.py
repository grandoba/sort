# sort.py

import argparse
from typing import *

def task0():
    print("\n#### TASK 0 ####")
    """
    TASK 0: Sorting a list type + Learning about `key` in `sorted()` function
        A List type has a built-in function called `sort()`. Also the function can set `reverse` to True if the sorted order needs to be reversed.
        Also, the `sorted()` function can be used to sort lists.
    """
    print("\n** Sorting a list with its own attribute function `.sort()`")
    list_of_names = ["eric","tangri","shroof","jeesu"]
    print(f"Original: \t{list_of_names}")
    # Original:  ['eric', 'tangri', 'shroof', 'jeesu']

    list_of_names.sort()
    print(f"Sorted: \t{list_of_names}")
    # Sorted: ['eric', 'jeesu', 'shroof', 'tangri']

    print("\n** Sorting a list with its own attribute function `.sort(reverse=True)`")
    list_of_names = ["eric","tangri","shroof","jeesu"]
    print(f"Original: \t{list_of_names}")
    list_of_names.sort(reverse=True)
    print(f"Sorted: \t{list_of_names}")
    # Sorted: ['tangri', 'shroof', 'jeesu', 'eric']

    print("\n** Sorting using `sorted()` function")
    list_of_names = ["eric","tangri","shroof","jeesu"]
    print(f"Original: \t{list_of_names}")
    ordered = sorted(list_of_names)
    print(f"Sorted: \t{ordered}")

    print("\n** Sorting by the `sorted( key= ... )` function. The `key` function defines with which value to compare elements")
    print("\tHere, we sort by character of index 1 by `key=func` where \n\tdef func(x):\n\t\treturn x[2]")
    print(f"Original: \t{list_of_names}")
    def func(x):
        return x[2]
    ordered = sorted(list_of_names, key=func)
    print(f"Sorted: \t{ordered}")
    print("\nFinal Remarks:\nAs one can see, the `key` is the value to use to order the target iterable object.\nIn other words, if the `key` is a function, the function must return a value")

    # Want to sort a list of custom classes? -> GO TO TASK #?
    # Want to get the index of how the ordered list is made? -> GO TO TASK #?

def task0_a():
    print("\n#### TASK 0-a: Sorted() for dictionaries ####")
    """
    TASK 0-a: sorted() function for dictionary
        The `sorted()` function can take any iterable object and sort the elements. Objects such as a lists, dictionaries, strings, tuples, sets, and even custom iterators could be sorted. This funciton can also take the `reverse` argument to choose whether to sort in ascending (reverse=True) or descending order (reverse=False). By the way, reverse=False is the default value. The biggest difference with the list's built-in `sort()` function is that `sorted()` returns the sorted object. So the returned value must be assigned to a variable to check it.
    """

    # example: dictionary -> GO TO `TASK 0`
    dict_of_names = {}
    dict_of_names["sam"] = "hello"
    dict_of_names["me"] = "yellow"
    dict_of_names["me2"] = "fun"
    print("\n** Sorting a dictionary returns a list of ordered `keys`, not its `values`")
    print(f"Original: \t{dict_of_names}")
    # Original: {'sam': 'hello', 'me': 'yellow', 'me2': 'fun'}

    tmp = sorted(dict_of_names)
    print(f"Sorted: \t{tmp}")
    # Sorted: ['me', 'me2', 'sam']

    print("\n** To sort by the values and get the sorted values, make a list of the values and then sort()")
    tmp = [dict_of_names[x] for x in dict_of_names]
    print(f"Original: \t{tmp}")
    # Original: ['hello', 'yellow', 'fun']
    tmp.sort()
    print(f"Sorted: \t{tmp}")
    #  Sorted: ['fun', 'hello', 'yellow']

    print("\n** To sort by the values and get the sorted keys, make a lambda function")
    tmp = sorted(dict_of_names,key=lambda x: dict_of_names[x])
    print(f"Original: \t{dict_of_names}")
    # Original: {'sam': 'hello', 'me': 'yellow', 'me2': 'fun'}
    print(f"Sorted: \t{tmp}")
    # Sorted: ['me2', 'sam', 'me']

    # Want to sort a cutom iterator? -> GO TO TASK #?
    # 

def task0_b():
    print("\n#### TASK 0-b: Sorted() for strings ####")
    """
    TASK 0-b: sorted() function for strings

    """
    print("\n** Sorting a string makes a list of characters")
    original = "ceafbd"
    print(f"Original: \t{original}")
    # Original: acbdfe
    ordered = sorted(original)
    print(f"Sorted: \t{ordered}")
    # Sorted as a List: ['a', 'b', 'c', 'd', 'e', 'f']
    tmp = ""
    tmp = tmp.join(ordered)
    print(f"Recombined: \t{tmp}")
    # Sorted: abcdef
        
def task0_c():
    print("\n#### TASK 0-c: Sorted() for tuples ####")
    """
    TASK 0-c: sorted() function for tuples
        FYI: lists and tuples could have many different types, but only comparable elements can be sorted. e.g. `int`s and `str`s cannot be sorted if in a list or tuple
        FYI 2: sorted() returns a list always
    """
    print("\n** Sorting single element tuples of the same type")
    original = (3,2,4,1)
    print(f"Original: \t{original}")
    # Original: (3, 2, 4, 1)
    ordered = sorted(original)
    print(f"Sorted: \t{ordered}")
    # Sorted: [1, 2, 3, 4] 
    # As shown above, it's a list (sorted() returns a list always)
    
    print("\n** Sorting a tuple of tuples")
    original = ((1,2,3),(1,2,4),(2,2,3),(2,3,2))
    print(f"Original: \t{original}")
    # Original: ((1, 2, 3), (1, 2, 4), (2, 2, 3), (2, 3, 2))
    ordered = sorted(original)
    print(f"Sorted: \t{ordered}")
    # Sorted: [(1, 2, 3), (1, 2, 4), (2, 2, 3), (2, 3, 2)]
    # As shown above, it returned a list of tuples
    
    print("\n** Sorting a tuple of tuples with different types")
    original = ((1,"a",3),(1,"b",4),(2,"c",3),(2,"d",2))
    print(f"Original: \t{original}")
    # Original: ((1, 'a', 3), (1, 'b', 4), (2, 'c', 3), (2, 'd', 2))
    ordered = sorted(original)
    print(f"Sorted: \t{ordered}")
    # Sorted: [(1, 'a', 3), (1, 'b', 4), (2, 'c', 3), (2, 'd', 2)]
    # As shown above, if a tuple has comparable elements in the same index it can sort.

def task0_d():
    print("\n#### TASK 0-d: Sorted() for sets ####")
    """
    TASK 0-d: sorted() function for sets
        
    """
    print("\n** Sorting sets\n\toriginal = {3,2,4,1} -> automatically sorted")
    original = {3,2,4,1}
    print(f"Original: \t{original}")
    # Original: {1, 2, 3, 4}
    ordered = sorted(original)
    print(f"Sorted: \t{ordered}")
    # Sorted: [1, 2, 3, 4]
    print("\nFinal Remarks:\nsets are naturally ordered in ascending order")


def task1():
    print("\n#### TASK 1: Sorted() with lambda ####")
    """
    TASK 1: sort with lambda

    """
    print("\n** We can sort a list by using a lambda function")    
    print("\t `key = lambda x: -x`")
    orig = [2,5,3,1,4]
    print(f"Original: \t{orig}")
    ordered = sorted(orig,key = lambda x: -x)
    print(f"Sorted: \t{ordered}")
    
    print("\n** We can sort a tuple by using a lambda function")
    print("\t `key = lambda x: x[1]` -> sorting by number")
    orig = (("a",10),("b",3),("c",1))
    print(f"Original: \t{orig}")
    ordered = sorted(orig,key = lambda x: x[1])
    print(f"Sorted: \t{ordered}")

    print("\nFinal Remarks:\nAs you can see, the `x` in `lambda x:` is the element that is accessed by the sorted function")

def task2(): 
    print("\n#### TASK 2: Sorted() with function ####")
    """
    TASK 2: sort with function (instead of lambda)
        According to [this link](https://www.w3schools.com/python/python_lambda.asp#:~:text=A%20lambda%20function%20is%20a,can%20only%20have%20one%20expression.): A lambda function is a small anonymous function.
        So we can use a function to sort also 
    """
    def f_ascend(x):
        return x
    print("\n** We can sort a list by using a function f_ascend")    
    print("\tdef f_ascend:")
    print("\t\treturn x")
    orig = [2,5,3,1,4]
    print(f"Original: \t{orig}")
    ordered = sorted(orig,key=f_ascend)
    print(f"Sorted: \t{ordered}")
    
    print("\n** We can sort a list by using a function f_descend")    
    print("\tdef f_descend:")
    print("\t\treturn -x")
    def f_descend(x):
        return -x
    print(f"Original: \t{orig}")
    ordered = sorted(orig,key=f_descend)
    print(f"Sorted: \t{ordered}")
    
    
    print("\n** Of course, we can also implement complicated rule based sorting")
    print("\tdef f_sort(x):")
    print("\t\treturn ord(x[0]) + x[1]")
    def f_sort(x):
        return ord(x[0]) + x[1]
        
    orig = (("a",10),("a",3),("b",1), ("b",3), ("c",10), ("c",9))
    print(f"Original: \t{orig}")
    ordered = sorted(orig,key=f_sort)
    print(f"Sorted: \t{ordered}")

def task3():
    print("\n#### TASK 3: Sorting a class either by \n\t1: defining __lt__, __eq__\n\t2: create key=function ####")
    """
    TASK 3: sort classes
        if you want to create a class and sort them, you can either ...
            1: implement __lt__ and __eq__ 
            2: implement a key=function(x:custom class)
    """
    class Animal:
        def __init__(self, name:str, num_legs:int, height:float,able2fly:bool):
            self.name = name
            self.num_legs = num_legs
            self.height = height
            self.able2fly = able2fly
        def __repr__(self):
            return repr(f"[{self.name}, {self.num_legs}, {self.height}, {str(self.able2fly)[0]}]")
        def __eq__(self, other: object) -> bool:
            if self.name == other.name and self.num_legs == other.num_legs and self.height == other.height and self.able2fly == other.able2fly:
                return True
            return False
        def __lt__(self, other): ## if (self < other ) return True
            if self.num_legs < other.num_legs:
                return True
            elif self.num_legs > other.num_legs:
                return False
            if self.height < other.height:
                return True
            elif self.height > other.height:
                return False
            if self.name < other.name:
                return True
            elif self.name > other.name:
                return False
            if self.able2fly < other.able2fly:
                return True
            elif self.able2fly > other.able2fly:
                return False
            return False #finishing touch so something is always returned 
 
    animal_1 = Animal("henry",4,0.5,False)      # henry the dog
    animal_2 = Animal("gatos",4,0.2,False)      # gatos the cat
    animal_3 = Animal("whaly",0,8.5,False)       # whaly the whale
    animal_4 = Animal("birdy",2,0.1,True)       # birdy the bird
    animal_5 = Animal("sithe",0,0.1,False)      # sithe the snake
    animal_6 = Animal("speed",2,1.7,True)       # speed the spiderman
    zoo = [animal_1,animal_2,animal_3,animal_4,animal_5,animal_6]

    print("\n** Sorting a list of custom objects is easy if __lt__ and __eq__ is implemented")
    print(f"Original: \t{zoo}")
    new_zoo = sorted(zoo)
    print(f"Sorted: \t{new_zoo}")

    print("\n** Or you could use a function output elements to tuples in the order we would like to sort")
    print("\tdef animal_sort(x:Animal):")
    print("\t\treturn (x.able2fly,x.height,x.num_legs,x.name)")
    def animal_sort(x:Animal):
        return (x.able2fly,x.height,x.num_legs,x.name)
    
    print(f"Original: \t{zoo}")
    new_zoo = sorted(zoo,key=animal_sort)
    print(f"Sorted: \t{new_zoo}")

    print("\n** If you want height to be in reverse order, put a (-) sign on the height attribute")
    print("\tdef animal_sort(x:Animal):")
    print("\t\treturn (x.able2fly,-x.height,x.num_legs,x.name)")
    def animal_sort_v1(x:Animal):
        return (x.able2fly,-x.height,x.num_legs,x.name)
    print(f"Original: \t{zoo}")
    new_zoo = sorted(zoo,key=animal_sort_v1)
    print(f"Sorted: \t{new_zoo}")

def task4():
    print("\n#### TASK 4: Sorted() with operator.itemgetter ####")
    """
    TASK 4: using `itemgetter` of `operator` module 
        Using the `itemgetter` functions from `operator` module is an option. Using them will speed up your sorting algorithm. How does it speed this up? `itemgetter` gets it done at the C level, thus faster performance. [This link](https://www.py4u.net/discuss/17087) shows that there is a 10% increase in performance.  
        
        references
            + https://siddharth1.medium.com/1-understanding-operator-itemgetter-attribute-or-operator-itemgetter-attribute-27e61754d1fa
            + https://www.py4u.net/discuss/17087
    """
    # import operator 
    from operator import itemgetter

    print("\n** operator.itemgetter(i) returns the item in the ith index or the value that corresponds to key i if it is a dictionary")
    print("\tSort by index 0 or index 1")
    orig = [[3,6],[2,7],[1,8]]
    print(f"Original: \t{orig}")
    ordered = sorted(orig,key=itemgetter(0))
    print(f"Sorted (by 0): \t{ordered}")
    ordered = sorted(orig,key=itemgetter(1))
    print(f"Sorted (by 1): \t{ordered}")

    print(f"\n** itemgetter can get multiple items too")
    print("\tindex order in 2, 0, 1")
    orig = [[1,1,1],[1,1,2],[1,1,3],[1,2,1],[1,2,3],[1,3,1],[1,3,4]]
    print(f"Original: \t{orig}")
    ordered = sorted(orig,key=itemgetter(2,0,1))
    print(f"Sorted: \t{ordered}")


def task5():
    print("\n#### TASK 5: Sorted() with operator.attrgetter ####")
    """
    TASK 5: using `attrgetter` of `operator` module

    """
    from operator import attrgetter

    class Animal:
        def __init__(self, name:str, num_legs:int, height:float,able2fly:bool):
            self.name = name
            self.num_legs = num_legs
            self.height = height
            self.able2fly = able2fly
        def __repr__(self):
            return repr(f"[{self.name}, {self.num_legs}, {self.height}, {str(self.able2fly)[0]}]")
        # def __iter__(self):
        #     return self
        # def __next__(self):
        #     return 0
        
    animal_1 = Animal("henry",4,0.5,False)      # henry the dog
    animal_2 = Animal("gatos",4,0.2,False)      # gatos the cat
    animal_3 = Animal("whaly",0,8.5,False)       # whaly the whale
    animal_4 = Animal("birdy",2,0.1,True)       # birdy the bird
    animal_5 = Animal("sithe",0,0.1,False)      # sithe the snake
    animal_6 = Animal("speed",2,1.7,True)       # speed the spiderman
    zoo = [animal_1,animal_2,animal_3,animal_4,animal_5,animal_6]
    
    print("\n** Sorting by key=operator.attrgetter('name')")
    print(f"Original: \t{zoo}")
    ordered = sorted(zoo,key=attrgetter("name"))
    print(f"Sorted: {ordered}")

    print("\n** `attrgetter` can also get multiple attributes")
    print("\tkey=attrgetter('able2fly','num_legs','name')")
    print(f"Original: \t{zoo}")
    ordered = sorted(zoo,key=attrgetter('able2fly','num_legs',"name"))
    print(f"Sorted: \t{ordered}")


def task6():
    print("\n#### TASK 6: Sorted() for a Class with __iter__ and __next__ implemented ####")
    """
    TASK 6: defining class __iter__ or __next__ to sort
        According to [this link](https://stackabuse.com/sorting-algorithms-in-python/), 
            "The sorted() function can sort any iterable object and that includes - lists, strings, tuples, dictionaries, sets, and custom iterators you can create."
        In cases where you want to sort items that are within one class object, you can define __iter__ and __next__ to sort them. This method is useful when loading the entire database to a list is troublesome, perhaps b/c the data size is too big.   
    """

    class Numbers:
        def __init__(self, nums):
            self.nums = nums

        def __iter__(self):
            self.it = 0
            return self

        def __next__(self):
            # if(self.num >= self.max):
                # raise StopIteration
            self.it += 1
            if (self.it > len(self.nums)):
                raise StopIteration
            return self.nums[self.it-1]

    original = Numbers([4,1,5,3,2])

    # for x in print_num.nums:
    #     print(x, end="-")
    print("\n**Sorting a single class object Numbers -> original = Numbers([4,1,5,3,2])")
    print(f"Original: \t{original.nums}")
    k = sorted(original)
    print(f"Sorted: \t{k}")

    print("\n**But it is always easier to just sorted() the list itself like `sorted(original.nums)`")
    k = sorted(original.nums)
    print(f"Sorted: \t{k}")

def task7():
    print("\n#### TASK 7: Sorted() for a Class with __iter__ and __next__ implemented ####")
    """
    TASK 7: An old but traditional way to sort    
    """

    print("\n** Sorting students by using enumerate to get the newly sorted idx order")
    student_objects = [('john', 'C', 15), ('jane', 'B', 12), ('dave', 'A', 10)]
    print(f"Original: \t{student_objects}")
    decorated = [(student[1], i, student) for i, student in enumerate(student_objects)]
    decorated.sort()
    ans = [student for grade, i, student in decorated]               # undecorate
    print(f"Sorted: \t{ans}")
    # [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)] 

    # But this can be also done by enumerate and zip!!!


# Work in Progress
def _task8():
    """
    When you are exclusively using numbers, using numpy to sort is an option.
    What advantages does this have? 
        Aspect 1: Speed     [List speed, numpy speed]
            + 10x10     matrix  -> []
            + 100x100   matrix  -> []
            + 1000x1000 matrix  -> []
    """ 
    import numpy as np
    # sorting tensors with numpy
    

    # sorting according to a certain row or column



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Choose a sorting method ID = [0, 0_a, 0_b, 0_c, 0_d, 1, 2, 3, 4, 5, 6, 7]')
    parser.add_argument('taskID', metavar='ID', type=str,
                        help='the task id to choose')
    args = parser.parse_args()

    # print('Running task' + args.taskID)

    if args.taskID == '0':
        task0()
    elif args.taskID == '0_a':
        task0_a()
    elif args.taskID == '0_b':
        task0_b()
    elif args.taskID == '0_c':
        task0_c()
    elif args.taskID == '0_d':
        task0_d()
    elif args.taskID == '1':
        task1()
    elif args.taskID == '2':
        task2()
    elif args.taskID == '3':
        task3()
    elif args.taskID == '4':
        task4()
    elif args.taskID == '5':
        task5()
    elif args.taskID == '6':
        task6()
    elif args.taskID == '7':
        task7()
    else:
        print("Choose an ID in the list shown in `python3 sort.py -h`")