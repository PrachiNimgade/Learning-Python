# # Python program to demonstrate  opening a file

# file1 = open('E:\LearningPython\FileHandling.py\FirstFile.txt',"r")
# print(file1.read())
# file1.close()

# # Python program to demonstrate  opening a file with some exception handling
# try:
#     file1 = open('E:\LearningPython\FileHandling.py\FirstFile.txt',"r")
# except FileNotFoundError:
#     print("File Not present , I am goind ahead and creating a file for you with some default text !!! ")    
#     file1 = open('my_first_file.txt',"w+")
#     #file1.write("Default creation was done in exception block")
#     file1.writelines(['first_line\n','second_line\n','third_line'])
    
#     print("I am location ", file1.tell())
#     print("I am resetting it at 0 " , file1.seek(0))
#     print("I am location after resetting ", file1.tell())
#     print("I am reading just after writing-->", file1.read())
#     file1.close()
    
        
    # program to read from one file and write to the same file 
input_file = open('E:\LearningPython\FileHandling.py\FirstFile.txt')
temp_data = input_file.readlines()
input_file.close()

output_file= open('E:\LearningPython\FileHandling.py\FirstFile.txt','w+')
for input_line in temp_data:
    output_file.write('HPCSA'+input_line)

output_file.seek(0)    
print(output_file.read())
    
    
    
    
#     # program to read from one file and write to the same file 
# input_file = open('my_first_file.txt')
# temp_data = input_file.readlines()
# input_file.close()

# output_file= open('my_first_file.txt','w+')
# for input_line in temp_data:
#     output_file.write('HPCSA'+input_line)

# output_file.seek(0)    
# print(output_file.read())

# program where we are using os module along with file handling
import os 

current_file_abs_path = __file__ # gives absolute path of the file 
current_directory = os.getcwd() # gives current working directory path 
target_folder_path = os.path.join(current_directory,'output') # creates path from strings

if 'output' not in os.listdir(current_directory): # gets all files folders in list
     os.mkdir(target_folder_path) # creates a folder

target_path = os.path.join(target_folder_path,'my_first_file_output.txt')

# output_file= open('C:\\Users\\acer\\Desktop\\HPCSA_python\\output\\my_first_file_output.txt','w+')
output_file= open(target_path,'w+') # we use the variable instead of harcoded value
for input_line in open('my_first_file.txt'):
    output_file.write('HPCSA'+input_line)

output_file.seek(0)    
print(output_file.read())    
