import os

cmd = "sudo screen /dev/serial/by-id/usb-1a86_USB_Serial-if00-port0 9600"

returned_value = os.system(cmd)  # returns the exit code in unix