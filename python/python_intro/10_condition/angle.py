rows = int(input("Enter the rows: "))

for i in range(rows):
    print()
    for j in range(i + 1):
        print("*", end=' ')
print()


for i in range(rows):
    print()
    for j in range(rows-i):
        print(" ", end=' ')
    for k in range(2*i+1):
        print("*", end=' ')

print()



