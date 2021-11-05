# sort.py
# https://wiki.python.org/moin/HowTo/Sorting/

# FINDING ALL WAYS TO SORT! 
# WRITE ABOUT SORT() IN REAL DEPTH
import argparse
from operator import attrgetter
from typing import *

# sorting a list
# sorting a dictionary
# sorting a list of classes

class Person:
    def __init__(self, name :str, room_num :int):
        self.name = name
        self.room = []
        self.room.append(room_num)
        self.room0 = room_num 
        self.num_rooms = 1
    def __repr__(self):
        return repr((self.name,f"size: {self.num_rooms}", [x for x in self.room]))

class People:
    def __init__(self):
        self.num_of_people = 0
        self.names : List(Person) = [] 
    def __repr__(self):
        return repr((f"{self.num_of_people} people ->",[x for x in self.names]))
    def add_person(self, name, room_num):
        for pers in self.names:
            if pers.name == name:
                pers.room.append(room_num)
                pers.num_rooms +=1
                return
        self.names.append(Person(name,room_num))
        self.num_of_people += 1


def task0():
    print("\n\n#### TASK 0 ####")
    """
    TASK 0: Sorting a list type
        A List type has a built-in function called `sort()`. Also the function can set `reverse` to True if the sorted order needs to be reversed.
        Also, the `sorted()` function can be used to sort lists.
    """
    list_of_names = ["eric","tangri","shroof","jeesu"]
    print(f"Original: {list_of_names}")
    # Original:  ['eric', 'tangri', 'shroof', 'jeesu']

    list_of_names.sort()
    print(f"Sorted: {list_of_names}")
    # Sorted: ['eric', 'jeesu', 'shroof', 'tangri']

    list_of_names.sort(reverse=True)
    print(f"Sorted in reverse: {list_of_names}")
    # Sorted in reverse: ['tangri', 'shroof', 'jeesu', 'eric']

    print("sorting using `sorted()` function")
    ordered = sorted(list_of_names)
    print(f"sorted: {ordered}")

    print("The `sorted()` function can take a `key` function that defines with which value to compare elements")
    print(f"Original: {list_of_names}")
    def func(x):
        return x[2]
    ordered = sorted(list_of_names, key=func)
    print(f"sorted (by 2nd index character): {ordered}")
    print("As one can see, the `key` is the value to use to order the target iterable object.\nIn other words, if the `key` is a function, the function must return a value")

    # Want to sort a list of custom classes? -> GO TO TASK #?
    # Want to get the index of how the ordered list is made? -> GO TO TASK #?

def task0_a():
    print("\n\n#### TASK 0-a: Sorted() for dictionaries ####")
    """
    TASK 0-a: sorted() function for dictionary
        The `sorted()` function can take any iterable object and sort the elements. Objects such as a lists, dictionaries, strings, tuples, sets, and even custom iterators could be sorted. This funciton can also take the `reverse` argument to choose whether to sort in ascending (reverse=True) or descending order (reverse=False). By the way, reverse=False is the default value. The biggest difference with the list's built-in `sort()` function is that `sorted()` returns the sorted object. So the returned value must be assigned to a variable to check it.
    """

    # example: dictionary -> GO TO `TASK 0`
    dict_of_names = {}
    dict_of_names["sam"] = "hello"
    dict_of_names["me"] = "yellow"
    dict_of_names["me2"] = "fun"
    print("\nSorting a dictionary returns a list of ordered `keys`, not its `values`")
    print(f"Original: {dict_of_names}")
    # Original: {'sam': 'hello', 'me': 'yellow', 'me2': 'fun'}

    tmp = sorted(dict_of_names)
    print(f"Sorted: {tmp}")
    # Sorted: ['me', 'me2', 'sam']

    print("\nTo sort by the values, and get the sorted values")
    tmp = [dict_of_names[x] for x in dict_of_names]
    print(f"Original: {tmp}")
    # Original: ['hello', 'yellow', 'fun']
    tmp.sort()
    print(f"Sorted: {tmp}")
    #  Sorted: ['fun', 'hello', 'yellow']

    print("\nTo sort by the values and get the sorted keys, make a lambda function\n")
    tmp = sorted(dict_of_names,key=lambda x: dict_of_names[x])
    print(f"Original: {dict_of_names}")
    # Original: {'sam': 'hello', 'me': 'yellow', 'me2': 'fun'}
    print(f"Sorted: {tmp}")
    # Sorted: ['me2', 'sam', 'me']
         

    # Want to sort a cutom iterator? -> GO TO TASK #?
    # 

