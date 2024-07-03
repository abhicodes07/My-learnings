def info(func):
    def fxexc(*args):
        print("Hello this is pyramid!")
        func(*args)
        print("Function executed!")
    return fxexc

@info
def pyramid(*args):
    for i in range(*args):
        for j in range(i):
            print('*', end=" ")
        print()

row = int(input("Enter the rows: "))
pyramid(row)

