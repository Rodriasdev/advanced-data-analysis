import MySQLdb
import sys
from db import connectdb
import pandas as pd
import matplotlib.pyplot as plt

class EmployeePerformanceAnalyzer:
    def __init__(self):
        self.cursor, self.db = connectdb()
        self.df = None

    def fetch_data(self):
        try:
            self.cursor.execute("SELECT * FROM employeeperformance")
            data = self.cursor.fetchall()
            self.df = pd.DataFrame(data, columns=['id', 'employee_id', 'departament', 'performance_score', 'years_with_company', 'salary'])
        except MySQLdb.error as e:
            print(e)
            sys.exit(1)

    def calculate_statistics(self):
        mean_score = self.df['performance_score'].mean()
        median_score = self.df['performance_score'].median()
        std_dev_score = self.df['performance_score'].std()

        mean_salary = self.df['salary'].mean()
        median_salary = self.df['salary'].median()
        std_dev_salary = self.df['salary'].std()

        print(f"Performance Score - Mean: {mean_score}, Median: {median_score}, Std Dev: {std_dev_score}")
        print(f"Salary - Mean: {mean_salary}, Median: {median_salary}, Std Dev: {std_dev_salary}")

        return {
            'mean_score': mean_score,
            'median_score': median_score,
            'std_dev_score': std_dev_score,
            'mean_salary': mean_salary,
            'median_salary': median_salary,
            'std_dev_salary': std_dev_salary
        }

    def calculate_correlations(self):
        corr_years_with_company_performance_score = self.df["years_with_company"].corr(self.df['performance_score'])
        corr_salary_performance_score = self.df["salary"].corr(self.df['performance_score'])

        print(f"Correlation between Years with Company and Performance Score: {corr_years_with_company_performance_score}")
        print(f"Correlation between Salary and Performance Score: {corr_salary_performance_score}")

        return {
            'corr_years_with_company_performance_score': corr_years_with_company_performance_score,
            'corr_salary_performance_score': corr_salary_performance_score
        }

    def plot_histogram_performance_score(self):
        departments = self.df['departament'].unique()
        plt.figure(figsize=(10, 6))

        for department in departments:
            subset = self.df[self.df['departament'] == department]
            plt.hist(subset['performance_score'], bins=10, alpha=0.5, label=department)

        plt.xlabel('Performance Score')
        plt.ylabel('Frequency')
        plt.title('Histogram of Performance Score by Department')
        plt.legend(loc='upper right')
        plt.show()

    def plot_scatter_years_vs_performance(self):
        plt.figure(figsize=(8, 5))
        plt.scatter(self.df['years_with_company'], self.df['performance_score'], alpha=0.6)
        plt.xlabel('Years with Company')
        plt.ylabel('Performance Score')
        plt.title('Scatter Plot of Years with Company vs Performance Score')
        plt.show()

    def plot_scatter_salary_vs_performance(self):
        plt.figure(figsize=(8, 5))
        plt.scatter(self.df['salary'], self.df['performance_score'], alpha=0.6)
        plt.xlabel('Salary')
        plt.ylabel('Performance Score')
        plt.title('Scatter Plot of Salary vs Performance Score')
        plt.show()

    def close_connection(self):
        self.cursor.close()
        self.db.close()

def main():
    analyzer = EmployeePerformanceAnalyzer()
    analyzer.fetch_data()
    analyzer.calculate_statistics()
    analyzer.calculate_correlations()
    analyzer.plot_histogram_performance_score()
    analyzer.plot_scatter_years_vs_performance()
    analyzer.plot_scatter_salary_vs_performance()
    analyzer.close_connection()

if __name__ == "__main__":
    main()
