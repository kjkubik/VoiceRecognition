# what is a set? how do you initialize a set?
# we use '{}' to define a set. like this:

set1 = {1,2,3,4,5}
print(type(set1)) # <class 'set'>

# An empty string is defined like this:
string = ''
print(string)
print("String: ", type(string))

# An empty tuple is defined like this: 
tuple = ()
print(tuple)
print("Tuple: ", type(tuple)) # <class 'tuple'>

# An empty list is defined like this: 
list = []
print(list)
print("List: ", type(list)) # <class 'list'>

# BUT an empty set is NOT defined like this: 
set = {}
print(set)
print(type(set)) # <class 'dict'>

# This is how an empty set is defined:
set = set()
print (set) 
print (type(set))


# b = 0
# a = 1
# a = b
# print(type(a))
# print(a)
# print(b)
# considered unordered, cannot access with an index
#            ---------
# unique items are only processed, ignoring duplicate elements
#  fast operations like checking membership, inserting elements, and removing elements.

# This will raise a TypeError because sets are mutable and not hashable.
# set1 = {1, 2, 3}
# set2 = {set1}  # TypeError: unhashable type: 'set'

# A frozenset is an immutable version of a set, and since it's immutable, it is hashable and can be used as an element of another set.
# set1 = frozenset([1, 2, 3])
# set2 = {set1}  # This works because frozenset is immutable and hashable
# print(set2)
# print(type(set1))
# print(type(set2))
# set3={set2}

# stringset = {"cherry", "banana", "apple"}
# print(stringset)
# print(stringset)
# print(stringset)

# numberset = {9,3,1,2,3}
# print(numberset)
# print(numberset)
# print(numberset)
# note that the three isn't considered twice for teh print function

# putting None in the set?
# stringset = {"cherry", None, "banana",  "apple"}
# numberset = {9,3,1,None, 2,3}
# # print(stringset)
# print(numberset)
# is a set reordered after adding None?
# numberset = {9,3,1,2,3}
# print(numberset)
# print(numberset.add(None))
# print(numberset.remove(None))
# print(numberset)

# Why does this happen? This is because None is considered a "smaller" element than other types, so it gets printed first, 
# followed by the other elements in ascending order. Sets in Python are unordered, but when the set is printed or 
# converted to a list, Python places None at the start and sorts the other elements in ascending order.

# # using sorted
# my_set = {5, 2, 8, 1, 3}

# # Convert set to list and sort
# sorted_list = sorted(my_set)

# # Print the sorted list
# print(sorted_list)

# The add method
# set = {1, 2, 3}
# set.add(4)  # {1, 2, 3, 4}
# print(set)

# cannot add something already present
# set = {1, 2, 3}
# set.add(2)  
# print(set)

# The remove method
# set = {1, 2, 3}
# set.remove(2)  # {1, 3}
# print(set)

# you cannot remove something not in the set
# set.remove(4) #KeyError: 4 

# Now that kind of stinks...but we have a method that doesn't do this
# discard will not raise a key error
# let's try it: 
# set = {1, 2, 3}
# set.discard(2)  # {1, 3}
# print(set)
# set.discard(4) 
# print(set) # so use discard when you don't care if the element is present.
# NOTE: this is an "I want to make sure that my set only contains specific elements"

# pop() method
# Removes and returns an arbitrary element from the set. Since sets are unordered, you don’t know which element will be removed.
# NOTE: think random removal and return.
# choreSet = {"sweep", "vacuum", "dishes"}
# choreYourDoing = choreSet.pop()
# print(choreYourDoing)
# print(choreSet)
# choreYourDoing = choreSet.pop()
# print(choreYourDoing)
# print(choreSet)
# choreYourDoing = choreSet.pop()
# print(choreYourDoing)
# print(choreSet)
# What happens if you attempt to pop from an empty set?
# choreYourDoing = choreSet.pop()
# print(choreYourDoing)
# print(choreSet)

# clear method
# set = {1, 2, 3}
# set.clear()
# print (set)
# what happens when you attempt to clear an empty set?
# set.clear()
# print (set)

# copy method - Returns a shallow copy of the set.
# set1 = {1, 2, 3}
# set2 = set.copy(set1)
# print(set2)
# what is a 'shallow' copy and why does it matter?
# It is a copy of an object that duplicates the object itself, but does not recursively copy the objects it contains.
# Note: This can be important when you want a new object, 
# but still want changes in nested objects (like lists within lists)
# to reflect in both the original and the copy.
# print(set1)
# print(set2)
# popSet2 = set2.pop()
# print(set1)
# print(set2) # no difference


#When you create a shallow copy of a set, you get a new set object, but the elements within the set are not copied. Instead, the new set simply contains references to the same objects as the original set.
# original_set = {1, 2, 3, 4}
# shallow_copy = original_set.copy()
# print(id(original_set))
# print(id(shallow_copy))

# print("Original Set:", original_set)
# print("Shallow Copy:", shallow_copy)

