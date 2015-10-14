import meArm
import pyttsx
import time

try:
    engine=pyttsx.init()
except:
    print("voice is unavailable")
def speak(phrase):
    try:
        engine.say(phrase)
        engine.runAndWait()
    except:
        print(phrase)
    

speak("initializing robot")

me = meArm.meArm(meArm.windows())
speak("Initialization complete")
speak("Testing")
me.rotateRight(80)

me.forward(35)


for i in range(5, 30,5):
    time.sleep(0.1)
    me.leftUp(5)
    i+=5

time.sleep(0.2)
me.claw()
time.sleep(0.2)
me.lift(25)
me.rotateLeft(160)
me.lower(16)
time.sleep(0.2)
me.leftDwn(10)
time.sleep(0.2)
me.leftDwn(10)
time.sleep(0.2)
me.leftDwn(10)
time.sleep(0.2)
me.lower(8)
me.claw()
me.backward(35)
me.rotateRight(80)

speak("test complete")

me.center()