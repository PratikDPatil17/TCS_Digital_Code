class Student():
    def __init__(self, name, roll, age, gender):
        self.name = name
        self.roll = roll
        self.age = age
        self.gender = gender

class college():
    def __init__(self, name, std_lst):
        self.name = name
        self.std_lst = std_lst

    def addStudent(self, name, roll, year, gender):
        self.std_lst.append(Student(name,roll,age,gender))

    def getStudentCount(self):
        return len(self.std_lst)

    def findStudent(self, roll):
        for i in self.std_lst:
            if i.roll == roll:
                return i.name
        return -1
    def countYearwiseStudents(self, year):
        count = 0
        for i in self.std_lst:
            if i.year == year:
                count+=1
        return count



students=[]
c = College('XYZ',students)
n=int(input())
for i in range(n):
    name=input()
    roll=int(input())
    year=int(input())
    gender=input()
    c.addStudent(name,id,year,gender)

roll=int(input())
year=int(input())
print(c.getStudentCount())
print(c.findStudent(roll))
print(c.countYearwiseStudents(year))
