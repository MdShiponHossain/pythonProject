class student:
    roll: ""
    gpa: ""

    def set_value(self,roll,gpa):
        self.roll = roll
        self.gpa = gpa

    def display(self):
        print(f"Roll : {self.roll}, GPA : {self.gpa}")



shipon = student()
shipon.set_value(206, 3.90)
shipon.display()

mariya = student()
mariya.set_value(264, 3.50)
mariya.display()