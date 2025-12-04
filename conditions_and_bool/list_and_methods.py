"""
Lecture: Python Lists — Creation, Indexing, Slicing, Basic Methods

=======================================================
1. WHAT IS A LIST?
=======================================================
A list in Python is an ordered, changeable (mutable) collection of items.
Lists can store different data types: numbers, strings, booleans, etc.

Examples:
numbers = [1, 2, 3]
mixed = ["apple", 10, True]

Lists are created using square brackets: [ ]
"""

print("=== Creating Lists ===")

numbers = [10, 20, 30, 40]
foods = ["pizza", "pasta", "salad"]

print(numbers)
print(foods)


"""
=======================================================
2. ACCESSING ELEMENTS (INDEXING)
=======================================================
Each element in a list has an index.
Index starts from 0.

my_list[0] → first element
my_list[1] → second element
my_list[-1] → last element (negative indexing)
"""

print("\n=== Indexing ===")

my_list = ["a", "b", "c", "d"]

print("First element:", my_list[0])
print("Second element:", my_list[1])
print("Last element:", my_list[-1])


"""
=======================================================
3. SLICING
=======================================================
Slicing allows you to get a part of a list.

Syntax:
list[start:end] → returns elements from start to end-1

Examples:
my_list[:2]  → first two elements
my_list[1:3] → elements at index 1 and 2
my_list[2:]  → from index 2 to the end
my_list[:]   → full copy of list

WITH STEP
list[start : end : step]

start → where to begin (included)
end   → where to stop (excluded)
step  → interval (default = 1)

Examples:
my_list[::2]  → every second element
my_list[1::2] → every second element starting from index 1
my_list[::-1] → full list reversed
"""

print("\n=== Slicing ===")

print(my_list[:2])     # ['a', 'b']
print(my_list[1:3])    # ['b', 'c']
print(my_list[2:])     # ['c', 'd']
print(my_list[:])      # full copy


"""
=======================================================
4. MODIFYING LISTS
=======================================================
Since lists are mutable, we can change elements.

my_list[index] = new_value
"""

print("\n=== Modifying Elements ===")

my_list[1] = "NEW"
print(my_list)


"""
=======================================================
5. BASIC LIST METHODS
=======================================================
append(x)    → adds x at the end
insert(i, x) → inserts x at index i
remove(x)   → removes the first occurrence of x
pop(i)      → removes element at index i (default: last)
count(x)    → counts how many times x appears
index(x)    → returns index of first x
sort()      → sorts the list
reverse()   → reverses the list
extend() -> added one list to another list
copy() -> copy list
sorted() -> sort without change object
"""

print("\n=== Basic List Methods ===")

fruits = ["apple", "banana", "orange", "banana"]

fruits.append("kiwi")
print("append:", fruits)

fruits.insert(1, "mango")
print("insert:", fruits)

fruits.remove("banana")  # removes first 'banana'
print("remove:", fruits)

popped_item = fruits.pop()  # removes last item
print("pop:", popped_item)
print("after pop:", fruits)

print("count 'banana':", fruits.count("banana"))
print("index of 'orange':", fruits.index("orange"))

numbers = [5, 1, 7, 3]
numbers.sort()
print("sorted:", numbers)

numbers.reverse()
print("reversed:", numbers)


"""
=======================================================
6. PRACTICE TASKS (NO LOOPS)
=======================================================
"""

print("\n=== Practice Tasks ===")

print("\nTask 1: Create a list")
"""
Create a list with 5 numbers.
Print the first and last element.
"""

# TODO: Write your solution here


print("\nTask 2: Replace an element")
"""
Create a list of 4 fruits.
Replace the second element with a different fruit.
"""

# TODO: Write your solution here


print("\nTask 3: Add and remove elements")
"""
Create an empty list.
Add 3 elements using append().
Remove one element using remove().
Print the final list.
"""

# TODO: Write your solution here


print("\nTask 4: Slicing practice")
"""
Create a list of 6 items.
Print:
— first 3 items
— last 2 items
— items from index 2 to index 4
"""

# TODO: Write your solution here


print("\nTask 5: Using methods")
"""
Create a list with repeated values.
Print how many times a value appears using count().
Remove one of them.
Find the index of another value.
"""

# TODO: Write your solution here


"""
=======================================================
7. EXTRA OPTIONAL TASKS
=======================================================
(For students who want more practice)

— Swap two elements in a list manually
— Create a copy of a list using slicing
— Remove the last element using pop()
"""


