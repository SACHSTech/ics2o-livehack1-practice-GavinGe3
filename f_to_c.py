"""
-------------------------------------------------------------------------------
Name:   f_to_c.py
Purpose:  converts given temperature in fahrenheit into temperature in celsius
 
Author: Ge.G
 
Created:  08/02.2021
------------------------------------------------------------------------------
"""

#get degrees in fahrenheit
degreesInFahrenheit = float(input("Enter the temperature in fahrenheit: "))

#calculate degrees in Celsius
degreesInCelsius = (degreesInFahrenheit - 32) * (5 / 9)

#output degrees in Celsius
print(f"\nDegrees in celsius: {degreesInCelsius}")

