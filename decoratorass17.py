def add_greeting(self):
    self.greet = lambda self: "Hello from Decorator!"
    return self

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Farhat")
print(p.greet())