from Appt import Appt
class Month(Appt):
    def __init__(self,month = 0,day = 0,year = 0,description ="" ):
        super().__init__(month,day,year,description)
    def OccursOn(self,month,day,year):
        if month.lstrip('-').isdigit() == False:
            return False
        else:
            month = int(month)
        if month < 1 or month > 12:
            print("Invalid month")
        if month==self.month:
            return True
        else:
            return False