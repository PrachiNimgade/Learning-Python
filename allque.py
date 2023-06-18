# #  Using for loop, write and run a Python program for this algorithm.
# # 10 Factorial = 10*9*8*7*6*5*4*3*2*1

# fact = 1
# for i in range(int(input('Enter number: ')),1,-1):
#     fact*= i
# print(fact)    

# #.2. Modify the program above using a while loop so it prints out all of the factorial values that are 
# # less than 2 billion. (You should be able to do this without looking at the output of the previous 
# # exercise.)


# fact = 1
# input_num = int(input("Please enter number: "))
# cnt = input_num
# while ( cnt > 1 ):
#     fact = fact*cnt 
#     cnt = cnt-1

# if fact < 2000000 :
#     print(fact)    
# else:
#     print("Sorry limit excedded of 2 Billion ")    

# input_number_of_days = int(input("Days: "))
# start_day_of_week = int(input('0: Monday 1 : Tuesday ... '))
# print(f'S  M  T  W  T  F  S')
# cnt = 1
# for i in range((start_day_of_week-1)*-1, input_number_of_days+1,1):
#     print(f'{i:2}' if i > 0 else ' ' , end= ' ')
#     if cnt%7 == 0 :
#         print('')
#     cnt = cnt+1    






# key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 
# 'p':'c', 'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k', 'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 
# 'F':'S', 'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A', 'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 
# 'T':'G', 'U':'H', 'V':'I', 'W':'J', 'X':'K', 'Y':'L', 'Z':'M', ' ': ' '}

# secret_message = 'Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!'
# for i in secret_message:
#     print( key.get(i) , end = '')
    
    
    
    
    
    
#     Write a version of a palindrome recognizer that also accepts phrase palindromes such as "Go
# hang a salami I'm a lasagna hog.", "Was it a rat I saw?", "Step on no pets", "Sit on a potato pan,
# Otis", "Lisa Bonet ate no basil", "Satan, oscillate my metallic sonatas", "I roamed under it as a tired
# nude Maori", "Rise to vote sir", or the exclamation "Dammit, I'm mad!". Note that punctuation,
# capitalization, and spacing are usually ignored.
    
# import re
# def palindrome_recognizer(words):
#     album = []
#     word=re.sub('[^a-zA-Z]','',words).lower()
#     for str in (word):
#         album.insert(0, str)
#     if word==(''.join(album)):
#         return True
#     else:
#         return  False
# a=palindrome_recognizer("I am testing")
# print(a)
# b=palindrome_recognizer("Go hang a salami I'm a lasagna hog.")
# print(b)
# c=palindrome_recognizer("Was it a rat I saw?")
# print(c)
# d=palindrome_recognizer("Sit on a potato pan, Otis")
# print(d)
# e=palindrome_recognizer("Dammit, I'm mad!")
# print(e)
    
    
    
    
# #     A pangram is a sentence that contains all the letters of the English alphabet at least once, for
# example: The quick brown fox jumps over the lazy dog. Your task here is to write a function to
# check a sentence to see if it is a pangram or not.

# def pangram(string):
#     string = string.lower()
#     alphabet = ['a','b','c','d','e','f','g','h',\
#                 'i','j','k','l','m','n','o','p',\
#                 'q','r','s','t','u','v','w','x','y','z']

#     a = 0
#     for i in alphabet:
#         if i not in string:
#             print("it's not a pangram")
#             a = 5
#             break
    
#     if a != 5:
#         print("it's a pangram")

# ab = "The quick brown fox jumps over the lazy dog."
# pangram(ab)








# Given a dictionary of students and their favourite colours:
# people={'Arham':'Blue','Lisa':'Yellow',''Vinod:'Purple','Jenny':'Pink'}
# 1. Find out how many students are in the list
# 2. Change Lisa’s favourite colour
# 3. Remove 'Jenny' and her favourite colour
# 4. Sort and print students and their favourite colours alphabetically by nam

# import sys
# people={'Arham':'Blue','Lisa':'Yellow','Vinod':'Purple','Jenny':'Pink'} 
# choice=1 
# while choice!=6:
#     print("-"*50)  
#     print("1.Find out how many students are in the list")    
#     print("2.Change Lisa’s favourite colour")    
#     print("3.Remove 'Jenny' and her favourite colour")   
#     print("4.Sort and print students and their favourite colours alphabetically by name")  
#     print("5.Display people")     
#     print("6.exit")    
#     print("-"*50)    
#     choice=int(input("Enter your choice="))
 
 
 
# # Create Tuple

number_tuple = (10, 20, 25.75)
print(number_tuple)
# create a tuple
sample_tuple = tuple((1, 2, 3, "Hello", [4, 8, 16]))
# iterate a tuple
for item in sample_tuple:
    print(item)   
del sample_tuple
print(sample_tuple)




# # Python program to demonstrate  opening a file 
# file1 = open('my_first_file.txt',"r")
# print(file1.read())
# file1.close()

# count how many lines
with open(r'my_first_file.txt', 'r') as fp:
    lines = len(fp.readlines())
    print('Total Number of lines:', lines)
    
    
    
    # number of words
number_of_words = 0
with open(r'SampleFile.txt','r') as file:
    # Reading the content of the file
    # using the read() function and storing
    # them in a new variable
    data = file.read()
    lines = data.split()
    number_of_words += len(lines)
# Printing total number of words
print(number_of_words)


