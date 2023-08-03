import getpass
from employee.service import validate_employee
from utils.main_menu import show_menu
from log.log import initialize_log

logger = initialize_log()


def login():
    """
       For Employee login
    """
    try:
        print("Enter the username and password for login")
        username = input("Please enter your username: ")
        password = getpass.getpass("Please enter your password: ")
        if username is None or not username or not password or password is None:
            raise ValueError("Bad request: username and password is required")
        employee = validate_employee(username, password)
        if employee:
            print("Login successful!")
            logger.info(f"Employee logged in username {username}")
            show_menu(employee[1])
        else:
            print("Invalid credentials..Please try again or if new employee please contact admin")
            login()
    except ValueError as ve:
        print(f"{str(ve)} ..Please try again")
        login()
    except Exception as e:
        print("Cannot retrieve the data ..Please try again")
        logger.error(e)
        login()


def show_main_menu():
    """
       For Display Main Menu
    """
    try:
        print("""Employee Management System
                1. Login
                2. Exit""")
        choice = int(input("Enter your choice"))
        if choice == 1:
            login()
        elif choice == 2:
            exit()
        else:
            print("Invalid choice")
            show_main_menu()
    except ValueError as ve:
        print("Invalid input..Please try again")
        logger.info(f"{str(ve)}")
        show_main_menu()
    except Exception as e:
        print(f"{str(e)} ..Please try again")
        show_main_menu()


show_main_menu()
