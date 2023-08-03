import re
from .service import add_projects
from utils.validation import is_valid_employee_id
from log.log import initialize_log

logger = initialize_log()

date_pattern = re.compile(r'^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$')


def add_project():
    try:
        print("Enter the project details")
        name = input("Enter the Project name")
        start_date = input("Please enter startdate in the format yyyy-MM-DD: ")
        if date_pattern.match(start_date) is None:
            raise ValueError("Please enter valid date format yyyy-MM-DD")
        end_date = input("Please enter enddate in the format yyyy-MM-DD:")
        if date_pattern.match(end_date) is None:
            raise ValueError("Please enter valid date format yyyy-MM-DD")
        add_projects(name, start_date, end_date)
    except ValueError as ve:
        print(str(ve))
    except Exception as e:
        print("Cannot retrieve the data..Please try again")
        logger.error(e)


def add_employee_projects():
    emp_id = input("Enter the employee id to add the project details")
    if is_valid_employee_id(emp_id) is False:
        add_employee_projects()
    project_name = input("Enter the project name")
    add_employee_projects(emp_id, project_name)
