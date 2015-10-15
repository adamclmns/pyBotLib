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
  servo1.attach(11);  
  servo2.attach(10);  
  servo3.attach(9);  
  servo4.attach(8);  

  servo4.write(140);
  Serial.begin(9600);
}

void loop() {

  //Read data from serial - python syntax is serial.write('90,90,90,90e')
  while (Serial.available() > 0) {
    servo1Pos = Serial.parseInt();
    servo2Pos = Serial.parseInt();
    servo3Pos= Serial.parseInt();
    servo4Pos = Serial.parseInt();

    if (Serial.read() == 'x') { //Ending character, can't be parsed to Int
      servo1.write(servo1Pos);
      servo2.write(servo2Pos);
      servo3.write(servo3Pos);
      if (servo4Pos < 140){
        servo4Pos = 140;
      }
      servo4.write(servo4Pos);
    }
  }
}
