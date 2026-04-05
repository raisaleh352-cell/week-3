"""
Project Name: Student Attendance Tracking System Prototype
Description: This program creates a prototype for tracking student attendance
for a training institute.
"""
import random

# Global list to store student records as tuples 
studentList = []

class Student:
    def __init__(self, student_name="", attendance=0, course=""):
        # Automatically generate a unique student ID 
        self.student_id = random.randint(1000, 9999)
        self.student_name = student_name
        self.attendance = attendance
        self.course = course

    def add_student_attendance(self):
        """Allows staff to enter student details until 'done' is typed [cite: 6, 7]"""
        print("--- Add Student Records (Type 'done' as name to finish) ---")
        while True:
            name_input = input("Enter student name: ").strip()
            if name_input.lower() == "done":
                break
            
            try:
                # Prompt for attendance and course details [cite: 7]
                att_input = int(input("Enter attendance percentage: "))
                course_input = input("Enter course name: ")
                
                # Create a temporary student object to get a unique ID 
                new_student = Student(name_input, att_input, course_input)
                
                # Store record in the list as a tuple 
                studentList.append((new_student.student_id, new_student.student_name, 
                                    new_student.attendance, new_student.course))
                print(f"Record added. Generated ID: {new_student.student_id}\n")
            except ValueError:
                print("Invalid input. Attendance must be a number. Please try again.")

    def calculate_average_attendance(self):
        """Calculates the average attendance percentage for all recorded students [cite: 12]"""
        if not studentList:
            return 0
        total = sum(student[2] for student in studentList)
        return total / len(studentList)

    def update_attendance(self):
        """Update an existing record by searching for the Student ID [cite: 10]"""
        try:
            update_id = int(input("Enter student ID to update: "))
            for i in range(len(studentList)):
                if studentList[i][0] == update_id:
                    new_att = int(input("Enter new attendance percentage: "))
                    new_crs = input("Enter new course name: ")
                    # Modify the tuple in the list [cite: 10]
                    studentList[i] = (studentList[i][0], studentList[i][1], new_att, new_crs)
                    print("Updated successfully.")
                    return
            print("Student ID not found.")
        except ValueError:
            print("Invalid ID format.")

    def display_student_list(self):
        """Display all records and the final average [cite: 11, 12]"""
        if not studentList:
            print("\nNo records to display.")
            return

        print("\n--- Student Attendance Records ---")
        for student in studentList:
            print(f"ID: {student[0]} | Name: {student[1]} | Attendance: {student[2]}% | Course: {student[3]}")
        
        avg = self.calculate_average_attendance()
        print("-" * 30)
        print(f"The average attendance is: {avg:.2f}%")
        print("-" * 30)

# --- Execution ---
# Create an instance to run the system [cite: 14]
system = Student()
system.add_student_attendance()
system.display_student_list()
