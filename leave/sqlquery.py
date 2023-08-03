import psycopg2
from log.log import initialize_log

con = psycopg2.connect(host='127.0.0.1', user='postgres', password='sql1234', database='EmployeeDetails')
cursor = con.cursor()
logger = initialize_log()


def save_employee_leaves(total_leave, casual_leave, sick_leave,
                         available, leave_taken, pending, approved, emp_id):
    try:
        values = (total_leave, casual_leave, sick_leave,
                  available, leave_taken, pending, approved, emp_id)
        sql = 'insert into "Leave" ("totalleave", "casualleave", "sickleave", "available", "leavetaken",' \
              ' "pending", "approved", "emp_id") ' \
              'values (%s,%s,%s,%s,%s,%s,%s,%s)'
        cursor.execute(sql, values)
        con.commit()
        print(cursor.rowcount, "record inserted")
    except Exception as e:
        logger.error(e)
        raise
