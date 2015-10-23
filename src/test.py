#Test.py
# Adam Clemons 10-21-2015 - Using to test pyBot lib. This file is always changing,
# and should not be used in any implementation


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