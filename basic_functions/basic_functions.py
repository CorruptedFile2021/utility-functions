import platform
import pathlib

def get_os_name():
    os_name = platform.system() # Gets Operating System Name, for example: Windows, Linux
    version = platform.release() # Gets Release Version of Operating System, for example: will return 10 if it is a Windows 10 machine

    return os_name, version # return the info

def file_exists(path:str):
    """checks whether the following file exists. Use directory_exists to check if a directory exists"""

    file = pathlib.Path(path)
    if file.exists():
        return True
    else:
        return False


def directory_exists(path:str):
    """checks whether the following directory exists. Use file_exists to check if a file exists"""

    file = pathlib.Path(path)
    if file.is_dir():
        return True
    else:
        return False
    