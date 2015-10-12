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
		
	def fwd(self,delta):
		self.hpos[1]+=delta
		self.set(self.hpos)
	
	def back(self, delta):
		self.hpos[1]-=delta
		self.set(self.hpos)
	
	def up(self,delta):
		self.vpos[1]+=delta
		self.set(self.vpos)
		
	def down(self, delta):
		self.vpos[1]-=delta
		self.set(self.vpos)
	
	def snap(self):
		if self.clawOpen != True:
			self.claw()
		self.up(10)
		self.fwd(10)
		self.claw()
		self.down(10)
		self.back(10)
		self.claw()
		
	def grab(self):
		if self.clawOpen != True:
			self.claw()
		self.down(15)
		self.fwd(15)
		self.claw()
		self.up(30)
		self.back(20)
		
	def floor(self):
		print("this will lower the arm all the way to the ground")
		
	def claw(self):
		if self.clawOpen:
			self.host.move(4,178)
			self.clawOpen=False
		else:
			self.host.move(4,145)
			self.clawOpen =True
		
