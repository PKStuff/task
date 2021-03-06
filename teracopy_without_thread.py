import os
import argparse
import shutil
import time

count_files = 0
def src_to_dest(src_folder, dest_folder):
    global count_files
    src_files = os.listdir(src_folder)
    all_files = []
    nested_folders = {}
    for files in src_files:
        full_file_name = os.path.join(src_folder, files)
        if os.path.isfile(full_file_name):
            all_files.append(full_file_name)
            count_files+=1
            #print(src_folder+"------->"+full_file_name)
        elif os.path.isdir(full_file_name):
            new_destination = os.path.join(dest_folder,files)
            if not os.path.exists(new_destination):
                os.mkdir(new_destination, 755)
            nested_folders[full_file_name] = new_destination
        else:
            pass
    std_copy(src_folder,dest_folder,all_files)
    for key, value in nested_folders.items():
        src_to_dest(key, value)

def std_copy(src_folder,dest_folder,files_to_copy):
    for files in files_to_copy:
        file_name = os.path.join(src_folder, files)
        os.chdir(dest_folder)
        if not os.path.exists(file_name.split("\\")[-1]):
            shutil.copy(file_name,dest_folder)

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Teracopy program.")
    parser.add_argument("teracopy", nargs = 2, metavar = 'path', type=str, help="1.Source files and 2.Destination folder.")
    args = parser.parse_args()

    src_folder = args.teracopy[0]
    dest_folder = args.teracopy[1]

    start_time = time.time()
    src_to_dest(src_folder,dest_folder)
    end_time = time.time()

    print("Time required to copy {} files are:{}".format(count_files,(end_time-start_time)))
    
    
   """
   OUTPUT:
   
   Time required to copy 207 files are:1.3161916732788086
   """
