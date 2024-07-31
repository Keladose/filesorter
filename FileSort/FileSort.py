import os
import shutil
import pathlib

def sort_files(file_type, file_type_loc):
    file_type = file_type.lower()
    destination_directory = os.path.join(file_type_loc, file_type)
    os.makedirs(destination_directory, exist_ok=True)

    for filename in os.listdir(downloads_directory):

        if filename.lower().endswith(file_type):
            src_file = os.path.join(downloads_directory, filename)

            dest_file = os.path.join(destination_directory, filename)

            shutil.move(src_file, dest_file)


if True:
    check_dir = input("If your download directory is different to default, please enter your download directory: ("
                      "else type continue)")
    if check_dir != "continue":
        downloads_directory = check_dir
    else:
        downloads_directory = pathlib.Path.home() / "Downloads"
    dirs_location = input("Please enter directory of where you want the folders to be saved: ")


while True:
    filetype = input("What filetype do you want to move (pdf, docx, exe, etc..)? (type end to cancel) ")
    if filetype == "end":
        break

    sort_files(filetype, dirs_location)


