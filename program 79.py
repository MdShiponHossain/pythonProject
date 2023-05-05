class student:
    roll: ""
    gpa: ""

    def display(self):
        print(f"Roll : {self.roll}, GPA : {self.gpa}")



shipon = student()
shipon.roll = 206
shipon.gpa = 3.90
shipon.display()

mariya = student()
mariya.roll = 264
mariya.gpa = 3.50
mariya.display()