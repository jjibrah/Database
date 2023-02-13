from database import Employees

try:
    employees_name = input("Enter your name\n")
    employees_post = input("Enter your post\n")
    employees_salary = input("Enter your salary\n")
    Employees.create(name=employees_name, post=employees_post, salary=employees_salary)
    print("Data saved successfully")

except:
    print("Invalid Data")
