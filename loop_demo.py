# range(start, stop,step_size)
# print(list(range(2,20,3)))
# print(list(range(2,20)))
# print(list(range(4))) #print(list(range(0,4)))

# num=1 
# while(num<10):
#      print(num, end = " ")
#      num=num+1
#      break
     

# num=1 
# while(num<10):
#      print(num, end = " ")
#      num+=1
#      continue
 

# num=1 
# while(num<10):
#      if num<6 : 
#         print(num, end = " ")
#      num+=1

# num=1 
# while(num<10):
#      num+=1
#      if num<6 : 
#           print(num, end = " ")
     
     
        
# ***********************************************************
# Practice problem 1 
# ***********************************************************
# Create a game for FIZZ BUZ and keeping playing with the user untill the user chooses to skip the game
          
def fiz_buz(num) :
              if num % 3 == 0 and num % 5 == 0:
                   return "FIZZ BUZ"
              elif num % 3 == 0:
                   return "FIZZ"
              elif num % 5 == 0:
                   return "BUZ"
              else:
                   return str(num)



choice = 'Y'
while (choice == 'Y' or choice =='y' ):
     fiz_buz()
     choice = input("Do you want to continue, press anything other than Y")
     
          
              
          
          