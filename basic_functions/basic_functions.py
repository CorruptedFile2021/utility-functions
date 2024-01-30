import platform

def get_os_name():
    os_name = platform.system() # Gets Operating System Name, for example: Windows, Linux
    version = platform.release() # Gets Release Version of Operating System, for example: will return 10 if it is a Windows 10 machine

    return os_name, version # return the info

