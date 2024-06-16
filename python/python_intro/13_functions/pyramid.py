# This is a program about pyramid program

def __pyramid__(rows: int) -> int:
   
    for i in range(rows):
        # Printing number of rows 
        print()
        for j in range(rows-i-1):
        # Printing white spaces
            print(" ", end="")
        for k in range(2*i+1):
        # Printing * on each iteration
            print("*", end='')
    print()
lines = int(input("Enter the number of lines you want to print: "))
__pyramid__(lines)

