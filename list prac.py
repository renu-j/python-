#  Mini Project: Student Record Manager (Using List)


students = []  # empty list to store student names

while True:
    print("\n Student Record Manager  0 '[ ]")
    print("1. Add Student")
    print("2. View Students")
    print("3. Remove Student")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        name = input("Enter student name: ")
        students.append(name)
        print(f"{name} has been added successfully!")

    elif choice == '2':
        print("\nList of Students:")
        for s in students:
            print("-", s)

    elif choice == '3':
        name = input("Enter student name to remove: ")
        if name in students:
            students.remove(name)
            print(f"{name} has been removed.")
        else:
            print("Student not found!")

    elif choice == '4':
        print("Exiting the program...")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 4.")
