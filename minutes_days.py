"""
-------------------------------------------------------------------------------
Name:   minutes_days.py
Purpose:  Converts given minutes into days, hours and minutes
 
Author: Ge.G
 
Created:  08/02.2021
------------------------------------------------------------------------------
"""
print("******Minutes to days, hours, and minutes converter******")
#get number of minutes
numberOfMinutes = float(input("Enter the number of minutes: "))

#convert into number of Days, Hours, and remaining minutes
numberOfDays = numberOfMinutes // 1440
numberOfHours = (numberOfMinutes - numberOfDays * 1440) // 60
numberOfRemainingMinutes = numberOfMinutes % 60 

#output number of Days, Hours, and remaining minutes
print(f"\n{numberOfMinutes} minutes = {numberOfDays} days {numberOfHours} Hours and {numberOfRemainingMinutes} minutes")