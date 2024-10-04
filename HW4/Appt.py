class Appt:
    def __init__(self,month = 0,day = 0,year = 0,description =""):
        self.month=month
        self.day=day
        self.year=year
        self.desc=description
    def OccursOn(self,month,day,year):
        if month.lstrip('-').isdigit() == False or day.lstrip('-').isdigit() == False or year.lstrip('-').isdigit() == False:
            return False
        else:
            month = int(month)
            day = int(day)
            year = int(year)
            # protecting my code if the user inputs a negative days or 0 days
        if day <= 0 or day > 31:
            print("Invalid Day")
        if month < 1 or month > 12:
            print("Invalid month")
        if year < 0:
            print("Invalid year")
        if month == self.month and day==self.day and year == self.year:
            return True
        else:
            return False




