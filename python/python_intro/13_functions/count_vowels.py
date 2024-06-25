def count(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u']
    flag = 0
    for i in range(len(sentence)):
        for j in range((len(vowels))):
            if sentence[i] == vowels[j]:
                flag += 1
                # return True
            # else: 
                # return False
    print(flag)
sentence = input("Enter the string: ")
# filtered = filter(count, sentence)
#
# print("Filtered letters: ")
# for s in filtered:
#     print(s)
#

count(sentence)

