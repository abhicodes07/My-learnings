# open and read file using with statement
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
# no need to close the file

