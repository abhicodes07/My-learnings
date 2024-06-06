

rows = int(input("Enter the number: "))

for i in range(rows):
    print()
    for j in range(rows-i):
        print(' ', end='')
    for k in range(2*i-1):
        print("*",end=' ')



