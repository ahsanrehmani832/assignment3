class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.courses = {}  # Dictionary to store enrolled courses and grades
    def enroll_in_course(self, course):
        self.courses[course.course_code] = None
        print(f"{self.name} enrolled in {course.course_name}")
    def submit_grade(self, course, grade):
        if course.course_code in self.courses:
            self.courses[course.course_code] = grade
            print(f"Grade submitted for {self.name} in {course.course_name}")
        else:
            print(f"{self.name} is not enrolled in {course.course_name}")
class Professor(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id
    def assign_grade(self, student, course, grade):
        student.submit_grade(course, grade)
        print(f"Grade assigned by {self.name} for {student.name} in {course.course_name}")
class Course:
    def __init__(self, course_code, course_name):
        self.course_code = course_code
        self.course_name = course_name


    def display_info(self):
        print(f"Course Code: {self.course_code}, Course Name: {self.course_name}")


# Example Usage:

# Create instances of Person, Student, Professor, and Course
person1 = Person("John Doe", 30)
student1 = Student("Alice", 20, "S001")
professor1 = Professor("Dr. Smith", 45, "P001")
course1 = Course("C001", "Introduction to Programming")

# Display information
person1.display_info()
student1.display_info()
professor1.display_info()
course1.display_info()

# Enroll student in a course
student1.enroll_in_course(course1)

# Assign grades by the professor
professor1.assign_grade(student1, course1, 85)

# Display student's enrolled courses and grades
print(f"{student1.name}'s Enrolled Courses and Grades:")
for course_code, grade in student1.courses.items():
    print(f"Course Code: {course_code}, Grade: {grade}")
