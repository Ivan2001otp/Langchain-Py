import os
import shutil
from datetime import datetime
import time
import schedule


def getCwd()->str:
    return os.getcwd()

def listAllDir()->list[str]:
    cwd = getCwd()

    files:list[str] = os.listdir(cwd)
    return files

def create_and_writefile(srcPath,destPath,file) -> None :
   
    try:
        destPath += file
        print("creating file ")
        buffer:str=""

        with open(srcPath,'r') as f:
            buffer = f.read()
        
        with open(destPath,'w') as f:
            f.write(buffer)
      
    except Exception as e:
        print(e)


def append_to_file(srcPath,destPath,file)->None:
    buffer:str = ""
    write_permission:bool = False

    try:
        with open(srcPath,'r') as f:
           buffer = f.read()
           write_permission = True
    except Exception as e:

        print(e)

    if(write_permission==False):
        return

    try:
        destPath += file
        with open(destPath,'a+') as f:
            f.write(buffer)
    except Exception as e:
        print(e)


def job() -> None:

    files = listAllDir()

    srcPath = getCwd()
    destPath = srcPath + "\\Backup\\'"

    print(f"srcPath : {srcPath}")
    print(f"destPath : {destPath}")

    for file in files:
        print(f'file {file} is backing up..')
        filePath = srcPath + "\\" 

        file_len = file.split('.')
        
        if ( len(file_len) > 1) :
            filePath += file
        else :
            continue

        print(f"File Path is {filePath}")

        if(os.path.exists(destPath)):
            create_and_writefile(srcPath=srcPath,destPath= destPath,file=file)
        else:
            append_to_file(srcPath=filePath, destPath=destPath,file=file)



def schedule_task(interval_in_seconds:int) -> None :
    schedule.every(interval_in_seconds).seconds.do(job)


def main() -> None :
    specified_time : int = 15 * 60 

    schedule_task(specified_time)

    while True:
        schedule.run_pending()


if __name__ == "__main__":
    main()