def task0_b():
    print("\n\n#### TASK 0-b: Sorted() for strings ####")
    """
    TASK 0-b: sorted() function for strings

    """

    original = "acbdfe"
    print(f"Original: {original}")
    # Original: acbdfe
    ordered = sorted(original)
    print(f"Sorted as a List: {ordered}")
    # Sorted as a List: ['a', 'b', 'c', 'd', 'e', 'f']
    tmp = ""
    tmp = tmp.join(ordered)
    print(f"Sorted: {tmp}")
    # Sorted: abcdef
        
def task0_c():
    print("\n\n#### TASK 0-c: Sorted() for tuples ####")
    """
    TASK 0-c: sorted() function for tuples
        FYI: lists and tuples could have many different types, but only comparable elements can be sorted. e.g. `int`s and `str`s cannot be sorted if in a list or tuple
        FYI 2: sorted() returns a list always
    """
    print("sorting single element tuples of same type")
    original = (3,2,4,1)
    print(f"Original: {original}")
    # Original: (3, 2, 4, 1)
    ordered = sorted(original)
    print(f"Sorted: {ordered}")
    # Sorted: [1, 2, 3, 4] 
    # As shown above, it's a list (sorted() returns a list always)
    
    print("sorting a tuple of tuples")
    original = ((1,2,3),(1,2,4),(2,2,3),(2,3,2))
    print(f"Original: {original}")
    # Original: ((1, 2, 3), (1, 2, 4), (2, 2, 3), (2, 3, 2))
    ordered = sorted(original)
    print(f"Sorted: {ordered}")
    # Sorted: [(1, 2, 3), (1, 2, 4), (2, 2, 3), (2, 3, 2)]
    # As shown above, it returned a list of tuples
    
    print("sorting a tuple of tuples with different types")
    original = ((1,"a",3),(1,"b",4),(2,"c",3),(2,"d",2))
    print(f"Original: {original}")
    # Original: ((1, 'a', 3), (1, 'b', 4), (2, 'c', 3), (2, 'd', 2))
    ordered = sorted(original)
    print(f"Sorted: {ordered}")
    # Sorted: [(1, 'a', 3), (1, 'b', 4), (2, 'c', 3), (2, 'd', 2)]
    # As shown above, if a tuple has comparable elements in the same index it can sort.

def task0_d():
    print("\n\n#### TASK 0-d: Sorted() for sets ####")
    """
    TASK 0-d: sorted() function for sets
        
    """
    print("sorting sets")
    original = {3,2,4,1}
    print(f"Original <3,2,4,1>: {original}")
    # Original: {1, 2, 3, 4}
    ordered = sorted(original)
    print(f"Sorted: {ordered}")
    # Sorted: [1, 2, 3, 4]
    print("sets are naturally ordered in ascending order")


def task1():
    """
    TASK 1: sort with lambda

    """
    print("We can sort a list by using a lambda function")    
    orig = [2,5,3,1,4]
    print(f"Original: {orig}")
    ordered = sorted(orig,key= lambda x: -x)
    print(f"Sorted (reversed): {ordered}")
    
    print("We can sort a tuple by using a lambda function")
    orig = (("a",10),("b",3),("c",1))
    print(f"Original: {orig}")
    ordered = sorted(orig,key= lambda x: x[1])
    print(f"Sorted (by number): {ordered}")

    print("As you can see, the `x` in `lambda x:` is the element that is accessed by the sorted function")

