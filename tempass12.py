class TemperatureConverter:
    
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c*9/5)+ 32
    
temp = TemperatureConverter() 
print(temp.celsius_to_fahrenheit(20))
 
   