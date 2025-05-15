class Employee:
    def __init__(self, name, salary, ssn):
        self.name =  name  #public
        self._salary = salary #protected
        self.__ssn = ssn  #privated
        
emp = Employee("farhat", 50000, "0043030330")        
print(emp.name)
print(emp._salary)
#print(emp.__ssn)
print(emp._Employee__ssn)  