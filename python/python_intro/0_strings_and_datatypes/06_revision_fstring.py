name = input("Enter the name: ")
std = int(input("Enter the class: "))
print("Enter the Dob in DD", "MM", "YY", sep="-")
date = int(input("Date: "))
month = input("Month: ")
year = int(input("Year: "))
info = f"Student Name: {name}\nStudent Class: {std}\nStudent DOB: {date} {month} {year}"
print(info)
