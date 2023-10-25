# Implement a function called sort_students

class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

# Function to define sorting key based on CGPA
def cgpa_key(student):
    return student.cgpa

# Test with different input lists of students
students_list = [
    Student("John", "2021001", 3.9),
    Student("Jane", "2021002", 3.7),
    Student("Alice", "2021003", 3.8),
    Student("Bob", "2021004", 3.6)
]

#sort the list of students by CGPA
sort_students = sorted(students_list, key=cgpa_key, reverse=True)


# Print the sorted list of students
for student in sort_students:
    print(f"Name: {student.name},  Roll Number: {student.roll_number}, CGPA: {student.cgpa}")