import mysql.connector

class Employee:

    def __init__(self):
        self.con = mysql.connector.connect(
            host = "localhost",
            user ="root",
            password ="root",
            database ="employee_db"
        )

        self.cursor = self.con.cursor()

    def add_employee(self):
        emp_id = int(input("Enter employee id: "))
        name = input("Enter Emp name: ")
        salary = float(input("Enter emp salary: "))
        department = input("Enter Department: ")

        query = "INSERT INTO employee VALUES (%s, %s, %s, %s)"

        values = (emp_id, name, salary, department)

        self.cursor.execute(query,values)
        self.con.commit()

        print("Employee added succesfully ")

    def display_employee(self):
        query = "SELECT * FROM employee"

        self.cursor.execute(query)
        employees = self.cursor.fetchall()

        if len(employees) == 0:
            print("No employee found")
        else: 
            for emp in employees:
                print(emp)

    def update_employee(self):
        emp_id= int(input("Enter employee ID to update: "))
        name = input("Enter new name: ")
        salary = float(input("Enter new salary: "))
        department = input("Enter new department: ")

        query = '''UPDATE employee SET name = %s, salary = %s, department = %s
        WHERE emp_id = %s
        '''

        values = (name, salary, department, emp_id)

        self.cursor.execute(query,values)
        self.con.commit()

        print("Employee updated successfully")

    def delete_employee(self):
        emp_id =int(input("Enter emp id to be deleted"))
        query = "DELETE FROM employee WHERE emp_id = %s"

        self.cursor.execute(query,(emp_id,))
        self.con.commit()

        print("Employee deleted succeefully")

employee = Employee()

while True:
    print("\n===== EMPLOYEE MANAGEMENT SYSTEM =====")
    print("1. Add Employee")
    print("2. Display Employees")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        employee.add_employee()

    elif choice == 2:
        employee.display_employee()

    elif choice == 3:
        employee.update_employee()

    elif choice == 4:
        employee.delete_employee()

    elif choice == 5:
        print("Program ended.")
        break

    else:
        print("Invalid choice!")