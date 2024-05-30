vsplit import string
# To print the details about the imported STRING module use below command

# --------- print(help(string)) ---------

# FOLLOWING ARE THE MOST USED AND COMMON STRING METHODS IN PYTHON
text = input('Enter the string: ')
print(f"Initialised string: {text}\n")

# 1
# string.ascii_uppercase and string.ascii_lowercase
print("Printing lowercase ASCII characters: ")
print(string.ascii_lowercase)

print("\n")
print("Printing uppercase ASCII characters: ")
print(string.ascii_uppercase)
print("\n")

# 2
# string.endswith() and string.startswith()

print("The string endswith abhinav: ",text.endswith('abhinav'))
print("The string starts with muskan: ", text.startswith('muskan'))


# 3
# string.upper
print("String in uppercase: ", text.upper())

# 4
# string.swapcase
text2 = input("Enter another string: ")
print("Swapping the case of intialised string using swapcase: ", text2.swapcase())

# 5
# string.strip()
text3 = input("Enter the string with trailing spaces: ")
strip_func = text3.strip()
print(strip_func)
