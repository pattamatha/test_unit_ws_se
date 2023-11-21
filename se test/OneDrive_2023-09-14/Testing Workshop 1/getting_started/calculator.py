from another_class import AnotherClass

class Calculator:

    def add(self, a, b):
        pass

    def multiply(self, a, b):
        pass

    def divide(self, a, b):
        pass

    def use_capsys_fixture(self):
        print("hello world!")

    def use_external(self, value):
        class_obj = AnotherClass()
        return class_obj.some_method(value)

    def use_object(self,value,some_obj):
        return some_obj.fetch(value)