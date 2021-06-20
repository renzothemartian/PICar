import serial
#init serial port and bound
# bound rate on two ports must be the same
ser = serial.Serial('/dev/serial/by-id/usb-1a86_USB_Serial-if00-port0', 9600)
print(ser.portstr)

#send data via serial port
serialcmd=("90")
ser.write(serialcmd.encode())
ser.close()