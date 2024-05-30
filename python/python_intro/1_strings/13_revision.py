import string

# THIS IS A STRING REVISION 
# 1 INITIALISING STRING 
string = 'This is a string.'
print("Initialised string: \n", string)

# 2 TAKING STRING AS A INPUT FROM THE USER
string = input("Enter the string: ")
print("Entered string: \n", string)

# 3 STRING INDEXING
# STRING EMPTY INDEXING
index = string[:]
print("Whole string: \n", index)

index = string[2:15]
print("Only selected characters: \n", index)

# 4 REVERSED STRING
index = string[::-1]
print("Reversed string: ", index)
# with reversed function and join funtion
index = ''.join(reversed(string))
print("Using reversed string: ", index)

for i in range(len(string)):
    print(string[i], end='')
    
