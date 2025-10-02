
class SchoolManagement:
    def __init__(self):
        self.students = {}   # Store student records as {id: details}
        self.next_id = 1     # Auto-increment Student ID

    # ➔ New Admission
    def new_admission(self, name, age, student_class, mobile):
        # Validate age
        if not (5 <= age <= 18):
            raise ValueError("Age must be between 5 and 18.")
        # Validate mobile
        if not (mobile.isdigit() and len(mobile) == 10):
            raise ValueError("Mobile number must be exactly 10 digits.")

        student_id = self.next_id
        self.students[student_id] = {
            "Name": name,
            "Age": age,
            "Class": student_class,
            "Mobile": mobile
        }
        self.next_id += 1
        print(f"Admission successful! Student ID = {student_id}")
        return student_id

    # ➔ View Student Details
    def view_student(self, student_id):
        student = self.students.get(student_id)
        if student:
            print(f"Student ID: {student_id}, Details: {student}")
        else:
            print("Student not found!")

    # ➔ Update Student Info
    def update_student(self, student_id, mobile=None, student_class=None):
        student = self.students.get(student_id)
        if not student:
            print("Student not found!")
            return

        if mobile:
            if not (mobile.isdigit() and len(mobile) == 10):
                print("Invalid mobile number. Must be 10 digits.")
            else:
                student["Mobile"] = mobile
        if student_class:
            student["Class"] = student_class
        print(f"Student {student_id} updated successfully!")

    # ➔ Remove Student Record
    def remove_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            print(f"Student {student_id} removed successfully!")
        else:
            print("Student not found!")

    # ➔ Exit System
    def exit_system(self):
        print("Exiting School Management System. Goodbye!")
        exit()


# 🔹 Menu-driven program
if __name__ == "__main__":
    sms = SchoolManagement()

    while True:
        print("\n--- School Management System ---")
        print("1. New Admission")
        print("2. View Student Details")
        print("3. Update Student Info")
        print("4. Remove Student Record")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                name = input("Enter Student Name: ")
                age = int(input("Enter Age: "))
                student_class = int(input("Enter Class (1-12): "))
                mobile = input("Enter Guardian Mobile Number: ")
                sms.new_admission(name, age, student_class, mobile)
            except Exception as e:
                print("Error:", e)

        elif choice == "2":
            student_id = int(input("Enter Student ID: "))
            sms.view_student(student_id)

        elif choice == "3":
            student_id = int(input("Enter Student ID: "))
            mobile = input("Enter new Mobile Number (or press Enter to skip): ")
            student_class = input("Enter new Class (or press Enter to skip): ")
            sms.update_student(student_id,
                               mobile if mobile else None,
                               int(student_class) if student_class else None)

        elif choice == "4":
            student_id = int(input("Enter Student ID: "))
            sms.remove_student(student_id)

        elif choice == "5":
            sms.exit_system()

        else:
            print("Invalid choice! Please try again.")
