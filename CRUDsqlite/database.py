import sqlite3

class DataBase:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()
    

    def close_connection(self):
        self.conn.close()


    def create_table(self, table_name):
        self.cur.execute(f"""CREATE TABLE IF NOT EXISTS {table_name}
                        (id INTEGER PRIMARY KEY,
                        name VARCHAR(50) NOT NULL,
                        age INTEGER NOT NULL,
                        city VARCHAR(50) NOT NULL) """)

        
    def insert_student(self):
        while True:
            name = input("enter name: ").strip().capitalize()
            if not name.isalpha():
                print("Name can only contain letters and spaces. Please try again")
                continue
            break
        while True:
            try:
                age = int(input("enter age: "))
                if age < 0:
                    print("Age must be greater than or equal to zero")
                else:
                    break
            except ValueError:
                print("Enter valid integer age")
        while True:
            city = input("enter city: ").strip().capitalize()
            if not city.isalpha():
                print("City can only contain letters and spaces. Please try again")
                continue
            break
        self.cur.execute("INSERT INTO students (name, age, city) VALUES (?,?,?)", (name,age,city))
        self.conn.commit()
        print("Inserted data successfully")


    def read_student(self):
        try:
            id = int(input("Enter student id: "))
            self.cur.execute("SELECT * FROM students WHERE id = ?", (id,))
            row = self.cur.fetchone()
            if row:
                print(f"Id:{row[0]}")
                print(f"Name:{row[1]}")
                print(f"Age:{row[2]}")
                print(f"City:{row[3]}")
            else:
                print("No student found with this id")
        except ValueError:
            print("Please enter a valid Integer Id")
        except Exception as e:
            print("An error occured", e)


    def update_student(self):
        try:
            id = int(input("Enter student id: "))
            self.cur.execute("SELECT * FROM students WHERE id = ?", (id,))
            row = self.cur.fetchone()
            if row:
                print(f"Id:{row[0]}")
                print(f"Name:{row[1]}")
                print(f"Age:{row[2]}")
                print(f"City:{row[3]}")
                name = input("enter name: ")
                age = int(input("enter age: "))
                city = input("enter city: ")
                self.cur.execute("UPDATE students set name = ?, age = ?, city = ? WHERE id = ?", (name,age,city,id))
                self.conn.commit()
                print("Student record updated successfully")
            else:
                print("No student found with this id")

        except ValueError:
            print("Please enter a valid Integer Id")
        except Exception as e:
            print("An error occured", e)


    def delete_student(self):
        try:
            id = int(input("Enter student ID: "))
            self.cur.execute("SELECT * FROM students WHERE id = ?", (id,))
            row = self.cur.fetchone()
            if row:
                self.cur.execute("DELETE FROM students WHERE id = ?", (id,))
                self.conn.commit()
                print("Student record deleted successfully.")
            else:
                print("No student found with that ID.")

        except ValueError:
            print("Please enter a valid Integer Id")
        except Exception as e:
            print("An error occured", e)


    def view_all_students(self):
        self.cur.execute("SELECT * FROM students")
        rows = self.cur.fetchall()
        if rows:
            for row in rows:
                print(f"ID: {row[0]}")
                print(f"Name: {row[1]}")
                print(f"Age: {row[2]}")
                print(f"City: {row[3]}")
                print("--------------------")
        else:
            print("No student found")


    def search_student_by_city(self):
        while True:
            city = input("enter city: ").strip().capitalize()
            if not city.isalpha():
                print("City can only contain letters and spaces. Please try again")
                continue
            break
        self.cur.execute("SELECT * FROM students WHERE city = ?", (city,))
        rows = self.cur.fetchall()
        if(len(rows) == 0):
            print("No student lives in this city")
        else:
            for row in rows:
                print(f"ID: {row[0]}")
                print(f"Name: {row[1]}")
                print(f"Age: {row[2]}")
                print(f"City: {row[3]}")
                print("--------------------")


    def search_student_by_name(self):
        while True:
            name = input("search for name starting with: ").strip().capitalize()
            if not name.isalpha():
                print("Name can only contain letters and spaces. Please try again")
                continue
            break
        search_query = f"{name}%"
        self.cur.execute("SELECT * FROM students WHERE name LIKE ?", (search_query,))
        
        rows = self.cur.fetchall()
        if len(rows) == 0:
            print("No student found")
        else:
            for row in rows:
                print(f"ID: {row[0]}")
                print(f"Name: {row[1]}")
                print(f"Age: {row[2]}")
                print(f"City: {row[3]}")
                print("--------------------")

            
    def search_student_by_age(self):
        search_query = input("Enter age range (e.g. '20-30' or just 20): ").strip()
        if '-' in search_query:
            age_range = search_query.split('-')
            start_age, end_age = map(int, age_range) #iterates over age_range list and converts string to integer
            self.cur.execute("SELECT * FROM students WHERE age >= ? AND age <= ?", (start_age, end_age))
        else:
            self.cur.execute("SELECT * FROM students WHERE age = ?", (int(search_query),))
        
        rows = self.cur.fetchall()
        if len(rows) == 0:
            print("No student found")
        else:
            for row in rows:
                print(f"ID: {row[0]}")
                print(f"Name: {row[1]}")
                print(f"Age: {row[2]}")
                print(f"City: {row[3]}")
                print("--------------------")
