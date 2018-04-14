import serial, sys, threading

def process_shape(message):
    #decode message
    #draw shape
    print(message)

def read_port(ser):
    while True:
        message = ser.readline().decode()
        process(message)

try:
    ser = serial.Serial('dev/ttyUSB0')
    thread = threading.Thread(target=read_from_port, args=(ser,))
    thread.start()
    print(ser.name)
except:
    print(sys.exc_info())

