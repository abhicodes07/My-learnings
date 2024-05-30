import string
string = input("Enter the string: ")
print("Initialised string: ", string)

string1 = ''.join(reversed(string.upper()))

for i in range(0, len(string1)):
    if string1[i] == ' ':
        print("\n")
    print(string1[i], end='')
