import os
import shutil

pwd1 = os.getcwd()

def moveFiles(srcPath:str, destPath:str)->bool:
    print("Src Path ->"+srcPath)
    print("Dest Path ->"+destPath)
    
    try:
        shutil.move(srcPath,destPath)
        return True
    except FileNotFoundError:
        print(f"File not found.")
    except PermissionError:
        print(f"Permission not found")
    except Exception as e:
        print(e)

    return False

def util(ext:str,fileName: str):
    print("Extension is "+ext)
    if(ext == "txt"):
        src = pwd1
        src += "\\"
        src += fileName

        dest = pwd1
        dest += "\\Text\\"

        result:bool = moveFiles(srcPath=src, destPath=dest)

    elif(ext == 'c'):
        src = pwd1
        src += "\\"
        src += fileName

        dest = pwd1
        dest += "\\Cfile\\"

        result:bool = moveFiles(srcPath=src, destPath=dest)

def listAllFiles():
    pwd:str = os.getcwd()

    files:list[str] = os.listdir(pwd)

    print(files)

    Cfiles : list[str]=[]
    TextFiles : list[str] = []

    for file in files:

        items = file.split('.')
        print(f"split items->{items}")

        if(len(items)>1):
            extension:str = items[1]

            if(extension=='c'):
                Cfiles.append(file)
            elif(extension=="txt"):
                TextFiles.append(file)

            util(extension, file)

def main()->None:
    print("driver executed")
    listAllFiles()

if __name__ == "__main__":
    main()