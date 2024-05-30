#Many people keep time using a 24-hour clock (11 is 11am and 23 is 11pm, 0 is midnight).
#If it is currently 13 and you set your alarm to go off in 50 hours, it will be 15 (3pm).
#Write a Python program to solve the general version of the above problem. Ask the user
#for the time now (in hours) and then ask for the number of hours to wait for the alarm.
#Your program should output what the time will be on a 24-hour clock when the alarm goes off.

#initialize variables
current_time_hhmm = 0
hours_to_wait = 0
alarm_time_hour = 0
alarm_time_minute = 0

#prompt for current time and check it is between 0 and 2400 and that the number of minutes is less than 60
current_time_hhmm = int(input('\nEnter the current time in HHMM format: '))
if current_time_hhmm < 0 or current_time_hhmm > 2359:
    print('You entered an invalid time: {:d}, the program will exit.'.format(current_time_hhmm))
    exit()
if current_time_hhmm % 100 > 59:
    print('You entered an invalid number of minutes: {:d}, the program will exit.\n'.format(current_time_hhmm % 100))
    exit()

#prompt for hours to wait and check if it is greater than 0
hours_to_wait = int(input('\nEnter the number of hours to wait: '))
if hours_to_wait <= 0:
    print('You entered an invalid time to wait: {:d}, the program will exit.'.format(hours_to_wait))
    
#do calculations
alarm_time_hour = (current_time_hhmm // 100 + hours_to_wait) % 24
alarm_time_minute = current_time_hhmm % 100
 
#print out alarm time
print('\nThe alarm will occur at: {:d}{:02d}\n'.format(alarm_time_hour,alarm_time_minute))