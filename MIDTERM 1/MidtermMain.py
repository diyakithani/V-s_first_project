#*** Object Oriented Programming MIDTERM Assignment***
#Name: Vyrareth Kuch
#Professor: Michael Chu
#Rutgers University - Camden
#Date: October 10th 2024
from Students import Students
from Graduate_Student import Graduate_Student
def main():
    # user inputs their first name, last name, and ID
    student_type = input("Are you an undergraduate (U) or a graduate student (G)? ").strip().upper()

    firstname = input("Enter your first name: ")
    lastname = input("Enter your last name: ")

    id_input = input("Enter your preferred ID number (leave blank to generate one): ")

    if id_input.isdigit():  # Check if a valid integer ID is entered
        id_number = int(id_input)
    else:
        id_number = 0  # Default to 0, which will trigger random generation in the Students class

    # Create the student object
    if student_type == 'G':
        student= Graduate_Student(id=id_number, firstname=firstname, lastname=lastname)
    else:
        student = Students(id=id_number, firstname=firstname, lastname=lastname)
    student = Students(id=id_number, firstname=firstname, lastname=lastname)

    # Interactive menu
    while True:
        print("\nSelect an action:")
        print("1. Register Course")
        print("2. Withdraw Course")
        print("3. Create Email")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            credits = input("How many credits is your course?(1-4): ")
            if credits.isdigit():  # checking if the input is a digit
                student.registerCourse(int(credits))
            else:
                print("Error: Please enter a valid integer.")

        elif choice == '2':
            credits = input("Enter the amount of credits of the course you want to withdraw from (1-4): ")
            if credits.isdigit():  # Checking if the input is a digit
                student.withdraw(int(credits))
            else:
                print("Error: Please enter a valid integer.")

        elif choice == '3':
            print(f"Email: {student.createEmail()}")

        elif choice == '4':
            print("Exiting the program.")
            break

        else:
            print("Error: Invalid choice. Please select a valid action.")

if __name__ == "__main__":
    main()
