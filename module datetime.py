import datetime
date_object = datetime.date(2031, 3, 14 )
day_name = date_object.strftime("%A")
print(f"The day name for {date_object} is: {day_name}")