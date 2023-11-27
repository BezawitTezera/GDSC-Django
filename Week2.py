import sys

Student_Databases = []

while True:
    name = input("Name: ")
    age = input("Age: ")
    grade = input("Grade: ")
    Student_Database = {'Name': name, 'Age': age, 'Grade': grade}
    Student_Databases.append(Student_Database)

    answer = input("Do you want to add more students? y/n ")
    if answer.lower()  != 'y':
        break

while True:
    choice = input("Do you want to: \n 1. View student's information \n 2. List all students information \n 3. Update student's information \n 4. Delete a student's information. \n 5. Exit    ")
    if choice == "1":
        found = False
        username = input("Enter the name of the student: ")
        for student in Student_Databases:     
            if student['Name'] == username:
                print(student)
                found = True
                break
        if not found:
            print("Student doesn't exist.")

    elif choice == "2":
        print(Student_Databases)

    elif choice =="3":
        UpdatedUser = input("Enter the name of the student you want to modify? ")
        found = False
        for index, student in enumerate (Student_Databases):
            if student['Name'] == UpdatedUser:            
                new_name = input("Name: ")
                new_age = input("Age: ")
                new_grade = input("Grade: ")
                student = {'Name': new_name, 'Age': new_age, 'Grade': new_grade}
                Student_Databases[index] = student
                print(f"The information is modified as {student}.")
                found = True
                break
        if not found:
            print("Student doesn't exist.")
        
    elif choice == "4":
        DeleteUser = input("Enter the name of the student you want to delete? ")
        found = False
        for student in Student_Databases:
            if student['Name'] == DeleteUser: 
                print(f"Student {DeleteUser} is deleted from the dictionary!")
                Student_Databases.remove(student)
                found  = True
                break
        if not found:
            print("Student doesn't exist.")

    elif choice == "5":
        sys.exit(0)

    else:
        print("Invalid key.")
 

