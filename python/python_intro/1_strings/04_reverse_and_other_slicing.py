string = "iamabhinavasthana"
print("String initialised: ", string)
print("\n")

print(string[::])
print("\n")

print(string[:5:])
print("\n")

print("-5th character of string: ", string[-3])
print(": characters of string: ", string[:])

print("Printing  characters with gap of two: ", string[::2])

print("Reversing the string: ",string[::-1])
print("\n")
print("Reversed string with a gap of two: ", string[::-2])


# USING REVERSED AND JOIN FUNCTION
string =''.join(reversed(string))
print(string)

string1 = 'acoolestdelusionalkid'.join(string)
print(string1)
