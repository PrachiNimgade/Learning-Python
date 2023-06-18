# 3) Create program that takes age of the user as input 
# and prints number of days that user has lived for 
# Exception handle the code such that if the user has lived for more than 
# 100001 days then user should get the message
# , you lived for so long , may be you will die soon:)


from datetime import datetime
name = input('What is your name? \n')
age = int(input('How old are you? \n'))
hundred = int((100-age) + datetime.now().year)
print ('Hello %s. You are %s years old. You will turn 100 years old in %s.' % (name, age, hundred))