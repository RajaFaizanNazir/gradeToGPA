import re

table = {"A+": 4.0, "A": 4.0, "A-": 3.7, "B+": 3.3, "B": 3.0, "B-": 2.7, "C+": 2.3, "C": 2.0, "C-": 1.7, "D+": 1.3,
         "D": 1.0, "F": 0}
majorCourse = ["COMP", "MATH"]


class Course:
    def __init__(self, subject, credit, grade):
        self.subject = subject
        self.credit = credit
        self.grade = grade

    def grade2Point(self):
        return table.get(self.grade) * self.credit


class Student:
    def __init__(self, name):
        self._name = name
        self._courseRecords = []
        self._totalCredits = 0

    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name

    def addCourse(self, t):
        self._courseRecords.append(t)
        self._totalCredits = self._totalCredits + t.credit

    def getCredits(self):
        return self._totalCredits

    def gpa(self):
        total = 0.0
        for i in self._courseRecords:
            total = total + i.grade2Point()
        return total


class CsStudent(Student):
    def __init__(self, name):
        self._mathCredits = 0
        self._csCredits = 0
        Student.__init__(self, name)

    def addCourse(self, t):
        sub = re.split(r'(\d+)', t.subject)[0]
        if sub == "COMP":
            self._csCredits = self._csCredits + t.credit
        elif sub == "MATH":
            self._mathCredits = self._mathCredits + t.credit
        Student.addCourse(self, t)

    def getCsCredits(self):
        return self._csCredits

    def getMathCredits(self):
        return self._mathCredits

    def majorGpa(self):
        total = 0.0
        for i in self._courseRecords:
            if re.split(r'(\d+)', i.subject)[0] in majorCourse:
                total = total + i.grade2Point()
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


main()
