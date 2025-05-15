class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.bread = breed
    
    def bark(self):
        print(f"{self.name} is says wolf")
        
d = Dog("Rex", "German Shephered")        

d.bark()