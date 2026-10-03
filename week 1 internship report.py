students = []


# Add Student
def add_student():
    try:
        student_id = input("Enter Student ID: ")
        student_name = input("Enter Student Name: ")
        student_age = int(input("Enter Student Age: "))
        student_course = input("Enter Student Course: ")
        student_marks = int(input("Enter Student Marks: "))

        # Check marks
        if student_marks < 0 or student_marks > 100:
            print("Marks must be between 0 and 100.")
            return

        # Calculate result
        if student_marks >= 50:
            result = "Passed"
        else:
            result = "Failed"

        # Calculate grade
        if student_marks >= 90:
            grade = "A"
        elif student_marks >= 75:
            grade = "B"
        elif student_marks >= 60:
            grade = "C"
        elif student_marks >= 50:
            grade = "D"
        else:
            grade = "F"

        student_info = {
            "id": student_id,
            "name": student_name,
            "age": student_age,
            "course": student_course,
            "marks": student_marks,
            "grade": grade,
            "result": result
        }

        students.append(student_info)

        print("Student added successfully!")

    except ValueError:
        print("Please enter valid numeric values for age and marks.")


# View Students
def view_students():
    if len(students) == 0:
        print("No student records found.")
        return

    print("\n===== STUDENT RECORDS =====")

    for student in students:
        print("-------------------------")
        print("ID:", student["id"])
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Course:", student["course"])
        print("Marks:", student["marks"])
        print("Grade:", student["grade"])
        print("Result:", student["result"])


# Search Student
def search_student():
    search_id = input("Enter Student ID to search: ")

    for student in students:
        if student["id"] == search_id:
            print("\nStudent Found!")
            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Course:", student["course"])
            print("Marks:", student["marks"])
            print("Grade:", student["grade"])
            print("Result:", student["result"])
            return

    print("Student not found.")


# Update Student
def update_student():
    update_id = input("Enter Student ID to update: ")

    for student in students:
        if student["id"] == update_id:

            print("1. Update Name")
            print("2. Update Age")
            print("3. Update Course")
            print("4. Update Marks")

            choice = input("Enter your choice: ")

            if choice == "1":
                student["name"] = input("Enter new name: ")

            elif choice == "2":
                try:
                    student["age"] = int(input("Enter new age: "))
                except ValueError:
                    print("Invalid age.")
                    return

            elif choice == "3":
                student["course"] = input("Enter new course: ")

            elif choice == "4":
                try:
                    marks = int(input("Enter new marks: "))

                    if marks < 0 or marks > 100:
                        print("Marks must be between 0 and 100.")
                        return

                    student["marks"] = marks

                    if marks >= 50:
                        student["result"] = "Passed"
                    else:
                        student["result"] = "Failed"

                    if marks >= 90:
                        student["grade"] = "A"
                    elif marks >= 75:
                        student["grade"] = "B"
                    elif marks >= 60:
                        student["grade"] = "C"
                    elif marks >= 50:
                        student["grade"] = "D"
                    else:
                        student["grade"] = "F"

                except ValueError:
                    print("Invalid marks.")
                    return

            else:
                print("Invalid choice.")
                return

            print("Student updated successfully!")
            return

    print("Student not found.")


# Delete Student
def delete_student():
    delete_id = input("Enter Student ID to delete: ")

    for student in students:
        if student["id"] == delete_id:
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found.")


# Calculate Result
def calculate_result():
    student_id = input("Enter Student ID: ")

    for student in students:
        if student["id"] == student_id:

            marks = student["marks"]

            if marks >= 50:
                student["result"] = "Passed"
            else:
                student["result"] = "Failed"

            if marks >= 90:
                student["grade"] = "A"
            elif marks >= 75:
                student["grade"] = "B"
            elif marks >= 60:
                student["grade"] = "C"
            elif marks >= 50:
                student["grade"] = "D"
            else:
                student["grade"] = "F"

            print("Grade:", student["grade"])
            print("Result:", student["result"])
            return

    print("Student not found.")


# Save Records
def save_records():
    try:
        with open("student_records.txt", "w") as file:

            for student in students:
                file.write("ID: " + student["id"] + "\n")
                file.write("Name: " + student["name"] + "\n")
                file.write("Age: " + str(student["age"]) + "\n")
                file.write("Course: " + student["course"] + "\n")
                file.write("Marks: " + str(student["marks"]) + "\n")
                file.write("Grade: " + student["grade"] + "\n")
                file.write("Result: " + student["result"] + "\n")
                file.write("-------------------------\n")

        print("Records saved successfully!")

    except Exception as e:
        print("Error while saving records:", e)


# Main Menu
while True:

    print("\n===== STUDENT RECORD MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Calculate Result")
    print("7. Save Records")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        calculate_result()

    elif choice == "7":
        save_records()

    elif choice == "8":
        print("Thank you for using Student Record Management System!")
        break

    else:
        print("Invalid choice. Please try again.")