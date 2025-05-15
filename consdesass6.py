class Logger:
    def __init__(self):    #Constructor
        print("Logger object created")
        
    def __del__(self):     #destructor
        print("Logger object destroyed")
        
log = Logger()     
del log            