from .sqlquery import save_project, save_employee_project


def add_projects(name, start_date, end_date):
    try:
        save_project(name, start_date, end_date)
    except Exception:
        raise


def add_employee_project(emp_id, project_name):
    try:
        save_employee_project(emp_id, project_name)
    except Exception:
        raise
