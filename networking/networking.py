from basic_functions import basic_functions
import socket
import requests
import urllib.request
import webbrowser

def get_private_ip():
    """returns the Private ip address of the current device, May get the private ip for a virtualbox/vmware apdater if it exists on the system"""
    
    device_hostname = socket.gethostname()
    ip_address = socket.gethostbyname(device_hostname)

    return ip_address

def get_device_hostname():
    """returns the current Device Hostname"""

    device_hostname = socket.gethostname()
    return device_hostname

def get_public_ip():
    """returns the Public Ip address of the current device."""

    ip = requests.get('https://api.ipify.org').content.decode('utf8')
    return ip

def download_file(url:str,file_name:str,overwrite_file=False):
    """downloads a file from a url
    Arguments:
        url: url of where to download the file from
        file_name: the name of the file after downloading
        overwrite_file: replace the file if a file of the same name exists
    
    """
    

    if overwrite_file == False:
        if basic_functions.file_exists(file_name):
            raise FileExistsError("a file name already exists with the filename you provided since the overwrite_file argument is False. An error has been raised, Change it to True to overwrite that file.")
        else:
            urllib.request.urlretrieve(url=url,filename=file_name)
    else:
        urllib.request.urlretrieve(url=url,filename=file_name)
        
def open_url(url:str):
    webbrowser.open(url=url)
