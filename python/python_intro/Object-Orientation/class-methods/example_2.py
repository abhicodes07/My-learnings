class Base:
    instance_var = 0
    def __init__(self):
        print(f"Initial Value of Instance Variable: {self.instance_var}")
    
    @classmethod
    def increase(cls):
        cls.instance_var += 10
        return cls.instance_var

b = Base()
print(b.increase())
