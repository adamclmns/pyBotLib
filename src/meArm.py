import servos
import time
print("import successful")

def linux():
	return servos.ServoController('/dev/ttyACM0')

def linux2():
	return servos.ServoController('/dev/ttyACM1')
	
def windows():
	return servos.ServoController('COM6')
	

class meArm():
	def __init__(self,host):
		self.host = host
		self.clawOpen=True
		self.rot = [1,90]
		self.hpos = [2,90]
		self.vpos = [3,90]

	def set(self, arg):
		self.host.move(arg[0],arg[1])
		time.sleep(0.125)
	
	def rotateLeft(self, delta):
		self.rot[1]+=delta;
		self.set(self.rot)
		
	def rotateRight(self, delta):
		self.rot[1]-=delta;
		self.set(self.rot)
		
	def out2(self,delta):
		self.hpos[1]+=delta
		self.set(self.hpos)
	
	def in2(self, delta):
		self.hpos[1]-=delta
		self.set(self.hpos)
	
	def out1(self,delta):
		self.vpos[1]+=delta
		self.set(self.vpos)
		time.sleep(.125)
	
	def in1(self, delta):
		self.vpos[1]-=delta
		self.set(self.vpos)
	
	def snap(self):
		self.claw()
		time.sleep(.15)
		self.claw()
		time.sleep(.1)
		self.claw()
		time.sleep(.1)
		self.claw()
	
	def forward(self, delta):
	    steps=delta / 4
	    for i in range(0,steps):
	        self.out1(4)
	        time.sleep(0.01)
	        self.out2(4)
	
	def backward(self, delta):
	    steps = delta / 4
	    for i in range(0,steps):
	        self.in1(4)
	        time.sleep(0.01)
	        self.in2(4)
	
	def grab(self):
		if self.clawOpen != True:
		    self.claw()
		self.claw()
	
	def lift(self,delta):
	    steps = delta /4
	    for i in range(0,steps):
	        self.in2(4)
	        time.sleep(0.01)
	        self.out1(4)
	        time.sleep(0.01)
	
	def lower(self, delta):
	    steps = delta /4
	    for i in range(0,steps):
	        self.out2(4)
	        time.sleep(0.01)
	        self.in1(4)
	        time.sleep(0.01)
	        
	def grotate(self, delta):
	    steps = delta/4
	    for i in range(0,steps):
	        if delta > 0:
	            self.rotateRight(4)
	            time.sleep(0.01)
	        elif delta < 0:
	            self.rotateLeft(4)
	            time.sleep(0.01)
            
	def Status(self):
	    print("Rotation: "+str(self.rot[1]))
	    print("servo1: "+str(self.hpos[1]))
	    print("servo2: "+str(self.vpos[1]))
	    print("Claw Open: "+str(self.clawOpen))
	
	def claw(self):
		if self.clawOpen:
			self.host.move(4,178)
			self.clawOpen=False
		else:
			self.host.move(4,145)
			self.clawOpen =True
	
	def center(self):
	    self.host.moveAll(90,90,90,90)	
