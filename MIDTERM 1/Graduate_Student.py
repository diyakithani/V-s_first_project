#*** Object Oriented Programming MIDTERM Assignment***
#Name: Vyrareth Kuch
#Professor: Michael Chu
#Rutgers University - Camden
#Date: October 10th 2024

from Students import Students
class Graduate_Student(Students):
    def __init__(self, id = None  ,firstname = "" , lastname = "" ,creditsEarned = 0 ,courseLoadCredits = 0):
        super().__init__(id,firstname , lastname,creditsEarned,courseLoadCredits)
        self.status = 5

    def registerCourse(self, credits):
        if credits <= 0 or credits > 4:
            print("Error: Course credit must be between 1 and 4.")
        elif self.courseLoadCredits + credits > 15:
            print("Error: Cannot register more than 15 credits.")
        else:
            self.courseLoadCredits += credits
            print(f'Successfully registered {credits} credits.')