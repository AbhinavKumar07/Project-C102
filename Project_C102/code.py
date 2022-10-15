from distutils import extension
import os 
import shutil

source = 'C:/Users/Raj/Python_Whitehat/Project_C102/Project_C102_Source_Files'
destination = 'C:/Users/Raj/Python_Whitehat/Project_C102/Project_C102_Document_Files'

file_list = os.listdir(source)

for file in file_list:
    name , extension = os.path.splitext(file)
    if (extension == ''):
        continue
    if (extension == ['.txt' , '.doc' , '.docx' , '.pdf']):
        path1 = source + '/' + file
        path2 = destination + '/' + 'document_file'
        path3 = destination + '/' + 'document_file' + file

        if os.path.exists(path2):
            print("File is moving...")
            shutil.move(path1,path3)
        else: 
            os.makedirs(path2)
            print("File is moving...")
            shutil.move(path1,path3)