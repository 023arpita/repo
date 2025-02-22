import datetime
date_object = datetime.date(2030, 2, 27 )
day_name = date_object.strftime("%A")
print(f"The day name for {date_object} is: {day_name}")
