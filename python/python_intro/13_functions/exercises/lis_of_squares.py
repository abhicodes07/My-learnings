# a program to demonstrate printing list of squares 


def squares(leng):
    list = []
    for i in range(1, leng):
        sqr = i*i
        list.append(sqr)
    print(list)

squares(10)
        
