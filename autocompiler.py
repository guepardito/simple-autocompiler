import os
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='compiles all .c / .h files with gcc')
    parser.add_argument('--export', choices=["object", "exe"], help='Select from compile in .o or .exe file')
    
    args = parser.parse_args()
    return(vars(args).get("export"))

def parse_list(list):
    string = ""
    for i in list:
        string += i
        string += " "
    return string

def getFiles(path='.'):
    files = os.listdir(path)
    file_list = []
    exception_string = ""

    for f in files:
        new_path = path + '/' + f

        try:
            file_name, file_extension = f.split(".")
            if file_extension == 'c' or file_extension == 'h':
                file_list.append(new_path)
        except:
            exception_string += getFiles(new_path)

    return(parse_list(file_list) + exception_string)

def main():
    if parse_args() == 'exe':
        os.system("gcc -o main.exe " + getFiles())
    else:
        os.system("gcc -c " + getFiles())


if __name__ == "__main__":
    main()