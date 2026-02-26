def createSampleData(filename):
    """Create sample student data file"""
    sample_data = """10
8439, wilhelm, 10,11,10,43
7521, aaron, 18,19,20,85
6543, rizen, 15,16,14,72
9876, tan, 12,13,11,55
5432, jed, 19,18,17,90
3210, jan, 14,15,13,68
8765, mark, 8,9,7,35
4321, nathan, 16,17,18,78
2109, xander, 11,12,10,48
6789, mc, 20,19,18,95"""
    
    with open(filename, 'w') as file:
        file.write(sample_data)
    print(f"Created {filename} with sample student data!")

def loadStudentData(filename):
    """Load student data from file"""
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        num_students = int(lines[0].strip())
        students = []
        
        for i in range(1, num_students + 1):
            data = lines[i].strip().split(',')
            student = {
                'code': data[0].strip(),
                'name': data[1].strip(),
                'coursework1': int(data[2].strip()),
                'coursework2': int(data[3].strip()),
                'coursework3': int(data[4].strip()),
                'exam': int(data[5].strip())
            }
            students.append(student)
        
        return students
    except FileNotFoundError:
        print(f"File {filename} not found. Creating sample file...")
        createSampleData(filename)
        return loadStudentData(filename)
    except Exception as e:
        print(f"Error loading data: {e}")
        return []

def saveStudentData(filename, students):
    """Save student data to file"""
    try:
        with open(filename, 'w') as file:
            file.write(f"{len(students)}\n")
            for student in students:
                line = f"{student['code']}, {student['name']}, "
                line += f"{student['coursework1']},{student['coursework2']},"
                line += f"{student['coursework3']},{student['exam']}\n"
                file.write(line)
        print("Data saved successfully!")
        return True
    except Exception as e:
        print(f"Error saving data: {e}")
        return False

def calculateTotals(student):
    """Calculate total coursework, overall percentage and grade"""
    total_coursework = student['coursework1'] + student['coursework2'] + student['coursework3']
    total_marks = total_coursework + student['exam']
    percentage = (total_marks / 160) * 100
    
    if percentage >= 70:
        grade = 'A'
    elif percentage >= 60:
        grade = 'B'
    elif percentage >= 50:
        grade = 'C'
    elif percentage >= 40:
        grade = 'D'
    else:
        grade = 'F'
    
    return total_coursework, percentage, grade

def displayStudentRecord(student):
    """Display a single student's record"""
    total_cw, percentage, grade = calculateTotals(student)
    
    print(f"\nStudent Name: {student['name']}")
    print(f"Student Number: {student['code']}")
    print(f"Total Coursework Mark: {total_cw}/60")
    print(f"Exam Mark: {student['exam']}/100")
    print(f"Overall Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")
    print("-" * 50)

def viewAllRecords(students):
    """Display all student records"""
    print("\n" + "="*50)
    print("ALL STUDENT RECORDS")
    print("="*50)
    
    if not students:
        print("No student records found!")
        return
    
    total_percentage = 0
    
    for student in students:
        displayStudentRecord(student)
        _, percentage, _ = calculateTotals(student)
        total_percentage += percentage
    
    avg_percentage = total_percentage / len(students)
    
    print(f"\nTotal Students: {len(students)}")
    print(f"Average Percentage: {avg_percentage:.2f}%")
    print("="*50)

def viewIndividualRecord(students):
    """View a single student's record"""
    if not students:
        print("No student records found!")
        return
    
    print("\n" + "="*50)
    print("SELECT A STUDENT")
    print("="*50)
    
    for i, student in enumerate(students, 1):
        print(f"{i}. {student['name']} ({student['code']})")
    
    try:
        choice = int(input("\nEnter student number (1-{}): ".format(len(students))))
        if 1 <= choice <= len(students):
            print("\n" + "="*50)
            displayStudentRecord(students[choice - 1])
        else:
            print("Invalid choice!")
    except ValueError:
        print("Invalid input!")

