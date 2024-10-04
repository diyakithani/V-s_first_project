from Appt import Appt

class Day(Appt):
    def __init__(self,month = 0,day = 0,year = 0,description = ""):
        super().__init__(month,day,year,description)
    def OccursOn(self,month,day,year):
        if day.lstrip('-').isdigit() == False:
            return False
        else:
            day = int(day)
        if day <= 0 or day > 31:
            print("Invalid days")
        if day ==self.day:
            return True
        else:
            return False

