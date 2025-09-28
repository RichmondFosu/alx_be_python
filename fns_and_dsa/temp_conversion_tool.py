FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


temp = float(input('Enter the temperature to convert: '))
unit = input('Is this temperature in Celsius or Fahrenheit? (C/F): ').lower()

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    fahrenheit =  (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit



if unit == 'f':
  result = convert_to_celsius(temp)
  print(f'{temp}°F is {result}°C')
elif unit =='c':
    result = convert_to_fahrenheit(temp)
    print(f'{temp}°C is {result}°F')
else:
    print('Invalid temperature.Please enter a numeric value.')