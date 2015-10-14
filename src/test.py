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
	me.lift(40)
	tick()
	me.lower(40)
	tick()
	me.rotateLeft(90)
	tick()
	me.rotateRight(90)
	tick()
	me.up(40)
	tick()
	me.lower(40)
	tick()
	me.claw()
	print("Test Complete")


test()