# ----- Inheritance exercise ----
# 1. Define  
#   Person (superclass) that has name , place_of_residence , display_attributes()
#   Sister (subclass of Person)  that has additionally exam_subjects , display_attributes()
#   Uncle (subclass of Persom)  that has additionally business , display_attributes()

# main method:
# create a sister class object and display its attributes 
# create a Uncle class object and display its attributes 


class Person:
    def __init__(self,name,place_of_residence):
        self.name =name
        self.place_of_residence= place_of_residence
        
    def display_attributes(self):
            print(f"Name:{self.name}\n place Of Residence:{self.place_of_residence}")
            
            
            class Sister(Person):
                def __init__(self,name,place_of_residence,exam_subjects):
                    super().__init__(name,place_of_residence)
                    self.exam_subjects= exam_subjects
                    
                    def display_attributes(self):
                     super().display_attributes()
                    print(f"Exam Subjects:{self.exam_subjects}")
                    
                    class Uncle(Person):
                        def __init__(self, name, place_of_residence, business):
                            super().__init__(name, place_of_residence)
                            self.business= business
                            
                            def display_attributes(self):
                                super().display_attributes()
                                print(f"Business:{self.business}")
                                
                                

                                sister= Sister("Jane", "New York", ["Math","Science","English"])
                                sister.display_attributes()
                                    
                                uncle= Uncle("John", "Los Angeles", "Real Estate")
                                uncle.display_attributes()
                    