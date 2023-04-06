from database import DataBase

db = DataBase('class.db')

while True:
    print("\n===== Student Management System =====")
    print("1. Insert new student record")
    print("2. Read student record")
    print("3. Update student record")
    print("4. Delete student record")
    print("5. View all student records")
    print("6. Get Student list using city")
    print("7. Get Student list using name")
    print("8. Get Student list using age")
    print("9. Exit")
    choice = input("Enter your choice (1-9): ")
    if choice == '1':
        db.insert_student()
    elif choice == '2':
        db.read_student()
    elif choice == '3':
        db.update_student()
    elif choice == '4':
        db.delete_student()
    elif choice == '5':
        db.view_all_students()
    elif choice == '6':
        db.search_student_by_city()
    elif choice == '7':
        db.search_student_by_name()
    elif choice == '8':
        db.search_student_by_age()
    elif choice == '9':
        db.close_connection()
        break
    else:
        print("Invalid choice. Please try again.")