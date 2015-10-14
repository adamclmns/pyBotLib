#Test.py

import servos
import time
import meArm
print("import successful")


def tick():
	time.sleep(0.1)
	
def test():
	host=meArm.windows()
	me=meArm.meArm(host)
	tick()
	me.claw()
	tick()
	me.forward(20)
	tick()
	me.backward(20)
	tick()
	me.rotateLeft(10)
	tick()
	me.rotateRight(10)
	tick()
	me.up(10)
	tick()
	me.down(10)
	tick()
	me.claw()
	print("Test Complete")


test()