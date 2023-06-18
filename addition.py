# def my_addition(first_num=10 , second_num=11):
#     return  first_num+ second_num

# def my_square(first_num):
#     return first_num**2

# def my_exponentation(first_num , second_num):
#     return first_num**second_num


# first_num = int(input("Please enter First number:"))
# second_num = int(input("Please enter Second number:"))

# print("The Addition of the numbers is ", str(my_addition(first_num,second_num)))
# print("First number squared is  ", str(my_square(first_num)))
# print("First number raised to number second number is  ", str(my_exponentation(first_num , second_num)))


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
     choice = input("Do you want to continue, press anything other than Y")
     fiz_buz()