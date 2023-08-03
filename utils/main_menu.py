import re
from employee.views import add_employee, display_employee, display_employee_by_id, \
    delete_employee, update_employee, add_skills, get_skills, get_employee_basic_details
from project.views import add_project, add_employee_projects
from leave.views import insert_leave
from utils.validation import is_valid_employee_id
from utils.skills import Skill
from log.log import initialize_log

email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
date_pattern = re.compile(r'^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$')
logger = initialize_log()

"""
   Display employee menu and admin menu
"""


def show_menu(role):
    try:
        if role == 1:
            admin_menu()
        elif role == 2:
            print("""For Employee
                     1. Display all employee
                     2. Display employee details by employee id
                     3. Add Skills
                     4. Display Employee details and Skills
                     5. Exit""")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                display_employee()
                show_menu(role)
            elif choice == 2:
                display_employee_by_id()
                show_menu(role)
            elif choice == 3:
                print("Enter the skills details")
                emp_id = input("Enter the employee id: ")
                if is_valid_employee_id(emp_id) is False:
                    show_menu(role)
                print("Choose your skills")
                for skill in Skill:
                    print(f"{skill.value} {skill.name}")
                skill = int(input("Please enter your choice: "))
                add_skills(emp_id, skill)
                input("Press Any key To Continue")
                show_menu(role)
            elif choice == 4:
                emp_id = int(input("Enter the employee id: "))
                get_skills(emp_id)
                input("Press Any key To Continue")
                show_menu(role)
            elif choice == 5:
                exit()
            else:
                print("Invalid choice. Please try again")
                show_menu(role)
    except ValueError as ve:
        print("Invalid input..Please try again")
        show_menu(role)
        logger.error(str(ve))
    except Exception as ve:
        print("Cannot retrieve the data..Please try again")
        show_menu(role)
        logger.error(str(ve))


def admin_menu():
    try:
        print("""For Admin
                    1.Add Employee
                    2.Display all Employees
                    3.Display employee details by employee id
                    4.Delete Employee
                    5.Update Employee
                    6.Add Project
                    7.Add Project for Employee
                    8.Add Leaves for Employee
                    9.exit""")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print("Enter employee details to add")
            add_employee()
            input("Press Any key To Continue..")
            admin_menu()
        elif choice == 2:
            display_employee()
            admin_menu()
        elif choice == 3:
            emp_id = input("Enter the employee id: ")
            if is_valid_employee_id(emp_id) is False:
                admin_menu()
            display_employee_by_id(emp_id)
            admin_menu()
        elif choice == 4:
            emp_id = input("Enter the employee id to delete: ")
            if is_valid_employee_id(emp_id):
                delete_employee(emp_id)
            admin_menu()
        elif choice == 5:
            emp_id = input("Enter the employee id to update: ")
            if is_valid_employee_id() is False:
                admin_menu()
            employee_details = display_employee_by_id(emp_id)
            print(employee_details)
            print("Please enter the details to update")
            username = input("Please enter username: ")
            email = input("Please enter email: ")
            if re.match(email_pattern, email) is None:
                print("Invalid Email.. Please try again")
                get_employee_basic_details()
            no_of_experience = int(input("Please enter noofexperience : "))
            date_of_birth = input("Please enter dateofbirth in the format yyyy-MM-DD: ")
            if date_pattern.match(date_of_birth) is None:
                raise ValueError("Please enter valid date format yyyy-MM-DD")
            date_of_joining = input("Please enter dateofjoining in the format yyyy-MM-DD:")
            if date_pattern.match(date_of_joining) is None:
                raise ValueError("Please enter valid date format yyyy-MM-DD")
            update_employee(username, email, no_of_experience, date_of_birth, date_of_joining, emp_id, employee_details)
            input("Press Any key To Continue")
            admin_menu()
        elif choice == 6:
            add_project()
            input("Press Any key To Continue")
            admin_menu()
        elif choice == 7:
            add_employee_projects()
            input("Press Any key To Continue")
            admin_menu()
        elif choice == 8:
            insert_leave()
            input("Press Any key To Continue")
            admin_menu()
        elif choice == 9:
            exit()
        else:
            print("Invalid choice.Please try again")
            admin_menu()
    except ValueError:
        print(f"Invalid input..Please check the input type")
        admin_menu()
    except Exception as ve:
        print("Cannot retrieve the data..Please try again")
        admin_menu()
        logger.error(str(ve))
