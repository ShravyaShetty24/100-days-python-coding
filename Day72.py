# Online Course Enrollment Management System

courses = []

# Add Course
def add_course():

    course_id = int(input("Enter Course ID: "))
    course_name = input("Enter Course Name: ")
    fee = float(input("Enter Course Fee: "))

    for c in courses:
        if c["id"] == course_id:
            print("Course ID already exists")
            return

    course = {
        "id": course_id,
        "course_name": course_name,
        "fee": fee,
        "enrolled": 0
    }

    courses.append(course)
    print("Course added successfully")


# View Courses
def view_courses():

    if len(courses) == 0:
        print("No courses available")
    else:
        print("\n------ COURSE LIST ------")

        for c in courses:
            print("Course ID :", c["id"])
            print("Course Name :", c["course_name"])
            print("Fee :", c["fee"])
            print("Students Enrolled :", c["enrolled"])
            print()


# Search Course
def search_course():

    course_id = int(input("Enter Course ID: "))

    for c in courses:

        if c["id"] == course_id:

            print("\nCourse Found")
            print("Course Name :", c["course_name"])
            print("Fee :", c["fee"])
            print("Students Enrolled :", c["enrolled"])
            return

    print("Course not found")


# Enroll Student
def enroll_student():

    course_id = int(input("Enter Course ID: "))

    for c in courses:

        if c["id"] == course_id:

            c["enrolled"] += 1
            print("Student enrolled successfully")
            return

    print("Course not found")


# Update Course Fee
def update_fee():

    course_id = int(input("Enter Course ID: "))

    for c in courses:

        if c["id"] == course_id:

            new_fee = float(input("Enter New Course Fee: "))
            c["fee"] = new_fee

            print("Course fee updated successfully")
            return

    print("Course not found")


# Course Report
def course_report():

    total_students = 0

    for c in courses:
        total_students += c["enrolled"]

    print("Total Courses =", len(courses))
    print("Total Students Enrolled =", total_students)


# Main Program
while True:

    print("\n------ COURSE MENU ------")
    print("1. Add Course")
    print("2. View Courses")
    print("3. Search Course")
    print("4. Enroll Student")
    print("5. Update Course Fee")
    print("6. Course Report")
    print("7. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        add_course()

    elif ch == 2:
        view_courses()

    elif ch == 3:
        search_course()

    elif ch == 4:
        enroll_student()

    elif ch == 5:
        update_fee()

    elif ch == 6:
        course_report()

    elif ch == 7:
        print("Thank You")
        break

    else:
        print("Invalid Choice")