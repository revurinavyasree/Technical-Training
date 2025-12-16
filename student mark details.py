class Student:
    def __init__(self, name,roll_no,dept,mark1,mark2,mark3):
        self.name = name 
        self.roll_no = roll_no
        self.dept = dept
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3
    def total_marks(self):
        return self.mark1 + self.mark2 + self.mark3
    def average_marks(self):
        return self.total_marks() / 3
    def grade(self):
        total_marks = self.total_marks()
        if total_marks >=450:
            print("grade A")
        elif total_marks >=350:
            print("grade B")
        elif total_marks >=250:
            print("grade C")
        else:
            print("grade D")
    def display(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Department: {self.dept}")
        print(f"Marks: {self.mark1}, {self.mark2}, {self.mark3}")
        print(f"Total Marks: {self.total_marks()}")
        print(f"Average Marks: {self.average_marks():.2f}")
        self.grade()
student1 = Student("Alice", 101, "Computer Science", 85, 90, 88)
student1.display()
student2 = Student("Bob", 102, "Mechanical Engineering", 75, 80, 70)
student2.display()
student3 = Student("Charlie", 103, "Electrical Engineering", 65, 60, 70)
student3.display()
