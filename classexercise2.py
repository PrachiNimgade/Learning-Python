
# Exercise 02 : Classes and objects -- try creating this in oops world

# Create a class that captures airline tickets. 
# Each ticket lists the departure and arrival cities, a flight number, and a seat assignment. 
# A seat assignment has both a row and a letter for the seat within the row (such as 12F). 

# main method:
# Make two examples of tickets being sold to passengers.
# display tickets booked details




class Airlines_Tickets():
    
    Number_Of_Cities = 'Indigo'
     
      # class method
    @classmethod
    def change_Number_Of_Cities(cls,Air_Cities):
      cls.Number_Of_Cities = Air_Cities
 
    def __init__(self, in_arrival_cities,in_flight_number,in_seat_assignment):
        # instance variables
      self.arrcity = in_arrival_cities
      self.fnumber = in_flight_number
      self.seatass = in_seat_assignment
        
        
    def display_object_details(self):
         print(f'was created succesfully with Arrival_Cities: {self.arrcity} \n Flight_Number: {self.fnumber} \n Seat_assignment: {self.seatass}')
              
    @staticmethod
    def display_facilities():
         print('We are Providing plain Services just like Vijay Mallya')
        
        
def main():
    
    city_name= input("Enter city name : ")
    flight_num=input("Enter flight number :")
    seat_ass= input("Enter seat assignment :")

    plain= Airlines_Tickets(city_name,flight_num,seat_ass)
    print(type(plain))
    plain.display_object_details()
    plain.display_facilities()  
    
    
main()
        
        
        
        