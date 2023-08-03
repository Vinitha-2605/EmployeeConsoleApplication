import psycopg2

con = psycopg2.connect(host='127.0.0.1', user='postgres', password='sql1234', database='EmployeeDetails')
cursor = con.cursor()


def save_project(name,  start_date, end_date):
    try:
        values = (name,  start_date, end_date)
        sql = 'insert into "Project" ("name", "startdate", "enddate") values (%s,%s,%s)'
        cursor.execute(sql, values)
        con.commit()
        print(cursor.rowcount, "record inserted")
    except Exception as e:
        raise


def save_employee_project(emp_id, project_name):
    try:
        values = (emp_id, project_name)
        sql = 'insert into "EmployeeProject" ("emp_id", "project_id") ' \
              'values (%s, (select id from "Project" where "name" = %s))'
        cursor.execute(sql, values)
        con.commit()
        print(cursor.rowcount, "record inserted")
    except Exception as e:
        raise