def task2(): 
    """
    TASK 2: sort with function instead of lambda
        According to [this link](https://www.w3schools.com/python/python_lambda.asp#:~:text=A%20lambda%20function%20is%20a,can%20only%20have%20one%20expression.): A lambda function is a small anonymous function.
        So we can use a function to sort also 
    """
    def f_ascend(x):
        return x
    print("We can sort a list by using a function f_ascend")    
    orig = [2,5,3,1,4]
    print(f"Original: {orig}")
    ordered = sorted(orig,key=f_ascend)
    print(f"Sorted (f_ascend): {ordered}")
    
    def f_descend(x):
        return -x
    print("Of course, we can also sort with f_descend")
    print(f"Original: {orig}")
    ordered = sorted(orig,key=f_descend)
    print(f"Sorted (f_descend): {ordered}")
    
    
    print("Of course, we can also implement complicated rule based sorting")
    def f_sort(x):
        return ord(x[0]) + x[1]
        

    orig = (("a",10),("a",3),("b",1), ("b",3), ("c",10), ("c",9))
    print(f"Original: {orig}")
    ordered = sorted(orig,key=f_sort)
    print(f"Sorted (by ord(char) + number): {ordered}")

def task3():
    """
    TASK 3: sort classes
        if you want to create a class and sort them
    """
    class Animal:
        def __init__(self, name:str, num_legs:int, height:float,able2fly:bool):
            self.name = name
            self.num_legs = num_legs
            self.height = height
            self.able2fly = able2fly
        def __repr__(self):
            return repr(f"[{self.name}, {self.num_legs}, {self.height}, {self.able2fly}]")
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
 
    animal_1 = Animal("henry",4,0.5,False)  # henry the dog
    animal_2 = Animal("gato",4,0.2,False)   # gado the cat
    animal_3 = Animal("whaly",0,10,False)   # whaly the whale
    animal_4 = Animal("birdy",2,0.1,True)  # birdy the bird
    animal_5 = Animal("slitherin",0,0.1,False)  # slitherin the snake
    animal_6 = Animal("spiderman",2,1.7,True)  # Spiderman the spiderman
    zoo = [animal_1,animal_2,animal_3,animal_4,animal_5,animal_6]

    print(f"Original: {zoo}")
    new_zoo = sorted(zoo)
    print(f"Sorted: {new_zoo}")

    print("Or you could use a function output elements to tuples in the order we would like to sort")
    def animal_sort(x:Animal):
        return (x.able2fly,x.height,x.num_legs,x.name)
    
    print(f"Original: {zoo}")
    new_zoo = sorted(zoo,key=animal_sort)
    print(f"Sorted: {new_zoo}")

    print("if you want height to be in reverse order, put a (-) sign on the height attribute")
    def animal_sort_v1(x:Animal):
        return (x.able2fly,-x.height,x.num_legs,x.name)
    print(f"Original: {zoo}")
    new_zoo = sorted(zoo,key=animal_sort_v1)
    print(f"Sorted: {new_zoo}")

def task4():
    """
    TASK 4: using `itemgetter` of `operator` module 
        Using the `itemgetter` functions from `operator` module is an option. Using them will speed up your sorting algorithm. How does it speed this up? `itemgetter` gets it done at the C level, thus faster performance. [This link](https://www.py4u.net/discuss/17087) shows that there is a 10% increase in performance.  
        
        references
            + https://siddharth1.medium.com/1-understanding-operator-itemgetter-attribute-or-operator-itemgetter-attribute-27e61754d1fa
            + https://www.py4u.net/discuss/17087
    """
    # import operator 
    from operator import itemgetter

    print("operator.itemgetter(i) returns the item in the ith index or the value that corresponds to key i if it is a dictionary")
    orig = [[3,6],[2,7],[1,8]]
    print(f"Original: {orig}")
    ordered = sorted(orig,key=itemgetter(0))
    print(f"Sorted (by 0th index): {ordered}")
    ordered = sorted(orig,key=itemgetter(1))
    print(f"Sorted (by 1th index): {ordered}")

    print(f"itemgetter can get multiple items too")
    orig = [[1,1,1],[1,1,2],[1,1,3],[1,2,1],[1,2,3],[1,3,1],[1,3,4]]
    print(f"Original: {orig}")
    ordered = sorted(orig,key=itemgetter(2,0,1))
    print(f"Sorted (by 2nd, 0th, 1st index): {ordered}")

    # print("\noperator.attrgetter(string) returns the attribute 'string'. Again, multiple attributes can be returned")
    # print(f"People: {peep}")
    # ordered = sorted(peep, key=attrgetter('name'))
    # print(f"sorted (by names): {ordered}")


