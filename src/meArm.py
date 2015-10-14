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
		#not used yet... 
		self.positions=[[0,0],[1,90],[2,90],[3,90]]
		#Leaving old position tracking for backwards compatiblity while i make the change
		self.MS = [1,90]
		self.RS = [2,90]
		self.LS = [3,90]

	def set(self, arg):
		self.host.move(arg[0],arg[1])
		self.positions[arg[0]]=arg
		time.sleep(0.125)
	
	def rotateLeft(self, delta):
		steps=delta / 4
		for i in range(0,steps):
			self.MS[1]+=4
			self.set(self.MS)
		
	def rotateRight(self, delta):
		steps=delta / 4
		for i in range(0,steps):
			self.MS[1]-=4;
			self.set(self.MS)
	
	#mapping the arms.
	def rightBack(self, delta):
		self.RS[1]-=delta
		self.set(self.RS)
	
	def rightFwd(self,delta):
		self.RS[1]+=delta
		self.set(self.RS)
		
	def leftUp(self,delta):
		self.LS[1]+=delta
		self.set(self.LS)
		
	def leftDwn(self,delta):
		self.LS[1]-=delta
		self.set(self.LS)
		
#/////////////////////////////////////////////////////////////////
#
# remove these when replaced. Keeping for backwards compatibility
#
#/////////////////////////////////////////////////////////////////
# 	
#	def rightFwd(self,delta): # right fwd
# 		self.RS[1]+=delta
# 		self.set(self.RS)
# 	
# 	def rightBack(self, delta): # right  back
# 		self.RS[1]-=delta
# 		self.set(self.RS)
# 	
# 	def leftUp(self,delta): # left up
# 		self.LS[1]+=delta
# 		self.set(self.LS)
# 		time.sleep(.125)
# 	
# 	def leftDwn(self, delta): # left down
# 		self.LS[1]-=delta
# 		self.set(self.LS)
# 	
#//////////////////////////////////////////////////////////
	
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
	        self.leftDwn(4)
	        time.sleep(0.01)
	        self.rightFwd(4)
	
	def backward(self, delta):
	    steps = delta / 4
	    for i in range(0,steps):
	        self.leftUp(4)
	        time.sleep(0.01)
	        self.rightBack(4)
	
	def grab(self):
		if self.clawOpen != True:
		    self.claw()
		self.claw()
	
	def lift(self,delta):
	    steps = delta /4
	    for i in range(0,steps):
	        self.rightBack(4)
	        time.sleep(0.01)
	        self.leftUp(4)
	        time.sleep(0.01)
	
	def lower(self, delta):
	    steps = delta /4
	    for i in range(0,steps):
	        self.rightFwd(4)
	        time.sleep(0.01)
	        self.leftUp(4)
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
	    print("Rotation: "+str(self.MS[1]))
	    print("servo1: "+str(self.RS[1]))
	    print("servo2: "+str(self.LS[1]))
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