def showHighestScore(students):
    """Show student with highest overall mark"""
    if not students:
        print("No student records found!")
        return
    
    print("\n" + "="*50)
    print("STUDENT WITH HIGHEST SCORE")
    print("="*50)
    
    highest_student = max(students, key=lambda s: calculateTotals(s)[1])
    displayStudentRecord(highest_student)

def showLowestScore(students):
    """Show student with lowest overall mark"""
    if not students:
        print("No student records found!")
        return
    
    print("\n" + "="*50)
    print("STUDENT WITH LOWEST SCORE")
    print("="*50)
    
    lowest_student = min(students, key=lambda s: calculateTotals(s)[1])
    displayStudentRecord(lowest_student)

def sortStudentRecords(students):
    """Sort student records by overall percentage"""
    if not students:
        print("No student records found!")
        return
    
    print("\n" + "="*50)
    print("SORT STUDENT RECORDS")
    print("="*50)
    print("1. Ascending order (lowest to highest)")
    print("2. Descending order (highest to lowest)")
    
    choice = input("\nEnter your choice (1-2): ")
    
    if choice == '1':
        sorted_students = sorted(students, key=lambda s: calculateTotals(s)[1])
        print("\nStudents sorted in ascending order:")
    elif choice == '2':
        sorted_students = sorted(students, key=lambda s: calculateTotals(s)[1], reverse=True)
        print("\nStudents sorted in descending order:")
    else:
        print("Invalid choice!")
        return
    
    for student in sorted_students:
        displayStudentRecord(student)

def addStudentRecord(students):
    """Add a new student record"""
    print("\n" + "="*50)
    print("ADD NEW STUDENT RECORD")
    print("="*50)
    
    try:
        code = input("Enter student code (1000-9999): ").strip()
        if not (1000 <= int(code) <= 9999):
            print("Invalid student code!")
            return students
        
        name = input("Enter student name: ").strip()
        
        cw1 = int(input("Enter coursework 1 mark (0-20): "))
        cw2 = int(input("Enter coursework 2 mark (0-20): "))
        cw3 = int(input("Enter coursework 3 mark (0-20): "))
        exam = int(input("Enter exam mark (0-100): "))
        
        if not (0 <= cw1 <= 20 and 0 <= cw2 <= 20 and 0 <= cw3 <= 20 and 0 <= exam <= 100):
            print("Invalid marks entered!")
            return students
        
        new_student = {
            'code': code,
            'name': name,
            'coursework1': cw1,
            'coursework2': cw2,
            'coursework3': cw3,
            'exam': exam
        }
        
        students.append(new_student)
        print(f"\nStudent {name} added successfully!")
        
    except ValueError:
        print("Invalid input!")
    
    return students

def deleteStudentRecord(students):
    """Delete a student record"""
    if not students:
        print("No student records found!")
        return students
    
    print("\n" + "="*50)
    print("DELETE STUDENT RECORD")
    print("="*50)
    
    search = input("Enter student name or code: ").strip()
    
    found_indices = []
    for i, student in enumerate(students):
        if search.lower() in student['name'].lower() or search == student['code']:
            found_indices.append(i)
    
    if not found_indices:
        print("Student not found!")
        return students
    
    if len(found_indices) == 1:
        student = students[found_indices[0]]
        displayStudentRecord(student)
        confirm = input("\nAre you sure you want to delete this record? (yes/no): ").lower()
        if confirm == 'yes':
            students.pop(found_indices[0])
            print("Record deleted successfully!")
    else:
        print("\nMultiple students found:")
        for i in found_indices:
            print(f"{found_indices.index(i) + 1}. {students[i]['name']} ({students[i]['code']})")
        
        try:
            choice = int(input(f"\nSelect student to delete (1-{len(found_indices)}): "))
            if 1 <= choice <= len(found_indices):
                student = students[found_indices[choice - 1]]
                displayStudentRecord(student)
                confirm = input("\nAre you sure? (yes/no): ").lower()
                if confirm == 'yes':
                    students.pop(found_indices[choice - 1])
                    print("Record deleted successfully!")
        except ValueError:
            print("Invalid input!")
    
    return students

