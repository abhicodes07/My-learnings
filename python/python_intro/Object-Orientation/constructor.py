class Person:

    # __init__ is a special function called constructor
    def __init__(self: None, name: str, occ: str) -> str:
        """
        -- This is a constructor, a unique function 
        is called automatically when an object is 
        created of class --
        """
        print("Hey this is a constructor")
        self.name = name
        self.occ = occ

    def info(self) -> str:
        print(f"Hello! I am {self.name} and my occupation is {self.occ}")

# Initialised two of the objects hence constructor will be called two times
obj1 = Person("Abhinav", "Software developer")
obj2 = Person("Muskan", "HR")

# accessing information from the constructor
obj1.info()
obj2.info()
