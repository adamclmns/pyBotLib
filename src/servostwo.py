import serial


class ServoHost():
    
    def __init__(self, serialPort):
        self.servoHost = serial.Serial(serialPort, 9600, timeout=1)
        self.positions = [90,90,90,90]

    def setPositions(self, positionSet):
        outputString = ""
        for angle in positionSet:
            outputString += str(angle)
            outputString+=","
        outputString += "255"
        self.servoHost.write(outputString)
            