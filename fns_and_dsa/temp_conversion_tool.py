FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

try:
    temp = float(input("Enter the temperature to convert: "))
except ValueError:
    print("Invalid temperature. Please enter a numeric value.")
    exit()   # stop the program if it's not numeric

unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

if unit == 'f':
    result = convert_to_celsius(temp)
    print(f"{temp}°F is {result}°C")
elif unit == 'c':
    result = convert_to_fahrenheit(temp)
    print(f"{temp}°C is {result}°F")
else:
    # you can add a separate message for invalid unit if desired
    print("Invalid unit. Please enter 'C' or 'F'.")
