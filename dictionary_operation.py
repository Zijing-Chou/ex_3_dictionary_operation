student = {
    "name": "Alice Wong",
    "student_id": "ST1024",
    "age": 21,
    "program": "Software Engineering",
    "city": "Nanjing",
    "gpa": 3.6
}


# first, display the complete record
for key, value in student.items():
    print(f"{key}: {value}")

# check for an email key
if "email" not in student:
    student["email"] = input("Enter email: ")

# update the city
new_city = input("Enter new city: ")
if new_city == "":
    print("City cannot be empty.")
else:
    student["city"] = new_city

# check for a phone key using get()
if student.get("phone") is None:
    print("Phone number not found.")

# add the contact dictionary
phone = input("Enter phone number: ")
student["contact"] = {
    "phone": phone,
    "email": student["email"]
}

# add the courses dictionary
student["courses"] = {
    "Python": 88,
    "Databases": 91,
    "Software Engineering": 84
}

# calculate the average score without sum()
total = 0
count = 0
for score in student["courses"].values():
    total = total + score
    count = count + 1
average = total / count

# add academic status
if average >= 90:
    student["academic_status"] = "Excellent"
elif average >= 75:
    student["academic_status"] = "Good"
elif average >= 60:
    student["academic_status"] = "Pass"
else:
    student["academic_status"] = "At Risk"

# search for a course
search_course = input("Enter course to search: ")
if search_course in student["courses"]:
    print(search_course + ": " + str(student["courses"][search_course]))
else:
    print("Course not found")

# update a course score
update_course = input("Enter course to update: ")
new_score = input("Enter new score: ")
if update_course in student["courses"]:
    if not new_score.isdigit():
        print("Score must be a number.")
    else:
        new_score = int(new_score)
        if new_score < 0 or new_score > 100:
            print("Score must be between 0 and 100.")
        else:
            student["courses"][update_course] = new_score
            print(update_course + " score updated.")
else:
    print("Course not found")

# recalculate the average and academic status
total = 0
count = 0
for score in student["courses"].values():
    total = total + score
    count = count + 1
average = total / count

if average >= 90:
    student["academic_status"] = "Excellent"
elif average >= 75:
    student["academic_status"] = "Good"
elif average >= 60:
    student["academic_status"] = "Pass"
else:
    student["academic_status"] = "At Risk"

# final student record
print("=====================================")
print("        STUDENT RECORD")
print("=====================================")
print()
print("Name:", student["name"])
print("Student ID:", student["student_id"])
print("Age:", student["age"])
print("Program:", student["program"])
print("City:", student["city"])
print("GPA:", student["gpa"])
print()
print("CONTACT")
print("Phone:", student["contact"]["phone"])
print("Email:", student["contact"]["email"])
print()
print("COURSE RESULTS")
for course, score in student["courses"].items():
    print(course + ": " + str(score))
print()
print("Average Score:", round(average, 1))
print("Academic Status:", student["academic_status"])
print()
print("=====================================")
