# this a practice program


with open('test.txt', 'a') as file:
    file.write("This is test")

with open('test.txt', 'r') as file1:
    content = file.read()
    print(content)



