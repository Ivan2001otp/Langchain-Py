import os
import datetime


def list_files_in_current_dir():
    current_dir:str = os.getcwd()

    files_and_folders:list[str] = os.listdir(current_dir)
    print("The files and folders")

    for item in files_and_folders:
        temp : list[str] = item.split('.')
        
        if( len(temp)>1 ):
            print("File : "+item)
        else:
            print("Folder : "+item)

def present_working_directory():
    pwd:str = os.getcwd()
    print(f'Present working dir is {pwd}')

def create_new_file()->None:
    path : str  = input("Give path where u want to create file : ")
    pwd:str = os.getcwd()

    if path == "./":
        path = pwd
    
    now = datetime.datetime.now
    defaultFileName = "file -> "+str(now)
    
    print("Enter file name :")
    fileName = input()

    if(len(fileName)!=0):
        defaultFileName = fileName

    print("Path is "+path)
    print("File is "+defaultFileName)

    print("Enter the content u want to write")
    content:str = ""
    
    while True:
        spare:str = input()

        if spare == ":wq":
            break
        content = content + (spare)


    try:
        with open(defaultFileName,'w') as f:
            f.write(content)
    except IOError:
        print("Error: could not create file")


def rename_file(old_name:str) -> None:
    print("renaming file")
    new_file_name = input()

    try:
        os.rename(old_name, new_file_name)
        print(f"File renaming is successful")
    except FileNotFoundError:
        print(f"File not found")
    except PermissionError:
        print(f"Permission error")
    except Exception as e:
        print(f"An error occured")
        

def delete_file()->None:
    print("rename file")
    file_name:str = input()

    pwd:str = os.getcwd()
    pwd += "\\"
    pwd += file_name

    os.remove(pwd)


def copy_content(src:str, dest:str) -> None:
    print("copying file")

    # read the content from src and buffer it
    buffer:str = ""

    try:
        with open(src,'r') as f:
            buffer = f.read()

        with open(dest,'a') as f:
            f.write(buffer)
        
        print("Copied content successfully !")

    except IOError:
        print("io error")
    except Exception as e:
        print(e)


def switch_case(option:int, *args) -> None:
   if(option==1):
       present_working_directory()
       
   elif(option==2):
       list_files_in_current_dir()

   elif(option==3):
       create_new_file()

   elif(option==4):
       old_name:str = input()
       rename_file(old_name=old_name)

   elif(option==5):
       delete_file()

   elif(option==6):
       src = input()
       dest = input()
       copy_content(src,dest)

   else:
       print("None")
       
        
    

def driver():
   
    print("choose the above operation")
    optionStr : str = input()
    

    print(f"Your option is {optionStr}")

    if(optionStr.isnumeric()):
        switch_case(int(optionStr))

if __name__ == "__main__":
    print("3. Create new file")
    print("4. Rename the file")
    print("5. Delete the file")
    print("6. Copy the file")
    print("1. PWD")
    print("2. List current directory files & folders")
    
    driver()