# Create a shallow copy of the set
# original_set = {1, 2, (3, 4), 5}
# shallow_copy = original_set.copy()
# print(id(original_set))
# print(id(shallow_copy))

# the set() constructor also creates a shallow copy
# original_set = {1, 2, 3, 4}
# shallow_copy = set(original_set)

# print("Original Set:", original_set)
# print("Shallow Copy:", shallow_copy)

# Both .copy() method and set() constructor will create a new set object 
# that has the same elements as the original set.

# import copy

# Create a set with a mix of immutable and mutable elements
# original_set = {1, 2, (3, 4), [5, 6]} # TypeError: unhashable type: 'list', immutable!

# original_set = {1, 2, (3, 4), (5, 6)}
# # Create a shallow copy of the set
# shallow_copy = copy.copy(original_set)

# print(original_set)
# print(shallow_copy)

# Mutable collections can contain immutable items. 
# my_set = {1, "hello", (2, 3)}
# my_list = [1, "hello", (2, 3)]
# print(my_set)
# print(list)
# while mutable collections can contain immutable items, 
# they cannot contain mutable items (such as lists or dictionaries)
#my_set = {1, "hello", [2, 3]} #TypeError: unhashable type: 'list'

# True: Mutable collections (like lists, sets, and dictionaries) can contain immutable items (like integers, strings, and tuples).
# False: Mutable collections can contain immutable items.
# my_list = [(1,2),{3,4},1]  # no error
# my_set = {[1,2],3,4,1} # TypeError: unhashable type: 'list'
# If you want to create a set with the elements you're trying to use, you must make sure all elements are immutable. 

# Mutable collections (lists, dictionaries) can hold both mutable and 
# immutable items.
# Sets, despite being mutable collections themselves, can only hold 
# immutable items because those items need to be hashable to maintain
# the set's internal structure.

# # Unions
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# set3 = set1.union(set2)  # {1, 2, 3, 4, 5}
# print (set3)
# # Or using the `|` operator:
# set3 = set1 | set2
# print (set3)
# # what happens if I do a union on set1, 2 and 3 now?
# set4 = set1 | set2 | set3
# print(set4)

# intersection (what element(s) are in both sets)
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# set3 = set1.intersection(set2)  # {3}
# # Or using the `&` operator:
# set3 = set1 & set2

# print(set3)

# difference ("What is the difference between set1 and set2?")
# what is in set1 that is not in set2
# set1 = {1, 2, 3}; set2 = {3, 4, 5}
# set3 = set1.difference(set2)  
# # # Or using the `-` operator:
# # set3 = set1 - set2
# print(set3)
# what is in set2 that is not in set1?
# set3 = set2 - set1  
# print (set3)

# Why doesn't this work?
# print ((set1-set2 & set2-set1))

# why does this work?
# print ((set1-set2 | set2-set1))

# a = set1 - set2
# b = set2 - set1
# print(a|b)


# symmetric difference ("give me everything except for what is in both"
# or "how do you get what is not in set1 that is in set2 and not in set2 that is in set1?"
# set1 = {1, 2, 3}; set2 = {3, 4, 5}
# set3 = set1.symmetric_difference(set2)
# print (set3)

# set3 = set2.symmetric_difference(set1)
# print(set3)

# set3 = set1 ^ set2
# print(set3)

# # is subset
# set1 = {1, 2}
# set2 = {1, 2, 3}
# print(set1.issubset(set2))  # True
# print(set2.issubset(set1))  # False

# # is superset
# set1 = {1, 2}
# set2 = {1, 2, 3}
# print(set1.issuperset(set2))  # False
# print(set2.issuperset(set1))  # True

# # isdisjoint()
# set1 = {1, 2, 3}
# set2 = {4, 5, 6}
# print(set1.isdisjoint(set2))  # True

# length function
# set1 = {1, 2, 3}
# set2 = {}
# print(len(set1)) 

# if len(set2) == 0 :
#     print("empty set") 

# # OR

# if not set2:
#     print("The set is empty")
    
    
# in
# my_set = {1, 2, 3, 4, 5}

# Check if an element is in the set
# if 3 in my_set:
#     print("3 is in the set.")
# else:
#     print("3 is not in the set.")

# if 6 in my_set:
#     print("6 is in the set.")
# else:
#     print("6 is not in the set.")

# what is the output of a string to a set?    
# aString = "this is a string that I want to be a set"
# stringSet = set(aString)
# print(stringSet)

# # list to a set output
# list = ["frank", "judy", "mark", "john", "seth", "sid", "mary", "kim", "kendra", "judy"]
# numList = [1,8,10,7,3,9] 
# set = set(list)
# print(set)

# finding the largest element in a set
# print(max(list))
# print(max(numList))

# stringSet = {"frank", "judy", "mark", "john", "seth", "sid", "mary", "kim", "kendra", "judy"}
# numSet = {1,8,10,7,3,9}
# print(max(stringSet))
# print(max(numSet))

# print(min(stringSet))
# print(min(numSet))

# since a set is an iterative data type, how do we iterate over it.

# for x in stringSet: 
#     print(x)
    