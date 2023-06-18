# template
class Student():
	
    #class variables 
    institute_name = 'CDAC'
    
    # class method
    @classmethod
    def change_institute_name(cls,in_institute_name):
        cls.institute_name = in_institute_name
        
    def __init__(self,in_name,in_rollno,in_subject_enrolled,in_pocket_money):
        # instance variables
        self.name = in_name
        self.rollno = in_rollno
        self.subject_enrolled = in_subject_enrolled
        self.pocket_money = in_pocket_money
     
     # instance method
    def display_object_details(self):
         print(f'Name {self.name} Rollno {self.rollno} subject : {self.subject_enrolled} pocket money : {self.pocket_money}')
    
    # static method
    @staticmethod
    def display_facilities():
        print('I am static method , i do not need any class or object reference (first parameter)')
        
# main method
def main():
    gaurav= Student("Gaurav",1,"Python",100)
    print(type(gaurav))
    gaurav.display_object_details()
    
    sagar= Student("Sagar",2,"Java",200)
    sagar.display_object_details()
    
    print(" Class variable printed ")
    print(f" Before Gaurav's institute: {gaurav.institute_name}")
    print(f"Before Sagar's institute: {sagar.institute_name}")
    Student.change_institute_name("Sunbeam")
    print(f" After Gaurav's institute: {gaurav.institute_name}")
    print(f"After Sagar's institute: {sagar.institute_name}")
    
    Student.display_facilities()
    gaurav.display_facilities()
    sagar.display_facilities()
    
    
# executing my main method
main()



