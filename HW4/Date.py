from Appt import Appt
class Date(Appt):
    def __init__(self,month = 0,day = 0,year = 0,description = ""):
        super().__init__(month,day,year,description)
    def OccursOn(self,month,day,year):
        return super().OccursOn(month,day,year)
