#*** Object Oriented Programming MIDTERM Assignment***
#Name: Vyrareth Kuch
#Professor: Michael Chu
#Rutgers University - Camden
#Date: October 10th 2024
import random
class Students:
    def __init__(self, id = 0, firstname="", lastname = "", creditsEarned = 0, courseLoadCredits = 0,
                 status: object = 1) -> object:
        self.id = id or random.randint(1,999)
        self.firstname = firstname
        self.lastname = lastname
        self.creditsEarned = creditsEarned
        self.courseLoadCredits = courseLoadCredits
        self.status = status # Default status is freshmen
        self.update_status()  # adjust status based on credits earned
    def update_status(self):
        if self.creditsEarned < 30:
            self.status = 1
            print("Freshmen")
        elif  30 < self.creditsEarned < 60:
            self.status = 2
            print("Sophomore")
        elif  60 < self.creditsEarned < 90:
            self.status = 3
            print("Junior")
        elif  90 < self.creditsEarned < 120:
            self.status = 4
            print("Senior")
    def registerCourse(self,credits):

        if credits <= 0 or credits > 4:
            print("Error: Course credit must be between 1 and 4.")
        elif self.courseLoadCredits + credits > 18:
            print("Error: Cannot register more than 18 credits.")
        else:
            self.courseLoadCredits += credits
            print(f"Successfully registered {credits} credits.")
    def withdraw(self,credits):

        if credits <= 0 or credits > 4:
            print("Error: Course credit must be between 1 and 4.")
        if credits > self.courseLoadCredits:
            print("Error: Cannot withdraw more credits than current course load.")
        else:
            self.courseLoadCredits -= credits
            print(f"Successfully withdrew {credits} credits.")
    def passedCourses(self,credits):

        if credits <= 0 or credits > 4:
            print("Error: Course credit must be between 1 and 4.")
        elif credits > self.courseLoadCredits:
            print("Error: Cannot pass more credits than current course load.")
        else:
            self.courseLoadCredits -= credits
            self.creditsEarned += credits
            self.update_status()
            print(f"Successfully passed {credits} credits and earned them.")

    def createEmail(self):
        return self.lastname.lower()+str(self.id)+"@rutgers.edu"

    def __str__(self):
        return  (f"Welcome{self.firstname +" "+ self.lastname} you're currently a{self.status}\n"
                 f"Current Credits: {self.creditsEarned}\n")
