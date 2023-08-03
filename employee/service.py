from .sqlquery import show_employee, get_employee_by_id, \
    update_employee, delete_employee_by_id, get_employee, \
    save_employee, save_skills, show_employee_skills


def validate_employee(name, password):
    try:
        employee = get_employee(name, password)
        return employee
    except Exception as e:
        print(e)
        raise


def add_employees(name, password, email, role, age, no_of_experience, date_of_birth, date_of_joining):
    try:
        save_employee(name, password, email, role, age, no_of_experience, date_of_birth, date_of_joining)
    except Exception as e:
        print(e)
        raise


def show_employees():
    try:
        result = show_employee()
        employees = {}
        for item in result:
            employees['name'] = item[0]
            employees['email'] = item[1]
            employees['no_of_experience'] = item[2]
            employees['date_of_birth'] = str(item[3])
            employees['date_of_joining'] = str(item[4])
            employees['project'] = item[5]
            employees['organisationname'] = item[6]
        return employees
    except IndexError:
        print("Index out of range")
    except Exception as e:
        print(e)
        raise


def show_employee_by_id(emp_id):
    try:
        result = get_employee_by_id(emp_id)
        employees = {}
        for item in result:
            employees['name'] = item[0]
            employees['email'] = item[1]
            employees['no_of_experience'] = item[2]
            employees['date_of_birth'] = str(item[3])
            employees['date_of_joining'] = str(item[4])
            employees['project'] = item[5]
            employees['organisationname'] = item[6]
        return employees
    except IndexError:
        print("Index out of range")
    except Exception as e:
        print(e)
        raise


def update_employee_by_id(username, email, no_of_experience, date_of_birth, date_of_joining, emp_id, result):
    try:
        username = result['name'] if username == '' else username
        email = result['email'] if email == '' else email
        no_of_experience = result['no_of_experience'] if no_of_experience == '' else int(no_of_experience)
        date_of_birth = result['date_of_birth'] if date_of_birth == '' else date_of_birth
        date_of_joining = result['date_of_joining'] if date_of_joining == '' else date_of_joining
        update_employee(username, email, no_of_experience, date_of_birth, date_of_joining, emp_id)
    except Exception as e:
        print(e)
        raise


def delete_by_id(emp_id):
    delete_employee_by_id(emp_id)


def add_employee_skills(emp_id, skill):
    save_skills(emp_id, skill)


def get_employee_skills(emp_id):
    print(show_employee_skills(emp_id))
