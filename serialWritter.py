import serial


def sendCommand(ser, command):
    print("Writing "+str(command))
    ser.write(command)     # write a string

    # with serial.Serial('/dev/cu.SLAB_USBtoUART', 115200, timeout=1) as ser:
    print("Reading response")
    line = ser.readline()   # read a '\n' terminated line
    print(line)
    return line



def open_serial_connection():
    ser = serial.Serial('/dev/cu.SLAB_USBtoUART', 115200, timeout=1)  # open serial port
    print("Connected to device")
    print(ser.name)         # check which port was really use
    a = sendCommand(ser, b'0,0,0')
    print(a)
    return ser


def close_serial_connection(ser):
    ser.close()             # close port
