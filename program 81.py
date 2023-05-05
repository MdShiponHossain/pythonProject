class student:
    roll: ""
    gpa: ""

    def __init__(self,roll,gpa):
        self.roll = roll
        self.gpa = gpa

    def display(self):
        print(f"Roll : {self.roll}, GPA : {self.gpa}")



shipon = student(206, 3.90)
shipon.display()

mariya = student(264, 3.50)
mariya.display()