def updateStudentRecord(students):
    """Update a student record"""
    if not students:
        print("No student records found!")
        return students
    
    print("\n" + "="*50)
    print("UPDATE STUDENT RECORD")
    print("="*50)
    
    search = input("Enter student name or code: ").strip()
    
    found_index = -1
    for i, student in enumerate(students):
        if search.lower() in student['name'].lower() or search == student['code']:
            found_index = i
            break
    
    if found_index == -1:
        print("Student not found!")
        return students
    
    student = students[found_index]
    displayStudentRecord(student)
    
    print("\nWhat would you like to update?")
    print("1. Student name")
    print("2. Student code")
    print("3. Coursework marks")
    print("4. Exam mark")
    print("5. Cancel")
    
    choice = input("\nEnter your choice (1-5): ")
    
    try:
        if choice == '1':
            new_name = input("Enter new name: ").strip()
            students[found_index]['name'] = new_name
            print("Name updated successfully!")
        elif choice == '2':
            new_code = input("Enter new code (1000-9999): ").strip()
            if 1000 <= int(new_code) <= 9999:
                students[found_index]['code'] = new_code
                print("Code updated successfully!")
            else:
                print("Invalid code!")
        elif choice == '3':
            cw1 = int(input("Enter new coursework 1 mark (0-20): "))
            cw2 = int(input("Enter new coursework 2 mark (0-20): "))
            cw3 = int(input("Enter new coursework 3 mark (0-20): "))
            if 0 <= cw1 <= 20 and 0 <= cw2 <= 20 and 0 <= cw3 <= 20:
                students[found_index]['coursework1'] = cw1
                students[found_index]['coursework2'] = cw2
                students[found_index]['coursework3'] = cw3
                print("Coursework marks updated successfully!")
            else:
                print("Invalid marks!")
        elif choice == '4':
            exam = int(input("Enter new exam mark (0-100): "))
            if 0 <= exam <= 100:
                students[found_index]['exam'] = exam
                print("Exam mark updated successfully!")
            else:
                print("Invalid mark!")
        elif choice == '5':
            print("Update cancelled.")
        else:
            print("Invalid choice!")
    except ValueError:
        print("Invalid input!")
    
    return students

def displayMenu():
    """Display the main menu"""
    print("\n" + "="*50)
    print("STUDENT MANAGEMENT SYSTEM")
    print("="*50)
    print("1. View all student records")
    print("2. View individual student record")
    print("3. Show student with highest total score")
    print("4. Show student with lowest total score")
    print("5. Sort student records")
    print("6. Add a student record")
    print("7. Delete a student record")
    print("8. Update a student record")
    print("9. Save and Exit")
    print("="*50)

def main():
    """Main function"""
    print("Loading student data...")
    students = loadStudentData('studentMarks.txt')
    
    if not students:
        print("Unable to load student data.")
        students = []
    else:
        print(f"Successfully loaded {len(students)} student records!")
    
    while True:
        displayMenu()
        choice = input("\nEnter your choice (1-9): ")
        
        if choice == '1':
            viewAllRecords(students)
        elif choice == '2':
            viewIndividualRecord(students)
        elif choice == '3':
            showHighestScore(students)
        elif choice == '4':
            showLowestScore(students)
        elif choice == '5':
            sortStudentRecords(students)
        elif choice == '6':
            students = addStudentRecord(students)
        elif choice == '7':
            students = deleteStudentRecord(students)
        elif choice == '8':
            students = updateStudentRecord(students)
        elif choice == '9':
            save = input("Save changes before exiting? (yes/no): ").lower()
            if save == 'yes':
                saveStudentData('studentMarks.txt', students)
            print("\nThank you for using Student Management System!")
            break
        else:
            print("Invalid choice! Please enter 1-9.")

if __name__ == "__main__":
    main()