# Program to store and display date, month, and time using tuple

# Taking user input
date = input("Enter the date : ")
month = input("Enter the month : ")
year = input("Enter the year : ")
time = input("Enter the time : ")

# Storing all values in a tuple (immutable data)
calendar_entry = (date, month, year, time)

# Displaying the stored information
print("\n Calendar Entry:")
print("-------------------------")
print("Date:", calendar_entry[0])
print("Month:", calendar_entry[1])
print("Year:", calendar_entry[2])
print("Time:", calendar_entry[3])
print("-------------------------")
print(f"Full Entry: {calendar_entry[0]} {calendar_entry[1]} {calendar_entry[2]}, at {calendar_entry[3]}")
