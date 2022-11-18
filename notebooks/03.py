import random

class Course(object):
    name: str
    classroom: str
    teacher: str
    etcs: int
    grade: None or int

    def __init__(self, name, classroom, teacher, etcs, grade):
        self.name = name
        self.classroom = classroom
        self.teacher = teacher
        self.etcs = etcs
        self.grade = grade

class DataSheet():
    courses: list[Course]

    def __init__(self, courses):
        self.courses = courses

    def get_grades_as_list(self):
        list = []
        for i in self.courses:
            list.append(i.grade)

        return self.courses

class Student():
    name: str
    gender: int
    data_sheet: DataSheet
    image_url = str

    def __init__(self, name, gender, data_sheet, image_url):
        self.name = name
        self.gender = gender
        self.data_sheet = data_sheet
        self.image_url = image_url

    def get_avg_grade(self):
        sum_num = 0
        grade_list = self.data_sheet.get_grades_as_list()
        for g in grade_list: sum_num = sum_num + g.grade

        avg = sum_num / len(grade_list)
        return avg


def gen_students(n):
    names = ["Brian", "Peter", "Jens", "Børge", "Helga", "Jesper", "navn1", "navn2", "navn3", "navn4", "navn5", "navn6", "navn7", "navn8", "navn9", "navn10"]
    students = []
    courses = [Course("Subject 1", "Room 1", "Teacher 1", 10, 4), Course("Subject 2", "Room 2", "Teacher 2", 80, 10), Course("Subject 3", "Room 3", "Teacher 3", 50, 0)]

    for i in range(n):
        coursesGenerated = []
        for course in courses:
            if random.randint(0, 1) < 0.5:
                coursesGenerated.append(course)

        name = names[random.randint(0, n)]
        if random.randint(0, 1) > 0.5:
            gender = "Boy"
        else:
            gender = "Girl"

        dataSheet = DataSheet(coursesGenerated)
        students.append(Student(name, gender, dataSheet, f"https://imageLink.com/{random.randrange(1, 100)}"))

    with open("./data/generatedStudents.csv", "w") as generatedStudents:
        data = "Name;Gender;Courses;imageUrl \n"
        for i in students:
            tmpStr = ""
            if i.data_sheet.courses is None:
                continue
            for j in i.data_sheet.courses:
                tmpStr += f"{j} "
            data += f"{i.name};{i.gender};{tmpStr};{i.image_url} \n"

        generatedStudents.write(data)
    return students

def read_students_into_list(file: str):
    with open(file, "r") as students:
        for line in students:
            name, gender, data_sheet, image_url = line.split(";")
            read_student = Student(name, gender, data_sheet, image_url)
            print(f"{read_student.name} {read_student.gender} {read_student.data_sheet} {read_student.image_url}")


if __name__ == "__main__":

    courseList1 = [Course("Subject 1", "Room 1", "Teacher 1", 10, 4), Course("Subject 2", "Room 2", "Teacher 2", 80, 10), Course("Subject 3", "Room 3", "Teacher 3", 50, 0)]
    courseList2 = [Course("Subject 1", "Room 1", "Teacher 1", 10, 4), Course("Subject 3", "Room 3", "Teacher 3", 50, 0)]
    dataSheet1 = DataSheet(courseList1)
    dataSheet2 = DataSheet(courseList2)

    students = [Student("Student 1", "Boy", dataSheet1, "student1img"), Student("Student 2", "Girl", dataSheet2, "image")]

    gen_students(10)
    for student in students:
        print(f"{student.name} {student.gender} {student.data_sheet.get_grades_as_list()}")
        print(f"{student.name} grade avg: {student.get_avg_grade()}")

    read_students_into_list("./data/generatedStudents.csv")