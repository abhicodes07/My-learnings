def dec1(func1):
    def execfunc():
        print("Executing now")
        func1()
        print("Executed!")
    return execfunc()

@dec1
def who_is_abhi():
    print("Abhi is badass")


