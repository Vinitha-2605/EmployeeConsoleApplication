import re
import getpass
from utils.validation import is_valid
from utils.roles import Role
from .service import add_employees, show_employees, show_employee_by_id, \
    update_employee_by_id, delete_by_id, add_employee_skills, get_employee_skills
from log.log import initialize_log

email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
date_pattern = re.compile(r'^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$')
logger = initialize_log()


def add_employee():
    username, password, email, role, age, no_of_experience, date_of_birth, date_of_joining = get_employee_basic_details()
    if is_valid(username, password, email, role, age, no_of_experience, date_of_birth, date_of_joining):
        add_employees(username, password, email, role, age, no_of_experience, date_of_birth, date_of_joining)


def display_employee_by_id(emp_id):
    try:
        result = show_employee_by_id(emp_id)
        print(result)
        input("Press Any key To Continue")
    except ValueError as ve:
        print(f"Invalid input {str(ve)}..Please try again")
    except Exception as ve:
        print("Cannot retrieve the data..Please try again")
        logger.error(str(ve))


def display_employee():
    print("List of employee")
    result = show_employees()
    print(result)
    input("Press Any key To Continue")


def update_employee(username, email, no_of_experience, date_of_birth, date_of_joining, emp_id, employee_details):
    update_employee_by_id(username, email, no_of_experience, date_of_birth, date_of_joining, emp_id, employee_details)


def delete_employee(emp_id):
    delete_by_id(emp_id)


def add_skills(emp_id, skill):
    add_employee_skills(emp_id, skill)


def get_skills(emp_id):
    get_employee_skills(emp_id)


def get_employee_basic_details():
    try:
        username = input("Please enter username: ")
        password = getpass.getpass("Please enter your password: ")
        email = input("Please enter email: ")
        if re.match(email_pattern, email) is None:
            print("Invalid Email.. Please try again")
            get_employee_basic_details()
        for role in Role:
            print(f"{role.value} {role.name}")
        role = int(input("Please enter your choice"))
        age = input("Please enter age: ")
        if age.isdigit() is False:
            raise ValueError("Age should only be integer")
        no_of_experience = input("Please enter noofexperience : ")
        if no_of_experience.isdigit() is False:
            raise ValueError("No_of_experience should only be integer")
        date_of_birth = input("Please enter dateofbirth in the format yyyy-MM-DD: ")
        if date_pattern.match(date_of_birth) is None:
            raise ValueError("Please enter valid date format yyyy-MM-DD")
        date_of_joining = input("Please enter dateofjoining in the format yyyy-MM-DD: ")
        if date_pattern.match(date_of_joining) is None:
            raise ValueError("Please enter valid date format yyyy-MM-DD")
        return username, password, email, role, age, no_of_experience, date_of_birth, date_of_joining
    except ValueError as ve:
        print(f"Invalid input..{str(ve)} Please try again")
        get_employee_basic_details()
