import csv
import os

FILE_NAME = "employee.csv"

def add_employee():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    department = input("Enter Department: ")
    salary = input("Enter Salary: ")

    file_exists = os.path.exists(FILE_NAME)

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["ID", "Name", "Department", "Salary"])

        writer.writerow([emp_id, name, department, salary])

    print("Employee added successfully!")

def display_employees():
    if not os.path.exists(FILE_NAME):
        print("No employee records found.")
        return

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.reader(file)

        for row in reader:
            print(row)

def search_employee():
    if not os.path.exists(FILE_NAME):
        print("No employee records found")
        return

    search_id = input("Enter Employee ID to search: ")

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for employee in reader:
            if employee["ID"] == search_id:
                print("Employee found:")
                print("ID:", employee["ID"])
                print("Name:", employee["Name"])
                print("Department:", employee["Department"])
                print("Salary:", employee["Salary"])
                return

    print("Employee not found")

def update_employee():
    if not os.path.exists(FILE_NAME):
        print("No employee records found.")
        return

    update_id = input("Enter Employee ID to update: ")

    employees = []
    found = False

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for employee in reader:

            if employee["ID"] == update_id:
                print("Enter new details:")

                employee["Name"] = input("Enter new name: ")
                employee["Department"] = input("Enter new department: ")
                employee["Salary"] = input("Enter new salary:")

                found = True

            employees.append(employee)

    if found:
        with open(FILE_NAME, "w", newline="") as file:
            fieldnames = ["ID", "Name", "Department", "Salary"]

            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(employees)

        print("Employee updated successfully!")

    else:
        print("Employee not found")
def delete_employee():
    if not os.path.exists(FILE_NAME):
        print("No employee records found.")
        return

    delete_id = input("Enter Employee ID to delete: ")
    employees = []

    found = False

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for employee in reader:
            if employee["ID"] == delete_id:
                found = True
            else:
                employees.append(employee)
    if found:
        with open(FILE_NAME, "w", newline="") as file:
            fieldnames = ["ID", "Name", "Department", "Salary"]

            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(employees)

        print("Employee deleted successfully!")

    else:
        print("Employee not found.")
while True:

    print("\n========== EMPLOYEE MANAGEMENT ==========")
    print("1. Add Employee")
    print("2. Display Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_employee()

    elif choice == "2":
        display_employees()

    elif choice == "3":
        search_employee()

    elif choice == "4":
        update_employee()

    elif choice == "5":
        delete_employee()

    elif choice == "6":
        print("Program ended.")
        break

    else:
        print("Invalid choice. Please try again.")