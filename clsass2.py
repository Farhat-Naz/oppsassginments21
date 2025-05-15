class Counter:
    
    count = 0
    def __init__(cls):
        Counter.count += 1
     
    @classmethod
    def show_count(cls):
        print(f"Totla object created: { cls.count}") 
     
     
     
     
c1 = Counter()
c2 = Counter
Counter.show_count()
        