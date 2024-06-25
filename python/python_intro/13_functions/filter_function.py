# Fliter function in py

def vowels(variable):
    vowel = ['a', 'e', 'i', 'o', 'u']
    if variable in vowel:
        return True
    else:
        return False

sent = input("Enter the string: ")
list1 = []
for i in range(len(sent)):
    list1.append(sent[i])
    if sent[i] == ' ':
        list1.remove(sent[i])

# print(list1)

filtered = filter(vowels, list1)

print("Filtered letters: ")
for s in filtered:
    print(s)


