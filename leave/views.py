from .service import insert_employee_leaves
from log.log import initialize_log

logger = initialize_log()


def insert_leave():
    try:
        emp_id = int(input("Enter the employee id"))
        total_leave = int(input("Enter the totalleave"))
        casual_leave = int(input("Enter the casualleave"))
        sick_leave = int(input("Enter the sickleave"))
        available = int(input("Enter the available"))
        leave_taken = int(input("Enter the leave_taken"))
        pending = int(input("Enter the pending"))
        approved = int(input("Enter the approved"))
        insert_employee_leaves(total_leave, casual_leave, sick_leave,
                               available, leave_taken, pending, approved, emp_id)
    except ValueError:
        print("Invalid input..Please try again")
        insert_leave()
    except Exception as e:
        print("Cannot retrieve the data..Please try again")
        logger.error(e)
