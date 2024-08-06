class ParentClass:
    def parentMethod(self):
        print("This is the parent method.")

class ChildClass(ParentClass):
    def childMethod(self):
        print("This is the child method.")
        super().parentMethod()

child_obj = ChildClass()
child_obj.childMethod()

child_obj.parentMethod()
