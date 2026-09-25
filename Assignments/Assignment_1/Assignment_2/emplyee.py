import csv
import os

class Employee:
    def __init__(self, filename) -> None:
        self.filename = filename

    def create_file(self):
        if not os.path.exists(self.filename):
            with open(self.filename, "w", newline ="") as file:
                writer = csv.writer(file)
                writer.writerow(["id","name","department", "salary"])
# The C (create) operation
    def add_emplyee(self):
        emp_id = input("Enter Emp id: ")
        name = input("Enter Emp name: ")
        department = input("Enter department: ")
        salary = input("enter salary")

        with open(self.filename, "a", newline="")as file:
            writer = csv.writer(file)
            writer.writerow([emp_id, name, department, salary])

        print("Employee added sucessfully ")
# The R (read) operation
    def display_employee(self):
        with open(self.filename, 'r', newline="") as file:
            reader = csv.reader(file)

            for row in reader:
                print(row, " ")
# The U (update) operation
    def update_employee(self):
        emp_id = input("Enter the Id of the Employee to be updated: ")

        rows = []
        with open(self.filename, 'r', newline="") as file:
            reader = csv.reader(file)

            for row in reader:
                rows.append(row)

        found = False

        for row in rows:
            if row[0] == emp_id:
                row[1] = input("Enter new Name: ")
                row[2] = input("Enter new department: ")
                row[3] = input("Enter new salary: ")
                found = True
                break

        if found:
            with open(self.filename, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(rows)

            print("Employee added Sucessfully ")        

        else :
            print("Emplyee not found ")
# the D (delete) operation
    def delete_employee(self):
        emp_id = input("ENter Emp id to delete")

        rows =[]

        with open(self.filename, 'r', newline="") as file:
            reader = csv.reader(file)

            for row in reader:
                rows.append(row)

        found = False

        new_rows = [rows[0]]

        for row in rows[1:]:
            if row[0] == emp_id:
                found =True
            else:
                new_rows.append(row)

        if found :
            with open(self.filename,'w',newline="")as file:
                writer = csv.writer(file)
                writer.writerows(new_rows)

            print("Employee deleted Sucessfully")
        else:
            print("Employee not found")

employee = Employee("employee.csv")

employee.create_file()
print("CSV location:", os.path.abspath("employees.csv"))

while True:
    print("\n-----Employee Operations-----")
    print("1.Add Employee")
    print("2.Display Employee")
    print("3.Update Employee")
    print("4.Delete Employee")
    print("5.Exit")

    choice = input("Enter you choice: ")

    if choice == "1":
        employee.add_emplyee()
    elif choice == "2":
        employee.display_employee()
    elif choice == "3":
        employee.update_employee()
    elif choice == "4":
        employee.delete_employee()
    elif choice == "5":
        break
    else:
        print("-----END OF PROGRAM-----")