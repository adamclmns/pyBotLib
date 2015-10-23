import serial


class ServoHost():
    
    def __init__(self, serialPort):
        self.servoHost = serial.Serial(serialPort, 9600, timeout=1)
        self.positions = [90,90,90,90]

    def moveFor(self, positionSet):
        for angle in positionSet:
            

    def moveOther(self, positionSet):
        self.servoHost.write((str(self.positions[0])+","+str(self.positions[1])+","+str(self.positions[2])+","+str(self.positions[3])+"x"))
        