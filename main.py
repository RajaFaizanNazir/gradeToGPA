import re

table = {"A+": 4.0, "A": 4.0, "A-": 3.7, "B+": 3.3, "B": 3.0, "B-": 2.7, "C+": 2.3, "C": 2.0, "C-": 1.7, "D+": 1.3,
         "D": 1.0, "F": 0}  # a dictionary table to define which grade has what grade points
majorCourse = ["COMP", "MATH"]  # major course list


class Course:  # course class
    def __init__(self, subject, credit, grade):  # constructor of course class
        self.subject = subject
        self.credit = credit
        self.grade = grade

    def grade2Point(self):  # it converts course grade to grade points
        return table.get(self.grade) * self.credit  # it gets the grade from the table and multiply it with the credit


class Student:
    def __init__(self, name):
        self._name = name
        self._courseRecords = []  # empty course records list in the start
        self._totalCredits = 0  # 0 total credits in the start

    # getter and setter of nam
    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name

    # it adds course to the list
    def addCourse(self, t):
        self._courseRecords.append(t)  # appending to the course record list
        self._totalCredits = self._totalCredits + t.credit  # and it adds total credits of the student

    def getCredits(self):
        return self._totalCredits

    # it adds grade points and return
    def gpa(self):
        total = 0.0
        for i in self._courseRecords:  # iterating through the course record list
            total = total + i.grade2Point()  # converting grade to grade points and adding it
        return total


class CsStudent(Student):  # cs student is a student / inheritance
    def __init__(self, name):  # constructor of student class
        self._mathCredits = 0
        self._csCredits = 0
        Student.__init__(self, name)  # calling base class constructor

    def addCourse(self, t):
        sub = re.split(r'(\d+)', t.subject)[0]  # it splits the characters, like MATH150 will become MATH
        if sub == "COMP":  # check if it is COMP
            self._csCredits = self._csCredits + t.credit  # add it to the cs credits
        elif sub == "MATH":  # check if it is MATH
            self._mathCredits = self._mathCredits + t.credit  # add it to the math credits
        Student.addCourse(self, t)  # and calling te base class add course function

    def getCsCredits(self):
        return self._csCredits

    def getMathCredits(self):
        return self._mathCredits

    def majorGpa(self):  # major gpa
        total = 0.0
        for i in self._courseRecords:  # iterating to course record list
            if re.split(r'(\d+)', i.subject)[0] in majorCourse:  # if course is in the major course list written above
                total = total + i.grade2Point()  # then add the grade points to total that will be return
        return total


def main():
    bob = CsStudent("bob")
    bob.addCourse(Course("MATH150", 5, "A"))
    bob.addCourse(Course("COMP164", 4, "B"))
    bob.addCourse(Course("COMP165", 4, "C+"))
    bob.addCourse(Course("ENG151", 4, "D+"))
    print("Bob's Total credits:", bob.getCredits())
    print("Bob's Total math credits:", bob.getMathCredits())
    print("Bob's Total comp credits:", bob.getCsCredits())
    print("Bob's gpa:", bob.gpa())
    print("Bob's majorGpa:", bob.majorGpa())


# calling main function
main()
