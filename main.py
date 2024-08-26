import MySQLdb
import sys
from db import connectdb
import pandas as pd
import matplotlib.pyplot as plt

cursor, db = connectdb()

# try:
#     cursor.execute("DROP TABLE IF EXISTS EmployeePerformance")
#     cursor.execute("CREATE TABLE EmployeePerformance (id INT AUTO_INCREMENT PRIMARY KEY, employee_id INT, departament VARCHAR(255), performance_score FLOAT, years_with_company INT, salary FLOAT)")
# except MySQLdb.error as e:
#     print(e)
#     sys.exit(1)


try:
    cursor.execute("SELECT * FROM employeeperformance")
    data = cursor.fetchall()
except MySQLdb.error as e:
    print(e)
    sys.exit(1)


df = pd.DataFrame(data, columns=['id', 'employee_id', 'departament', 'performance_score', 'years_with_company', 'salary'])

# Analisis de datos
mean_score = df['performance_score'].mean()
median_score = df['performance_score'].median()
std_dev_score = df['performance_score'].std()


mean_salary = df['salary'].mean()
median_salary = df['salary'].median()
std_dev_salary = df['salary'].std()

total_employees_per_department = df.groupby('departament').size().reset_index(name='total_employees')


corr_years_with_company_performance_score = df["years_with_company"].corr(df['performance_score'])


corr_salary_performance_score = df["salary"].corr(df['performance_score'])

# Visualización

departments = df['departament'].unique()
plt.figure(figsize=(10, 6))

for department in departments:
    subset = df[df['departament'] == department]
    plt.hist(subset['performance_score'], bins=10, alpha=0.5, label=department)

plt.xlabel('Performance Score')
plt.ylabel('Frequency')
plt.title('Histogram of Performance Score by Department')
plt.legend(loc='upper right')
plt.show()

plt.figure(figsize=(8, 5))
plt.scatter(df['years_with_company'], df['performance_score'], alpha=0.6)
plt.xlabel('Years with Company')
plt.ylabel('Performance Score')
plt.title('Scatter Plot of Years with Company vs. Performance Score')
plt.show()


plt.figure(figsize=(8, 5))
plt.scatter(df['salary'], df['performance_score'], alpha=0.6)
plt.xlabel('Salary')
plt.ylabel('Performance Score')
plt.title('Scatter Plot of Salary vs. Performance Score')
plt.show()

cursor.close()
db.close()
