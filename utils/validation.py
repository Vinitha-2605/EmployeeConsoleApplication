def is_valid(username, password, email, role, age, no_of_experience, date_of_birth, date_of_joining):
    try:
        if username is None or not username or password is None or not password\
                or email is None or not email or not age or \
                not no_of_experience or not date_of_birth or not date_of_joining:
            raise ValueError("Required input are missing")
        return True
    except ValueError as ve:
        print(str(ve))
        return False


def is_valid_employee_id(emp_id):
    try:
        if emp_id.isdigit() is False:
            raise ValueError("Employee id should be integer")
        return True
    except ValueError as ve:
        print(str(ve))
        return False
