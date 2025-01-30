# main_program.py
from employee import Employee

# Create an object of Employee class
emp = Employee("John Doe", 50000)

# Display employee details
print(f"Employee Name: {emp.get_name()}")
print(f"Employee Salary: {emp.get_salary()}")

