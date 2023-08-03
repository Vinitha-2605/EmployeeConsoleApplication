from .sqlquery import save_employee_leaves


def insert_employee_leaves(total_leave, casual_leave, sick_leave,
                           available, leave_taken, pending, approved, emp_id):
    try:
        save_employee_leaves(total_leave, casual_leave, sick_leave,
                             available, leave_taken, pending, approved, emp_id)
    except Exception as e:
        raise
