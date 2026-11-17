
import psycopg2
import getpass


# Prompt for PostgreSQL password once at startup
password = getpass.getpass("Enter PostgreSQL password: ")


# Connect to the PostgreSQL database
def connect():
    return psycopg2.connect(
        host="localhost",
        database="student_db",
        user="postgres",
        password=password
    )


# 1. Retrieve and display all students
def getAllStudents():
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM students ORDER BY student_id")

    students = cur.fetchall()

    for student in students:
        print(student)

    cur.close()
    conn.close()


# 2. Add a new student
def addStudent(first_name, last_name, email, enrollment_date):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO students
        (first_name, last_name, email, enrollment_date)
        VALUES (%s, %s, %s, %s)
        """,
        (first_name, last_name, email, enrollment_date)
    )

    conn.commit()

    print("Student added successfully.")

    cur.close()
    conn.close()


# 3. Update a student's email
def updateStudentEmail(student_id, new_email):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        """
        UPDATE students
        SET email = %s
        WHERE student_id = %s
        """,
        (new_email, student_id)
    )

    conn.commit()

    if cur.rowcount > 0:
        print("Student email updated successfully.")
    else:
        print("Student not found.")

    cur.close()
    conn.close()


# 4. Delete a student
def deleteStudent(student_id):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM students WHERE student_id = %s",
        (student_id,)
    )

    conn.commit()

    if cur.rowcount > 0:
        print("Student deleted successfully.")
    else:
        print("Student not found.")

    cur.close()
    conn.close()


# Main application menu
def main():
    while True:
        print("\n--- Student Database Application ---")
        print("1. Display all students")
        print("2. Add a student")
        print("3. Update student email")
        print("4. Delete a student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            getAllStudents()

        elif choice == "2":
            first_name = input("First name: ")
            last_name = input("Last name: ")
            email = input("Email: ")
            enrollment_date = input("Enrollment date (YYYY-MM-DD): ")

            addStudent(first_name, last_name, email, enrollment_date)

        elif choice == "3":
            student_id = int(input("Enter student ID: "))
            new_email = input("Enter new email: ")

            updateStudentEmail(student_id, new_email)

        elif choice == "4":
            student_id = int(input("Enter student ID: "))

            deleteStudent(student_id)

        elif choice == "5":
            print("Exiting application.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
