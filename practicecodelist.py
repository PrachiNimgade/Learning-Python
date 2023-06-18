# concatenate string
# type 1
# list1=["m","na","i","pra"]
# list2=["y","me","s","chi"]
# list3=[]
# for i in range(len(list1)):
#    list3.append(list1[i]+list2[i])
# print(list3)    

# type2

# list1=input("enter the list 1 :")
# list2=input("enter the list2 :")
# list3=[]
# for i in range(len(list1)):
#    list3.append(list1[i]+list2[i])
# print(list3)    


# l1=["m","na","i","pra"]
# l2=["y","me","s","chi"]
# l3= (l1 + l2)
# print(l3)




# Given a list of numbers. write a program to turn every item of a list into its square.

# l = [1, 2, 3, 4, 5, 6, 7]
# l1=[int(l[i])**2 for i in range(len(l))]
# print(l1)



# Given a two Python list. Write a program to iterate both lists simultaneously 
# and display items from list1 in original order and 
# items from list2 in reverse order.



# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# dict3= dict1.copy()
# dict3.update(dict2)
# print(dict3)





import datetime

def derive_age(date_of_birth):
    age_in_days = datetime.datetime.today() - date_of_birth 
    print("Age in days: ",age_in_days)

date_string = "21 April, 2023 00:00:00 000000"
datetime_object = datetime.datetime.strptime(date_string, "%d %B, %Y %H:%M:%S %f")

derive_age(datetime_object,10,10)
print("The datetime object in string format is " , datetime.datetime.strftime(datetime_object,'%A %B'))
    