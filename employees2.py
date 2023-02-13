from database import Employees

staff = Employees.select()


for employee in staff:
    print(employee.name, employee.post, employee.salary)