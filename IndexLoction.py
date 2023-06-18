class my_own_exeception(Exception):
    pass
try:
    dict = ["prachi", "nikhil", "ritik", "anushka"]
    print (dict)
    user_input_key = int(input("enter the element do you want to search : "))
    
    if (user_input_key<len(dict)):
        if dict[user_input_key] in dict :
            print(dict[user_input_key])
            
        else:
            raise my_own_exeception
except IndexError:
    print("Element not found")
except my_own_exeception:
   print("From my_own_exception --- Colour not found!!!!")    

        