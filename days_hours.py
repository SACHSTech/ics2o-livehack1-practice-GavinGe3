"""
-------------------------------------------------------------------------------
Name:   days_hours.py
Purpose:  converts given number of hours into the number of days and hours
 
Author: Ge.G
 
Created:  08/02.2021
------------------------------------------------------------------------------
"""
print("******Hours to days and hours converter******")

#get number of hours
numberOfHours = float(input("Enter the number of hours: "))

#convert number of hours into the amount of days and hours
numberOfDays = numberOfHours // 24
numberOfRemainingHours = numberOfHours % 24

#output number of days and and remaining hours
print(f"\n{numberOfHours} hours = {numberOfDays} days and {numberOfRemainingHours} hours")