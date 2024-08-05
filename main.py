import MySQLdb
import sys
from db import connectdb

cursor, db = connectdb()


try:
    cursor.execute("DROP TABLE IF EXISTS EmployeePerformance")
    cursor.execute("CREATE TABLE EmployeePerformance (id INT AUTO_INCREMENT PRIMARY KEY, employee_id INT, departament VARCHAR(255), performance_score FLOAT, years_with_company INT, salary FLOAT)")
except MySQLdb.error as e:
    print(e)
    sys.exit(1)