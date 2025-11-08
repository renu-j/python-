fruits=["apple,banana"]
fruits.append("mango")#add one element at the end
print(fruits)

#insert() add elememt a specific position
fruits.insert(1,"orange")
print(fruits)

#3.extend() → Add multiple elements (join lists)
fruits.extend(["grape", "banana","kiwi"])
print(fruits)

#4.remove() → Remove the first matching element
fruits.remove("banana")
print(fruits)

#4.pop() → Remove element by index (default: last)
fruits.pop()
print(fruits)
