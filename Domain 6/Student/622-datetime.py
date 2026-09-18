import datetime
current_time = datetime.datetime.now()
print("The current date and time is:", current_time.strftime('%m-%d-%y %H:%M %p'))
print("the day of the week is:", current_time.weekday())
print("name of the weekday is:", current_time.strftime('%A'))