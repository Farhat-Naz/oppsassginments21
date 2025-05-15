class Engine:
    def start(self):
        print("Engine started")
        
class Car:
    def __init__(self, Engine):
        self.Engine = Engine
        
    def start_car(self):
        self.Engine.start()
        
        
e1 = Engine()
c1 = Car(e1)
c1.start_car()                    