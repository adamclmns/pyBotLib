/*
 * Adam Clemons  
 * Arduino UNO R3 Sketch for PyBotLib
 * github.com/adamclmns/pyBotLib
 * October 14, 2015 - v 0.0.1
 * 
 */

#include <Servo.h>

//Arduino is connected to 4 servos
Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4; 

//Track servo positions as 0 < int < 180
int servo1Pos;
int servo2Pos;
int servo3Pos;
int servo4Pos;

//END Declarations

void setup() {  
  //Attach servos to pins
  servo1.attach(7);  
  servo2.attach(6);  
  servo3.attach(5);  
  servo4.attach(4);  

  //THis is lowest value for the MeArm robots 4th servo without damaging it. 
  servo4.write(140);
  Serial.begin(9600);
}

void writeServoPos(){
      servo1.write(servo1Pos);
      servo2.write(servo2Pos);
      servo3.write(servo3Pos);
      //Preventing servo 4 from opening too far. Can cause damage. Should be changed for your implementation.
      if (servo4Pos < 140){
        servo4Pos = 140;
      }
      servo4.write(servo4Pos);
}

void loop() {

  //Read data from serial - python syntax is serial.write('254,90,90,90,90,255')
  while (Serial.available() > 0) {
    
      servo1Pos = Serial.parseInt();
      servo2Pos = Serial.parseInt();
      servo3Pos= Serial.parseInt();
      servo4Pos = Serial.parseInt();
    
    if (Serial.parseInt() == 255) { //Write Command == 255
       writeServoPos();
    }
   
  }
}
