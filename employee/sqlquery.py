import psycopg2
from config.dbconfig import config
from log.log import initialize_log

db_config = config()
con = psycopg2.connect(host=db_config["host"], user=db_config["user"], password=db_config["password"],
                       database=db_config["database"])
cursor = con.cursor()
logger = initialize_log()


def get_employee(name, password):
    try:
        values = (name, password)
        sql = '''select "Employee".id, "Employee".role_id from "Employee"
              where "Employee".UserName = %s and "Employee".Password = %S'''
        cursor.execute(sql, values)
        con.commit()
        return cursor.fetchone()
    except ValueError:
        raise
    except Exception as e:
        logger.error(e)
        raise


def save_employee(name, password, email, role, age, no_of_experience, date_of_birth, date_of_joining):
    try:
        values = (name, password, email, role, age, no_of_experience, date_of_birth, date_of_joining)
        sql = 'insert into "Employee" ("username", "password", "emailid", "role_id", "age",' \
              ' "noofexperience", "dateofbirth", "dateofjoining") ' \
              'values (%s,%s,%s,%s,%s,%s,%s,%s)'
        cursor.execute(sql, values)
        con.commit()
        print(cursor.rowcount, "record inserted")
    except Exception as e:
        logger.error(e)
        raise


def show_employee():
    try:
        sql = '''SELECT  "Employee"."username", "Employee"."emailid", "Employee"."noofexperience",
              "Employee"."dateofbirth", "Employee"."dateofjoining",
               STRING_AGG("Project".name, ', ') AS project_names,
               "Organisation"."organisationname"
               FROM "Employee"
               JOIN "EmployeeProject" ON "Employee".id = "EmployeeProject".emp_id
               JOIN "Project" ON "EmployeeProject".project_id = "Project".id
               JOIN "Organisation" ON "Employee".org_id = "Organisation".id
               GROUP BY "Employee".id, "Organisation".id'''
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        logger.error(e)
        raise


def get_employee_by_id(emp_id):
    try:
        values = (emp_id,)
        sql = '''SELECT "Employee"."username", "Employee"."emailid", "Employee"."noofexperience",
              "Employee"."dateofbirth", "Employee"."dateofjoining",
               STRING_AGG("Project".name, ', ') AS project_names,
               "Organisation"."organisationname"
               FROM "Employee"
               JOIN "EmployeeProject" ON "Employee".id = "EmployeeProject".emp_id
               JOIN "Project" ON "EmployeeProject".project_id = "Project".id
               JOIN "Organisation" ON "Employee".org_id = "Organisation".id
               where "Employee".id= %s
               GROUP BY "Employee".id, "Organisation".id'''
        cursor.execute(sql, values)
        con.commit()
        return cursor.fetchall()
    except Exception as e:
        logger.error(e)
        raise


def update_employee(username, email, no_of_experience, date_of_birth, date_of_joining, emp_id):
    try:
        values = (username, email, no_of_experience, date_of_birth, date_of_joining, emp_id)
        sql = 'update "Employee" set "username"= %s, "emailid"= %s, '\
              ' "noofexperience"= %s, "dateofbirth"= %s, "dateofjoining"= %s where id= %s'
        cursor.execute(sql, values)
        con.commit()
        print(cursor.rowcount, "record inserted")
    except Exception as e:
        logger.error(e)
        raise


def delete_employee_by_id(emp_id):
    try:
        values = (emp_id,)
        sql = 'delete from "Employee" where id= %s'
        cursor.execute(sql, values)
        con.commit()
        print("Deleted Successfully")
    except Exception as e:
        logger.error(e)
        raise


def save_skills(emp_id, skill):
    try:
        values = (emp_id, skill)
        sql = 'insert into "EmployeeSkills" ("emp_id", "skill_id") ' \
              'values (%s, %s)'
        cursor.execute(sql, values)
        con.commit()
        print(cursor.rowcount, "record inserted")
    except Exception as e:
        logger.error(e)
        raise


def show_employee_skills(emp_id):
    try:
        values = (emp_id,)
        sql = '''SELECT  "Employee"."username", "Employee"."emailid", "Employee"."noofexperience",
               STRING_AGG("Skills"."skillname", ', ') AS skill_names 
               FROM "Employee"
               JOIN "EmployeeSkills" ON "Employee".id = "EmployeeSkills".emp_id
               JOIN "Skills" ON "EmployeeSkills".skill_id = "Skills".id where "Employee".id= %s
               GROUP BY "Employee".id'''
        cursor.execute(sql, values)
        return cursor.fetchall()
    except Exception as e:
        logger.error(e)
        raise
