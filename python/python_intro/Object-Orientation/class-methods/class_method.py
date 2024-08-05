class MyClass:
    class_variable = 0
    def __init__(self, instance_variable):
        self.instance_variable = instance_variable
    
    @classmethod
    def class_method(cls):
        """a class method is a method that s bound to the class and 
        not to an instance of the class"""
        cls.class_variable += 1
        print(f"Value of class variable: {cls.class_variable}")
        print()
        print()
        print(MyClass.class_method.__doc__)       

obj1 = MyClass(5)
obj2 = MyClass(10)

MyClass.class_method() #Output: 1, accessing class variable using class name 
obj1.class_method() #Output: 2, using object
obj2.class_method() #Output: 3, using object




