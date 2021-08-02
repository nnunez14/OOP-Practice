class Student:
    def __init__(self, major, year, hometown, balance_owed):
        self.major = major
        self.year = year
        self.hometown = hometown
        self.balance_owed = balance_owed
	
    def change_major(self, new_major):
	    self.major = new_major
	
    def pay_balance(self, amount):
	    self.balance_owed = self.balance_owed - amount
	
    def change_year(self):
        print("This student is currently a " + self.year)
        if self.year == "Freshman":
            self.year = "Sophomore"
        elif self.year == "Sophomore":
            self.year = "Junior"
        elif self.year == "Junior":
            self.year = "Senior"
        else:
            self.year = "Graduate"
        print("Next year, the student will be a " + self.year + "\n")
        
	
    def can_graduate(self):
        if self.year == "Senior" and self.balance_owed == 0:
            print("This student is eligible to graduate.\n")
            return True
        print("This student is not eligible to graduate.\n")
        return False

    def print_details(self):
        print("Student is a " + self.year + " majoring in " + self.major + " from " + self.hometown + ".")
        print("Student's balance is currently " + str(self.balance_owed) + "\n")


def run():
    student_1 = Student("Computer Science", "Senior", "Las Cruces", 0)
    student_1.print_details()
    student_1.can_graduate()
    student_2 = Student("Sports Communication", "Senior", "El Paso", 10000)
    student_2.print_details()
    student_2.can_graduate()
    student_3 = Student('Underwater basket weaving', 'Sophomore', 'Tulsa', 25000)
    student_3.print_details()
    student_3.change_year()
    student_3.print_details()


run()

