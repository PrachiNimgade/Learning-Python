# -------------------------------------------
# Exercise 01 : Classes and objects -- try creating this in oops world
# -------------------------------------------
# Employee
#   # instance variables 
#    emp_id
#    emp_salary
#    mgr_id
#   # class variable 
#   department_name
  
#   # instance methods
#   get_emp_salary()-> emp_salary
#   set_emp_salary(rcv_salary)-> emp_salary
#   display() --> displays all the values of the attributes of the class

#   # class method 
#   get_department_name() --> department_name
  
#   # static method
#   field_expertise() --> just displays some expertise for all my employees
  
# main:
# main

# 1) create an object employee(100,1000,1) 
# 2) display the employee object

class Employee():
    department_name='TCS'
    
           
    @classmethod
    def department_name(cls):
       return cls.department_name
   
    def __init__(self,rcv_emp_id,rcv_emp_salary,rcv_mgr_id):        
          # instance variables
        self.emp_id = rcv_emp_id
        self.emp_salary = rcv_emp_salary
        self.mgr_id = rcv_mgr_id
        
        
        print(f'was created succesfully with EmployeeId {self.emp_id} Salary {self.emp_salary}, ManagerId {self.mgr_id}')
        
        
         # instance method
    def get_emp_salary(self):
       return self.emp_salary
   
    def set_emp_salary(self,rcv_salary):
        self.emp_salary = rcv_salary
         
         
     
         
         # static method
    @staticmethod
    def field_expertice():
        print("Some Expetice")

    
       # # main method
def main():
    
    my_emp_emp_obj = Employee(1,10000,2)
    print(f"Employee id for the object is {my_emp_emp_obj.emp_id}")
    print(f"Employee id for the object is {my_emp_emp_obj.emp_salary}")
    print(f"Employee id for the object is {my_emp_emp_obj.mgr_id}")
    
    
    Employee.department_name()
    my_emp_emp_obj.department_name()
       
# # executing my main method
main()

# -------------------------------------------------------------------------------------------------------------------------------------
# second method

class My_airline :
    airline_name = 'Gaurav Airline'
    cities = {'Delhi','Pune','Mumbai','Bangalore','Chennai','Hyderabad','Patna','Trivandrum'}
    rows = set(range(1,21))
    section = {'A','B','C','D','E','F'}
    flight_numbers = set(range(564262,564362))
    
    def __init__(self,rcv_fn= None,rcv_dep = None , rcv_arr= None, rcv_sn = None) -> None:
        self.flight_number =  My_airline.flight_numbers.pop()  if rcv_fn is None else rcv_fn
        self.departure = My_airline.cities.pop() if rcv_dep is None else rcv_dep
        self.arrival = My_airline.cities.pop() if rcv_arr is None else rcv_arr
        self.seat_number = str(My_airline.rows.pop()) + My_airline.section.pop() if rcv_sn is None else rcv_sn
        
    def display_details(self):
        print(f"""Your ticket details :
--------------------------------------               
Airline_name : {My_airline.airline_name}
Flight_number : {self.flight_number}
Departure: {self.departure}
Arrival: {self.arrival}
Seat_number: {self.seat_number}
              
              """)   


def main():
   ticket_number1 = My_airline(1111111,'LONDON','USA','XXX1') 
   ticket_number2 = My_airline()
   
   ticket_number1.display_details()
   ticket_number2.display_details()

main()
