import calendar
import datetime
import pandas as pd


# print(calendar.calendar(2021, 2, 2, 6, 3))
c = calendar.TextCalendar()
c.prmonth(2021, 1)

my_date = datetime.datetime(2021, 1, 1)
print(pd.to_datetime(my_date).day_name())
