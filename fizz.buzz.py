"""Create a game for FIZZ BUZ and keeping playing with the user untill the user chooses to skip the game"""
def fizz_buzz():
    num = int(input("Please enter a number"))
    is_inside_if_clause = 'N'
    if num%3 == 0 :
        print("Fizz",end = ' ' )
        is_inside_if_clause = 'Y'

    if num%5 == 0 :
        print("Buzz")
        is_inside_if_clause = 'Y'

    if  is_inside_if_clause != 'Y':
        print("Invalid Input")


