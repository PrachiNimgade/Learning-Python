# 1) Write a program that creates a dictionary like this 
# {
#     1: "red" , 2: "Blue" , 3: "Orange"
# }
# Now take the key as input from the user and print its corresponding colour 

# (Exception handle the code to terminate gracefully by printing 
# Colour not found if the key doesnot exists )


class my_own_exception(Exception):
    pass
try:
    values = input("Please enter colours of your choice comma seperated").split(',')
    keys = list(range(1,len(values)+1))
    my_dict = {}
    for i in range(len(keys)):
        my_dict[keys[i]] = values[i]

    user_input_key = int(input("Key : "))
    if user_input_key in my_dict : 
        print(my_dict[user_input_key])    
    else:
        raise my_own_exception  
     
except KeyError:
    print("Colour not found!!!!")    
except my_own_exception:
    print("From my_own_exception --- Colour not found!!!!")    