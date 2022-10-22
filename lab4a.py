from datetime import datetime
import os
import io

CURRENT_DIR = os.getcwd() + '/assets'
if not os.path.exists(CURRENT_DIR):
    os.makedirs(CURRENT_DIR)
os.umask(0)

def q1():
    f_1 = open(CURRENT_DIR + '/sales.txt', 'a+')
    f_2 = open(CURRENT_DIR + '/'+ datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p") + '.txt', 'a+')
    f_3 = open(CURRENT_DIR + '/openWPerm.txt', 'a+', os.open(CURRENT_DIR + '/openWPerm.txt', (
        os.O_WRONLY
        | os.O_CREAT
        | os.O_TRUNC
    ), 0o777))
    
def q2():
    f = open(CURRENT_DIR + '/sales.txt', 'a+')
    f.writelines(['write content\n', 'write to text file\n'])
    f.close()
    f = open(CURRENT_DIR + '/sales.txt', 'a+')
    f.write('write to an existing file')
    f.writelines(['write first list\n', 'write second list\n', 'write third list\n'])
    f.close()
def q3():
    f = open(CURRENT_DIR + '/sales.txt', 'a+')
    print(f.seek(0))
    f.write('write to the beginning of file')
    print(f.seek(f.tell() - 3, os.SEEK_SET))
    f.write('write backward 3 from the current position')
    print(f.seek(io.SEEK_CUR))
    f.write('write to the end of file')
    print(f.seek(io.SEEK_END))
    print(f.tell())
def q4():
    # Rename a file after checking whether it exists
    old_name = str(input('File path need to rename: '))
    new_name = str(input('New file name: '))

    if os.path.isfile(new_name):
        print("The file already exists")
    else:
        path, filename = os.path.split(old_name)
        os.rename(old_name, path + new_name)
        
    # Rename Multiple Files in Python   
    folder = str(input('Enter folder path: '))
    count = 1
    for file_name in os.listdir(folder):
        source = folder + file_name

        destination = folder + "renamed_" + str(count) + ".txt"

        os.rename(source, destination)
        count += 1
    print('All Files Renamed!')

    print('New Names are: ')
    res = os.listdir(folder)
    print(res)

    # Renaming only a list of files in a folder
    num_files = int(input('Enter number of files you want to rename: '))
    files_to_rename = []
    for x in range(0, num_files - 1):
        files_to_rename.append(str(input('Enter filename number %i: '%(x+1))))
    folder = str(input('Enter folder path: '))

    for file in os.listdir(folder):
        if file in files_to_rename:
            old_name = os.path.join(folder, file)
             
            only_name = os.path.splitext(file)[0]

            new_base = only_name + '_new' + os.path.splitext(file)[1]
            new_name = os.path.join(folder, new_base)

            os.rename(old_name, new_name)

    res = os.listdir(folder)
    print(res)
    
    # Renaming files with a timestamp
    current_timestamp = datetime.today().strftime('%d-%b-%Y')
    old_name = str(input('File path need to rename: '))
    
    path, filename = os.path.split(old_name)
    new_name = path + current_timestamp + os.path.splitext(filename)[1]
    
    os.rename(old_name, new_name)
    
    # Renaming the Extension of the Files
    folder = str(input('Enter folder path: '))
    file_new_extension = str(input('Enter file extension you want to replace: '))
    file_old_extension = str(input('Enter file extension you want to replace by new extension: '))
    
    print('Before rename')
    files = os.listdir(folder)
    print(files)

    for file_name in files:
        if os.path.splitext(file)[1] == file_old_extension:
            old_name = os.path.join(folder, file_name)

            # Changing the extension from txt to pdf
            new_name = old_name.replace(file_old_extension, file_new_extension)
            os.rename(old_name, new_name)

    print('After rename')
    print(os.listdir(folder))
    
    # Renaming and then moving a file to a new location
    current_file = str(input('Enter current file path: '))
    new_folder = str(input('Enter new folder path: '))
    
    path, filename = os.path.split(current_file)
    new_name = new_folder + filename

    os.rename(current_file, new_name)