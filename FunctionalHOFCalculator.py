def hof(funct):
    return funct()

def my_addition():
    first_num= int(input("please enter First number:"))
    second_num= int(input("please enter the Second number:"))
    return first_num+second_num

def my_square():
    first_num= int(input("please enter First number:"))
    return first_num**2

def my_exponentation():
    first_num= int(input("Please enter the First number:"))
    second_num= int(input("please enter the Second number:"))
    return first_num**second_num

while(True):
    print("Operation supported by our program are:")
    print("1: Addition")
    print("2: Sqaure")
    print("3: Exponentation")
    print("4: Exit the Program")
    
    choice = int(input("Please Enter Your Choice :"))
    
    if choice== 1:
        
        print("The Addition Of the number is", hof(my_addition))
        
    elif choice== 2:
        print("The Sqaure Of the number is", hof(my_square))
        
    elif choice== 3:
         print("The Exponentation Of the number is", hof(my_exponentation))
    elif choice== 4:
        break
    else :
        
        print("invalid input")
    