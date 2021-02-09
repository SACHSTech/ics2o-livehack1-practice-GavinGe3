"""
-------------------------------------------------------------------------------
Name:   windchill.py
Purpose:  calculates the windchill factor with given temperature in celsius and windspeeed in km/h
 
Author: Ge.G
 
Created:  08/02.2021
------------------------------------------------------------------------------
"""
print("******Windchill factor converter******")

#get windspeed and temperature in celsius
temperatureInCelsius = float(input("Enter the temperature in Celsius: "))
windSpeed = float(input("Enter the velocity of wind in Km/H: "))

#calculate windchill factor
windChillFactor = 13.12 + (0.6215 * temperatureInCelsius) - (11.37 * windSpeed ** 0.16) + (0.3965 * temperatureInCelsius * windSpeed ** 0.16)

#output the windchill factor
print(f"\n When temperature (in celsius) is {temperatureInCelsius} and windspeed is {windSpeed} km/h, the windchill is {round(windChillFactor, 2)} degrees celsius")