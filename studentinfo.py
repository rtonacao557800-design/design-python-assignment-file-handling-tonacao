import os
students = {}

def validation():
    while True:
        studentID = input("Enter Student ID: ")
        if studentID.isdigit() and len(studentID) == 6: 
            return studentID
        else: 
            print("Invalid Student ID, Only 6 digit")

def addStudent():
    studentID = validation()
    if studentID in students:
        print("Student ID already exist in the database!")
        return
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    grades = []
    while True:
        grade = input("Enter Grade (or 'DONE' to finish): ")
        if grade.lower() == "done": break
        try: grades.append(int(grade))
        except ValueError: print("Invalid Grade, Try Again")
    students[studentID] = { "info": (studentID, name), "age": age, "grades": grades}

def updateStudent():
    id = input("Enter ID of student you want to Update: ")
    if id not in students: 
        print("Student ID doesn't exist")
        return
    update = int(input("What do you want to update \n[1] Name \n[2] Age \n[3] Grades \n[4] All \nAnswer: "))
    if update == 1: 
        NewName = input("Enter new Name: ")
        sid, _ = students[id]["info"]
        students[id]["info"] = (sid, NewName)
    elif update == 2: 
        NewAge = int(input("Enter new Age: "))
        students[id]["age"] = NewAge
    elif update == 3: 
        NewGrade = []
        while True:
            grade = input("Enter new Grade: (or 'DONE' to finish): ")
            if grade.lower() == "done": break
            try: NewGrade.append(int(grade))
            except ValueError: print("Invalid Grade, Try Again")
        students[id]["grades"] = NewGrade
    elif update == 4: 
        NewName = input("Enter new Name: ")
        NewAge = int(input("Enter new Age: "))
        NewGrade = []
        while True:
            grade = input("Enter new Grade: (or 'DONE' to finish): ")
            if grade.lower() == "done": break
            try: NewGrade.append(int(grade))
            except ValueError: print("Invalid Grade, Try Again")
        sid, _ = students[id]["info"]
        students[id]["info"] = (sid, NewName)
        students[id]["age"] = NewAge
        students[id]["grades"] = NewGrade
    else: 
        print("Invalid Input, Pls ")

def deleteStudent():
    id = input("Enter Student ID to Delete: ")
    if id not in students: 
        print("Student ID doesn't exist")
        return
    confirmation = input(f"Are you sure you want to Delete this Student {id}? (Y/N): ")
    if confirmation.lower() == "y":
        del students[id]
        print(f"Sucessfully Deleted Student {id}")
    else: 
        print("Deletion Canceled")

def displayStudent():
    if not students: 
        print("No Students found")
        return
    
    for sid, details in students.items():
        id, name = details["info"]
        age = details["age"]
        grades = details["grades"]
        print(f"Student ID: {id} \nName: {name} \nAge: {age} \nGrades ", end=" ")
        for g in grades:
            print(g, end=" ")
        print()

def saveTOfile():
    with open("tonacao.txt", "w") as rhea: 
        for sid, details in students.items():
            name = details["info"][1]
            age = details["age"]
            grades = ",".join(map(str, details["grades"]))  
            rhea.write(f"{sid}|{name}|{age}|{grades}\n")
    print("Student data saved to Database")

def loadFromfile():
    if not os.path.exists("tonacao.txt"):
        print("No saved file found")
        return
    with open("tonacao.txt", "r") as f:
        for line in f:
            sid, name, age, grades_str = line.strip().split("|")
            grades = list(map(int, grades_str.split(","))) if grades_str else []
            students[sid] = {"info": (sid, name), "age": age, "grades": grades}
    print("Student data loaded from tonacao.txt")

while True:
    choice = int(input("\n[1] Add Students \n[2] Display all Students \n[3] Update student Information \n[4] Delete a student Record" \
    "\n[5] Save student data to File \n[6] Load student data back from the File \n[7] Exit \nAnswer: "))
    if choice == 1: 
        addStudent()
    elif choice == 2: 
        displayStudent()
    elif choice == 3: 
        updateStudent()
    elif choice == 4: 
        deleteStudent()
    elif choice == 5: 
        saveTOfile()
    elif choice == 6: 
        loadFromfile()
    elif choice == 7: 
        break
    else: print("Invalid Input, Pls choose from 1-7 only")