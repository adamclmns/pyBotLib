/*
 * Adam Clemons  
 * Arduino UNO R3 Sketch for MeArm and USB Host Shield using v2.0 of the library
 * October 19, 2015 - v 0.0.1
 * 
 */

#include <Servo.h>
#include <XBOXUSB.h>
// Satisfy the IDE, which needs to see the include statment in the ino too.
#ifdef dobogusinclude
#include <spi4teensy3.h>
#include <SPI.h>
#endif

//Declare the XBOX Controller
USB Usb;
XBOXUSB Xbox(&Usb);

//Declare 4 servos
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
  //Initial values  
  servo1Pos = 90;
  servo2Pos = 90;
  servo3Pos = 90;
  servo4Pos = 140;
  //Attach servos to pins
  servo1.attach(7);  //rotate
  servo2.attach(6);  //left
  servo3.attach(5);  //right
  servo4.attach(4);  //claw
  //writing initial values 
  servo1.write(servo1Pos);
  servo2.write(servo2Pos);
  servo3.write(servo3Pos);
  servo4.write(servo4Pos);
    
  Serial.begin(115200);
  //Getting the XBox Controller
  #if !defined(__MIPSEL__)
  while (!Serial); // Wait for serial port to connect - used on Leonardo, Teensy and other boards with built-in USB CDC serial connection
#endif
  if (Usb.Init() == -1) {
    Serial.print(F("\r\nOSC did not start"));
    while (1); //halt
  }
  Serial.print(F("\r\nXBOX USB Library Started"));
}//END SETUP

void claw(){
  if(servo4Pos < 180){
    servo4Pos = 180;
  }else if(servo4Pos == 180){
    servo4Pos = 140;
  }
  servo4.write(servo4Pos);
}

void rotateLeft(){
  if(servo1Pos < 180){
    servo1Pos++;
  }
  servo1.write(servo1Pos);
}

void rotateRight(){
  if(servo1Pos > 1){
    servo1Pos--;
  }
  servo1.write(servo1Pos);
}

void rightUp(){
  if(servo3Pos < 180){
    servo3Pos++;
  }
  servo3.write(servo3Pos);
}

void rightDown(){
  if(servo3Pos > 1){
    servo3Pos--;
  }
  servo3.write(servo3Pos);
}

void leftUp(){
   if(servo2Pos < 180){
    servo2Pos++;
  }
  servo2.write(servo2Pos);
}

void leftDown(){
  if(servo2Pos > 1){
    servo2Pos--;
  }
  servo2.write(servo2Pos);
}

void loop() {
  Usb.Task();
   if (Xbox.Xbox360Connected) {
      if (Xbox.getAnalogHat(LeftHatX) > 9000 || Xbox.getAnalogHat(LeftHatX) < -9000) {
        if(Xbox.getAnalogHat(LeftHatX) > 9000){
          rotateRight();
        } else if(Xbox.getAnalogHat(LeftHatX) < -9000){
          rotateLeft();
        }

        
      }
      if (Xbox.getAnalogHat(LeftHatY) > 9000 || Xbox.getAnalogHat(LeftHatY) < -9000) {
        if(Xbox.getAnalogHat(LeftHatY) > 9000){
          leftUp();
        }else if(Xbox.getAnalogHat(LeftHatY) < -9000){
          leftDown();
        }

      }
      if (Xbox.getAnalogHat(RightHatY) > 9000 || Xbox.getAnalogHat(RightHatY) < -9000) {
        if(Xbox.getAnalogHat(RightHatY) > 9000){
          rightUp();
        }else if(Xbox.getAnalogHat(RightHatY) < -9000){
          rightDown();
        }
      }
      
    if (Xbox.getButtonClick(A)){
      Serial.println(F("A"));
      claw();
    }



    if (Xbox.getButtonClick(XBOX)) {
      Xbox.setLedMode(ROTATING);
      Serial.println(F("Xbox"));
    }
   
  }
  delay(5);
 
}
