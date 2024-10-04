from Appt import Appt
from Date import Date
from Day import Day
from Month import Month
#month, day, year, desc
appt1 = Appt(12,15,2024,"Root")
appt2 = Date(11,15,2024,"Pull teeth")
appt3 = Month(3,15,2024,"Clean")
appt4 = Day(4,15,2024,"Crown")
appts = [appt1,appt2,appt3,appt4]
d = input(" please enter the day that you want to check: ")
m = input(" please enter the month that you want to check: ")
y = input(" please enter the year that you want to check: ")
for x in appts:
    if(x.OccursOn(m,d,y)):
        print(x.desc)
