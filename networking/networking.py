import socket

def get_private_ip():
    """returns the Private ip address of the current device, May get the private ip for a virtualbox/vmware apdater if it exists on the system"""
    
    device_hostname = socket.gethostname()
    ip_address = socket.gethostbyname(device_hostname)

    return ip_address

def get_device_hostname():
    """returns the current Device Hostname"""

    device_hostname = socket.gethostname()

    return device_hostname

