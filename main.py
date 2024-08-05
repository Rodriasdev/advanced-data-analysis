import MySQLdb
import sys
from db import connectdb
import pandas as pd

cursor, db = connectdb()


# try:
#     cursor.execute("DROP TABLE IF EXISTS EmployeePerformance")
#     cursor.execute("CREATE TABLE EmployeePerformance (id INT AUTO_INCREMENT PRIMARY KEY, employee_id INT, departament VARCHAR(255), performance_score FLOAT, years_with_company INT, salary FLOAT)")
# except MySQLdb.error as e:
#     print(e)
#     sys.exit(1)

try:
    cursor.execute("SELECT * FROM employeeperformance")
    data=cursor.fetchall()
except MySQLdb.error as e:
    print(e)
    sys.exit(1)

df = pd.DataFrame(data, columns=['id', 'employee_id', 'departament', 'performance_score', 'years_with_company', 'salary'])


mean_score = df['performance_score'].mean()
median_score = df['performance_score'].median()
std_dev_score = df['performance_score'].std()

print(df)