def task5():
    """
    TASK 5: using `attrgetter` of `operator` module

    """
    class Animal:
        def __init__(self, name:str, num_legs:int, height:float,able2fly:bool):
            self.name = name
            self.num_legs = num_legs
            self.height = height
            self.able2fly = able2fly
        def __repr__(self):
            return repr(f"[{self.name}, {self.num_legs}, {self.height}, {self.able2fly}]")
        # def __iter__(self):
        #     return self
        # def __next__(self):
        #     return 0
        
    animal_1 = Animal("henry",4,0.5,False)  # henry the dog
    animal_2 = Animal("gato",4,0.2,False)   # gado the cat
    animal_3 = Animal("whaly",0,10,False)   # whaly the whale
    animal_4 = Animal("birdy",2,0.1,True)  # birdy the bird
    animal_5 = Animal("slitherin",0,0.1,False)  # slitherin the snake
    animal_6 = Animal("spiderman",2,1.7,True)  # Spiderman the spiderman
    zoo = [animal_1,animal_2,animal_3,animal_4,animal_5,animal_6]
    
    print(f"Original: {zoo}")
    ordered = sorted(zoo,key=attrgetter("name"))
    print(f"sorted (by name): {ordered}")
    print("`attrgetter` can also get multiple attributes")
    print(f"Original: {zoo}")
    ordered = sorted(zoo,key=attrgetter('able2fly','num_legs',"name"))
    print(f"sorted (by able2fly, num_legs, name): {ordered}")


def task6():
    """
    TASK 6: defining class __iter__ or __next__ to sort
        According to [this link](https://stackabuse.com/sorting-algorithms-in-python/), 
            "The sorted() function can sort any iterable object and that includes - lists, strings, tuples, dictionaries, sets, and custom iterators you can create."
        In cases where you want to sort items that are within one class object, you can define __iter__ and __next__ to sort them. This method is useful when loading the entire database to a list is troublesome, perhaps b/c the data size is too big.   
    """
    
    print_num = Numbers([4,1,5,3,2])

    for x in print_num.nums:
        print(x, end="-")

    k = sorted(print_num)
    print(k)
    # But it is always easier to just sorted() the list itself like below
    k = sorted(print_num.nums)
    print(k)

def task7():
    """
    TASK 7: Defining   
    """

def _task32():
    """
    TASK 3: sort by name (alphabetic order) -> Using lambda to access each element's attribute

    """
    peep = People()
    peep.add_person("Jake", 403)
    peep.add_person("Newt", 404)
    peep.add_person("Frap", 104)
    peep.add_person("Jake", 203)
    # for idx, person in enumerate(peep.names):
    #     print(f"Person no.{idx}: [{person.name}] is in rooms {[x for x in person.room]}")
    # print(f"Oringinal: {peep}")

    peep.names = sorted(peep.names, key= lambda x: x.name)

    # 
    # Option 1: using `sorted`
    # peep.names = sorted(peep.names, key= lambda x: x.name)
    # Option 2: using .sort to a list object
    # peep.names.sort(key=lambda x:x.name)
    # Option 3: using module `operator` 
    # peep.names.sort(key=operator.attrgetter('name'))
    
    # TASK 2: sort by name (alphabetic order) -> Using a function
    def reverse_alphabet(person_info : Person):
        return person_info.name
    task2 = sorted(peep.names,key=reverse_alphabet)
    print("As one can see, the `key` is the value to use to order the target iterable object.\nIn other words, if the `key` is a function, the function must return a value")
    print("task2:",task2)
    # TASK 2-1: sort by name (reverse alphabetic order) -> Using a function
    task2 = sorted(peep.names,key=reverse_alphabet,reverse=True)
    print("task2 (reversed):",task2)
    
    # Ordering first by multiple values (sort by attribute A -> attribute B -> attribute C)
    task2 = sorted(peep.names,key=operator.attrgetter("name","num_rooms")) 
    print("task2 (multi level sort using operator) -> name -> num_rooms:\n",task2)
    task2 = sorted(peep.names,key=operator.attrgetter("num_rooms","name")) 
    print("task2 (multi level sort using operator) -> num_rooms -> name:\n",task2)

    # But, what if you didn't want to sort by the attribute num_rooms, but do it by `rooms.size()`? 
    # Then, you would have to use a funciton.
    def func1(person_info: Person):
        return len(person_info.room)
    task2 = sorted(peep.names,key=func1) 
    print("task2 (sort using function):",task2)

    # Sort with multiple attributes with funcitons
    def func2(person_info: Person):
        return [len(person_info.room), person_info.name]
    task2 = sorted(peep.names,key=func2) 
    print("task2 (sort using function):",task2)

    # HOW TO SORT A DICTIONARY THEN?
    # "a"<"b"
    # itemgetter gets ith item (e.g. With a = [1,2], a[0] == 1. Also, getit = operator.itemgetter(0); getit(a) == 1) 
    # methodgetter gets the method ... etc etc

    # TASK 3: Sort by multiple values but some of them in reverse order! 
    # sort by # of rooms (more first) + sort by room number (smaller first)
    # By putting a (-) sign to numeric values, we can reverse the order
    # for strings, would putting a (-) sign work? -->  NO THIS DOESN'T WORK
    # But according to this link(https://www.tutorialsteacher.com/articles/compare-strings-in-python),
    #   characters are compared using the unicode value which could be found using the ord() function
    #   But ord() only takes in a single character so we construct a list
    def func2(person_info: Person):
        return [-len(person_info.room), [ord(x) for x in person_info.name]]
    task2 = sorted(peep.names,key=func2) 
    print("task2 (sort using function):",task2)
    
    
    # sorted()
    for idx, person in enumerate(peep.names):
        print(f"Person no.{idx}: [{person.name}] is in rooms {[x for x in person.room]}")

    # TASK 3: sort by ()
    sorted()
    for idx, person in enumerate(peep.names):
        print(f"Person no.{idx}: [{person.name}] is in rooms {[x for x in person.room]}")


    # An old way
    # decorated = [(student.grade, i, student) for i, student in enumerate(student_objects)]
    # decorated.sort()
    # ans = [student for grade, i, student in decorated]               # undecorate
    # [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)] 

    # But this can be also done by enumerate and zip!!!


