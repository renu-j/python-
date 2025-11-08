
#  Demonstration of List Methods in Python

# Creating a list
fruits = ["apple", "banana", "cherry"]
print("Original list:", fruits)

# 1️. append() – Add an element at the end
fruits.append("mango")
print("\nAfter append('mango'):", fruits)

# 2️. insert() – Insert at a specific position
fruits.insert(1, "orange")
print("After insert(1, 'orange'):", fruits)

# 3️. extend() – Add multiple elements (join lists)
fruits.extend(["grape", "kiwi"])
print("After extend(['grape', 'kiwi']):", fruits)

# 4️. remove() – Remove the first matching element
fruits.remove("banana")
print("After remove('banana'):", fruits)

# 5️. pop() – Remove element by index (default = last)
fruits.pop()
print("After pop():", fruits)

# 6️. index() – Return index of first matching element
index_pos = fruits.index("orange")
print("Index of 'orange':", index_pos)

# 7️. count() – Count how many times a value appears
fruits.append("apple")
print("After adding another 'apple':", fruits)
print("Count of 'apple':", fruits.count("apple"))

# 8️. sort() – Sort list in ascending order
fruits.sort()
print("After sort():", fruits)

# 9️. reverse() – Reverse the order of the list
fruits.reverse()
print("After reverse():", fruits)

# 10. copy() – Copy the list
copied_list = fruits.copy()
print("Copied list:", copied_list)

# 1️1. clear() – Remove all elements
fruits.clear()
print("After clear():", fruits)
