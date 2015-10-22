import serial
import time

class ServoHost():
    
    def __init__(self, serialPort):
        self.servoHost = serial.Serial(serialPort, 9600, timeout=1)
        self.positions = [90,90,90,90]

    def moveFor(self, positionSet):
        for angle in positionSet:
            if (0 <= angle <= 180):
                #self.servoHost.write(chr(255))
                #self.servoHost.write(chr(servo))
                self.servoHost.write(chr(angle))
                #self.positions[servo]=angle
            else:
                print("Servo angle must be an integer between 0 and 180.\n")
                self.servoHost.write(chr('x'))  

    def moveOther(self, positionSet):
        self.servoHost.write((str(self.positions[0])+","+str(self.positions[1])+","+str(self.positions[2])+","+str(self.positions[3])+"x"))
        