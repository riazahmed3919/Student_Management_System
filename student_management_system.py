class StudentDatabase:
    student_list = []

    @classmethod
    def add_student(cls, student_id, name, department, is_enrolled):
        student = Student(student_id, name, department, is_enrolled)
        cls.student_list.append(student)

    @classmethod
    def find_student_id(cls, student_id):
        for student in StudentDatabase.student_list:
            if student.get_student_id() == student_id:
                return student
        
        return None

class Student:
    def __init__(self, student_id, name, department, is_enrolled):
        self.__student_id =student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = is_enrolled

    def get_student_id(self):
        return self.__student_id

    def enroll_student(self):
        if not self.__is_enrolled:
            self.__is_enrolled = True
            print(f'{self.__name} has been successfully enrolled.')
        else:
            print(f'{self.__name} is already enrolled.')

    def drop_student(self):
        if self.__is_enrolled:
            self.__is_enrolled = False
            print(f'{self.__name} has dropped out.')
        else:
            print(f'{self.__name} is not enrolled yet.')

    def view_student_info(self):
        print(f'ID: {self.__student_id}, Name: {self.__name}, Department: {self.__department}, Enrolled: {self.__is_enrolled}')

StudentDatabase.add_student('S001', 'Johnny Depp', 'CSE', True)
StudentDatabase.add_student('S002', 'Robert Downey Jr', 'EEE', False)
StudentDatabase.add_student('S003', 'Tom Hardy', 'BBA', True)
StudentDatabase.add_student('S004', 'Rowan Atkinson', 'EEE', False)


# Replica System
while True:
    print("\n=== Student Management Menu ===")
    print("1. View All Students")
    print("2. Enroll Student")
    print("3. Drop Student")
    print("4. Exit")

    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        if not StudentDatabase.student_list:
            print('No student data found.')
        else:
            for student in StudentDatabase.student_list:
                student.view_student_info()

    elif choice == 2:
        student_id = input('Enter Student ID to enroll: ')
        student = StudentDatabase.find_student_id(student_id)
        
        if student:
            student.enroll_student()
        else:
            print(f'Invalid student id: {student_id}')

    elif choice == 3:
        student_id = input('Enter Student ID to drop: ')
        student = StudentDatabase.find_student_id(student_id)

        if student:
            student.drop_student()
        else:
            print(f'Invalid student id: {student_id}')

    elif choice == 4:
        print("You have exited the program.")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")