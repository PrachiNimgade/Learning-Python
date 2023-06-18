"""3) Define a variable named "raise_salary_percentage" and get the salary raise 
percentage from the user, Now apply the raise to an employee
with harcoded data Name= 'gaurav' existing_salary = 900 INR and 
print the incremented salary to the console"""

raise_salary_percentage = float(input("Enter the percentage of the salary raise:"))
name = 'Gaurav'
existing_salary = 1000
incremented_salary = existing_salary + (existing_salary*raise_salary_percentage/100)
print(f"The new salary of {name} is {incremented_salary:.2f} INR")