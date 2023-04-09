import os
import ctypes as ct


def remove_directory(directory_path):
    directory_path.replace("\ "[0], "/")
    status_code = "Alright"

    try:
        os.rmdir(directory_path)
    except Exception as e:
        status_code = "Something went wrong, cannot remove directory"
    finally:
        return status_code


def remove_file(file_path):
    status_code = "Alright"

    try:
        os.remove(file_path)
    except Exception as e:
        status_code = "Something went wrong, cannot remove file"
    finally:
        return status_code


def remove_path(path_to_remove):
    if os.path.isdir(path_to_remove):
        status_code = remove_directory(path_to_remove)
    elif os.path.isfile(path_to_remove):
        status_code = remove_file(path_to_remove)
    else:
        status_code = "The Path does not lead to file or directory"

    return status_code


def remove_something(label, path):
    label_content = remove_path(path)
    if label_content != "Alright":
        label.configure(text=label_content, fg="red")
    else:
        label.configure(text=label_content, fg="lightgreen")
