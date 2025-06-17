"""Create a class called `Temperature` with a static method `celsius_to_fahrenheit` that converts Celsius to Fahrenheit,
and a class method `from_fahrenheit` that creates a Temperature object from a Fahrenheit value.# Demonstrate both methods."""

class Temperature:
    def __init__(self):
        pass
    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        celsius = (fahrenheit- 32)/1.8
        return round(celsius,3)   
    @staticmethod    
    def celsius_to_fahrenheit(celsius):
        fahrenheit = (celsius * 1.8) + 32
        return round(fahrenheit,3)   
     
# instantiate the class and call the methods    
temp_cel = Temperature.fahrenheit_to_celsius(100) 
print(temp_cel)  
temp_fah = Temperature.celsius_to_fahrenheit(37.778)
print(temp_fah)