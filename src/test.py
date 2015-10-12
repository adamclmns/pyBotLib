#Test.py

import servos
import time
print("import successful")


def tick():
	time.sleep(0.5)
	
def test():
	host=linux()
	me=meArm(host)
	tick()
	me.claw()
	tick()
	me.fwd(20)
	tick()
	me.fwd(20)
	tick()
	me.back(20)
	tick()
	me.back(20)
	tick()
	me.rotateLeft(10)
	tick()
	me.rotateLeft(10)
	tick()
	me.rotateRight(10)
	tick()
	me.rotateRight(10)
	tick()
	me.up(10)
	tick()
	me.up(10)
	tick()
	me.down(10)
	tick()
	me.down(10)
	tick()
	me.claw()
	print("Test Complete")