# class Animal:
#     def __init__(self, name:str, num_legs:int, height:float,able2fly:bool):
#         self.name = name
#         self.num_legs = num_legs
#         self.height = height
#         self.able2fly = able2fly
#     def __iter__(self):
#         return 

#     def __next__(self):

#     def __repr__(self):
#         return repr()

class PrintNumber:
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if(self.num >= self.max):
            raise StopIteration
        self.num += 1
        return self.num

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


def _task4():
    # TASK 4: Using __iter__ and __next__ to iterate 
    #   According to [this link](https://stackabuse.com/sorting-algorithms-in-python/), 
    #       "The sorted() function can sort any iterable object and that includes - lists, strings, tuples, dictionaries, sets, and custom iterators you can create."
    #       So creating an __iter__ and __next__ will make it easy to sort a custom class
    #   Let's demonstrate with an example.

    print_num = Numbers([4,1,5,3,2])

    for x in print_num.nums:
        print(x, end="-")

    k = sorted(print_num)
    print(k)
    # But it is always easier to just sorted() the list itself like below
    k = sorted(print_num.nums)
    print(k)

def _task5():
    """
    How to make a custom class comparable

    
    references: 
        + https://www.pythonpool.com/python-__lt__/


    """
    class CompareClasses:
        def __init__(self, weight:int, value:int):
            self.w = weight # from 0 to 1
            self.v = value  # from -10 to 10
        def __lt__(self, other): ## <
            return self.w*self.v < other.w*other.v
        def __eq__(self, other):
            return self.w*self.v == other.w*other.v
        # object.__le__(self, other)
        # object.__ne__(self, other)
        # object.__gt__(self, other)
        # object.__ge__(self, other)
    weightNvalue1 = CompareClasses(0.5,10)
    weightNvalue2 = CompareClasses(1,4)
    print(weightNvalue1<weightNvalue2)

    m = [weightNvalue1, weightNvalue2]
    for n in m:
        print((n.w,n.v),end=" ")
    print()
    m = sorted(m)
    for n in m:
        print((n.w,n.v),end=" ")
    print()

def _task6():
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
    parser = argparse.ArgumentParser(description='Choose a sorting method ID = [0, 0_a, 0_b, 0_c, 0_d, 1, 2, 3, 4, 5, 6]')
    
    parser.add_argument('taskID', metavar='ID', type=str,
                        help='the task id to choose')
    args = parser.parse_args()

    print('Running task' + args.taskID)

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