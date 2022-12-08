table = {"A+": 4.0, "A": 4.0, "A-": 3.7, "B+": 3.3, "B": 3.0, "B-": 2.7, "C+": 2.3, "C": 2.0, "C-": 1.7, "D+": 1.3,
         "D": 1.0, "F": 0}


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

    def getCredits(self):
        pass

    def gpa(self):
        pass


class CsStudent(Student):
    def __init__(self, name):
        self._mathCredits = 0
        self._csCredits = 0
        Student.__init__(name)

    def addCourse(self, t):
        Student.addCourse(t)

    def getCsCredits(self):
        return self._csCredits

    def getMathCredits(self):
        return self._mathCredits

    def majorGpa(self):
        pass


def main():
    pass
