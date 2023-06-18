# days_in_moth= int(input("Enter the number of days in the month: "))
# start_day= int(input("Enter the number of day of the week the month starts on: "))

# print("S M T W T F S")

# num_spaces =start_day * 3

# for i in range(start_day):
#     print(" ", end="")
    
#     for i in range(1, 8 -start_day):
#         print("{%f}".format(i), end=" ")
#         print()
        
    
#     day_of_week = (start_day + 7) % 7
#     for day in range(8 - start_day, days_in_moth + 1): 
#      print("{%f}".format(day), end=" ")
#     day_of_week+= 1
#     if day_of_week %7 == 0:
#         print()
#         print()
    
    
    
def main():
    n= int(input("Enter the num of days in the month (28-31):"))
    d= int(input("Enter the number of days of the month start on:"))
    i= 1
    print("S M T W T F S")
    while i<= n:
        print (i),
        if(i+d) % 7 == 0:
            print (" ")
            i = i +1
            
            main()

        