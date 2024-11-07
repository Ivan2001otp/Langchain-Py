import os
import shutil
import re

# renaming files in batch manner

pwd:str = os.getcwd()

def list_all_files_of_currdir()->list[str]:
    try:
        list_of_files = os.listdir(pwd)
        return list_of_files 
    except FileNotFoundError:
        print("Directory not found.")
        return []
    
def rename_files(directory, old_filenames, new_filenames)->None :
    for old_name,new_name in zip(old_filenames, new_filenames):
        old_path  = os.path.join(directory,old_name)
        new_path = os.path.join(directory, new_name)
        os.rename(old_path, new_path)
        print(f"Renamed {old_name} -> {new_name}")

def add_prefix(files,prefix):
    return [prefix + f for f in files]

def add_suffix(files,suffix,incr=False):
    if(incr):
        for f in files:
            f = f.split('.')[0] + str(suffix) + '.' + f.split('.')[1]
            suffix += 1
        return files
    
    return [f.split('.')[0] + suffix + '.' + f.split('.')[1] for f in files]

def rename_jpg_batch(prefix:str,suffix:any) -> None:
    print("renaming jpg batch")

    all_files = list_all_files_of_currdir()
    jpg_files = list(filter(lambda file: file.endswith('.jpg'),all_files))

    modified_files:list[str]=[]

    print(jpg_files)

    if(len(prefix)!=0):
        modified_files = add_prefix(jpg_files, prefix= prefix)
        
    else:
        if isinstance(suffix, int):
            modified_files = add_suffix(jpg_files, suffix=suffix,incr=True)

        elif isinstance(suffix, str):
            modified_files = add_suffix(jpg_files, suffix= suffix)
    
    print(modified_files)


    choice:str = input("Are you sure you want to proceed renaming batch (y/n) ? ")
    if(choice == 'y'):

        print("renamed")
        rename_files(pwd, jpg_files, modified_files)


    elif (choice == 'n'):
        print("no renaming")

    # by default i am setting suffix as numbering
    

def rename_png_batch() -> None:
    print("renaming png batch")

def rename_pdf_batch() -> None:
    print("renaming png batch")

def rename_txt_batch() -> None:
    print("renaming png batch")


def main():
    print("main driver")
    print("what file type u want to rename ?")
    print("1.jpg")
    print("2.png")
    print("3.pdf")
    print("4.txt")

    ext:str = input()

    match(ext):
        case '1':
            print("jpg format")
            prefix:str = input("Enter the prefix : ")
            suffix:str = input("Enter the suffix : ")
            rename_jpg_batch(prefix=prefix,suffix=suffix)
        
        case '2':
            print("png format")
            rename_png_batch()


        case '3':
            print("pdf format")
            rename_pdf_batch()

        
        case '4':
            print("text format")
            rename_txt_batch()

        case _:
            print("default choice")
            

if __name__ == "__main__":
    main()