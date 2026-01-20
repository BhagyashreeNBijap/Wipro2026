import json
import csv
import time
from abc import ABC, abstractmethod

# DECORATORS 

def log_execution(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"[LOG] Method {func.__name__}() executed successfully")
        return result
    return wrapper


def admin_only(func):
    def wrapper(*args, **kwargs):
        is_admin = False
        if not is_admin:
            print("Access Denied: Admin privileges required")
            return
        return func(*args, **kwargs)
    return wrapper


def performance_timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution Time: {end - start:.4f} seconds")
        return result
    return wrapper


# DESCRIPTORS 

class MarksDescriptor:
    def __set__(self, instance, value):
        if any(m < 0 or m > 100 for m in value):
            raise ValueError("Marks should be between 0 and 100")
        instance.__dict__["marks"] = value

    def __get__(self, instance, owner):
        return instance.__dict__.get("marks", [])


class SalaryDescriptor:
    def __get__(self, instance, owner):
        print("Access Denied: Salary is confidential")
        return None

    def __set__(self, instance, value):
        instance.__dict__["_salary"] = value


# ABSTRACT CLASS 

class Person(ABC):
    def __init__(self, pid, name, department):
        self.id = pid
        self.name = name
        self.department = department

    @abstractmethod
    def get_details(self):
        pass

    def __del__(self):
        print(f"{self.name} object destroyed")


# STUDENT 

class Student(Person):
    marks = MarksDescriptor()

    def __init__(self, sid, name, department, semester, marks):
        super().__init__(sid, name, department)
        self.semester = semester
        self.marks = marks

    def get_details(self):
        print("Student Details:")
        print("--------------------------------")
        print("Name      :", self.name)
        print("Role      : Student")
        print("Department:", self.department)

    @log_execution
    @performance_timer
    def calculate_performance(self):
        avg = sum(m for m in self.marks) / len(self.marks)
        grade = "A" if avg >= 80 else "B" if avg >= 60 else "C"
        print("Student Performance Report")
        print("--------------------------------")
        print("Student Name :", self.name)
        print("Marks        :", self.marks)
        print("Average      :", round(avg, 2))
        print("Grade        :", grade)
        return avg

    def __gt__(self, other):
        print("Comparing Students Performance")
        print("--------------------------------")
        return self.calculate_performance() > other.calculate_performance()


# FACULTY 

class Faculty(Person):
    salary = SalaryDescriptor()

    def __init__(self, fid, name, department, salary):
        super().__init__(fid, name, department)
        self.salary = salary

    def get_details(self):
        print("Faculty Details:")
        print("--------------------------------")
        print("Name      :", self.name)
        print("Role      : Faculty")
        print("Department:", self.department)


# COURSE 

class Course:
    def __init__(self, code, name, credits, faculty):
        self.code = code
        self.name = name
        self.credits = credits
        self.faculty = faculty

    def __add__(self, other):
        return self.credits + other.credits

    def __iter__(self):
        yield self.code
        yield self.name
        yield self.credits


# DATA STORAGE 

class UniversityData:
    students = {}
    faculty = {}
    courses = {}
    enrollments = {}

    @staticmethod
    def student_generator():
        print("Student Record Generator")
        print("Fetching Student Records...")
        print("--------------------------------")
        for s in UniversityData.students.values():
            yield f"{s.id} - {s.name}"


# FILE HANDLING 

def save_students_json():
    data = []
    for s in UniversityData.students.values():
        data.append({
            "id": s.id,
            "name": s.name,
            "department": s.department,
            "semester": s.semester,
            "marks": s.marks
        })
    with open("students.json", "w") as f:
        json.dump(data, f, indent=2)
    print("Student data successfully saved to students.json")


def generate_csv():
    with open("students_report.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Name", "Department", "Average", "Grade"])
        for s in UniversityData.students.values():
            avg = sum(s.marks) / len(s.marks)
            grade = "A" if avg >= 80 else "B"
            writer.writerow([s.id, s.name, s.department, round(avg, 2), grade])
    print("CSV Report (students_report.csv)")


# MAIN MENU 

def main():
    while True:
        print("\n1 Add Student")
        print("2 Add Faculty")
        print("3 Add Course")
        print("4 Enroll Student to Course")
        print("5 Calculate Student Performance")
        print("6 Compare Two Students")
        print("7 Generate Reports")
        print("8 Exit")

        choice = input("Enter choice: ")

        try:
            if choice == "1":
                sid = input("Student ID: ")
                if sid in UniversityData.students:
                    raise Exception("Student ID already exists")
                name = input("Student Name: ")
                dept = input("Department: ")
                sem = int(input("Semester: "))
                marks = list(map(int, input("Marks: ").split()))
                s = Student(sid, name, dept, sem, marks)
                UniversityData.students[sid] = s
                print("Student Created Successfully")
                print("--------------------------------")
                print("ID        :", sid)
                print("Name      :", name)
                print("Department:", dept)
                print("Semester  :", sem)

            elif choice == "2":
                fid = input("Faculty ID: ")
                name = input("Faculty Name: ")
                dept = input("Department: ")
                sal = int(input("Monthly Salary: "))
                f = Faculty(fid, name, dept, sal)
                UniversityData.faculty[fid] = f
                print("Faculty Created Successfully")
                print("--------------------------------")
                print("ID        :", fid)
                print("Name      :", name)
                print("Department:", dept)

            elif choice == "3":
                code = input("Course Code: ")
                cname = input("Course Name: ")
                credits = int(input("Credits: "))
                fid = input("Faculty ID: ")
                course = Course(code, cname, credits, UniversityData.faculty[fid])
                UniversityData.courses[code] = course
                print("Course Added Successfully")
                print("--------------------------------")
                print("Course Code :", code)
                print("Course Name :", cname)
                print("Credits     :", credits)
                print("Faculty     :", UniversityData.faculty[fid].name)

            elif choice == "4":
                sid = input("Student ID: ")
                code = input("Course Code: ")
                UniversityData.enrollments[sid] = code
                print("Enrollment Successful")
                print("--------------------------------")
                print("Student Name :", UniversityData.students[sid].name)
                print("Course       :", UniversityData.courses[code].name)

            elif choice == "5":
                sid = input("Student ID: ")
                UniversityData.students[sid].calculate_performance()

            elif choice == "6":
                s1 = UniversityData.students[input("Student 1 ID: ")]
                s2 = UniversityData.students[input("Student 2 ID: ")]
                print(s1.name, ">", s2.name, ":", s1 > s2)

            elif choice == "7":
                generate_csv()
                save_students_json()
                for record in UniversityData.student_generator():
                    print(record)

            elif choice == "8":
                print("Thank you for using Smart University Management System")
                break

        except Exception as e:
            print("Error:", e)


# RUN 

if __name__ == "__main__":
    main()

