// MeArmMeCon-A041.ino
//Use With MeCon.exe Ver0.4 Windows Software for MeArm Motion Control
// Go to WWW.MICROBOTLABS.COM for ubdates and more info


#include <Servo.h>

//MeArm HAS 4 SERVOS
Servo xServo;  // create servo object, arm base servo - left right motion
Servo yServo;  // create servo object, left side servo - forward backwards motion
Servo zServo;  // create servo object, right side servo - forward backwards motion
Servo clawServo;  // create servo object, end of arm srevo - open,close the claw hand

//servo positions values, expects 1-180 deg.
int xPos;
int yPos;
int zPos;
int clawPos;

//Input Buffer for Python Client - Adam Clemons
int inputBuffer[5];
int endbyte;
int i;
//*************** INIT AT STARTUP *******************************************************************

void setup() {        // the setup function runs once when you press reset or power the board

  // assign servo to pin numbers
  xServo.attach(11);  // attaches the servo on pin 11 to the servo object
  yServo.attach(10);  // attaches the servo on pin 10 to the servo object
  zServo.attach(9);  // attaches the servo on pin 9 to the servo object
  clawServo.attach(8);  // attaches the servo on pin 6 to the servo object

  // initialize serial port
  Serial.begin(9600);

  // Debug only send serial message to host com port terminal window in Arduino IDE
  Serial.print("*** MeCon com Test V04 ***");   // send program name, uncomment for debug connection test



}

// ******************************************************************************************************
// ********************************** MAIN PROGRAM LOOP START *******************************************
// ******************************************************************************************************

void loop() {

  //Get servo position values from serial port
  //serial in packet patern = xVal,yVal,zVal,clawVal + end of packet char 'x'
  if(Serial.available() >4){
    //if(Serial.read()==255){
      for(i=0; i<4; i++){
        inputBuffer[i]=Serial.read();
      }
      xPos=inputBuffer[0];
      yPos=inputBuffer[1];
      zPos=inputBuffer[2];
      clawPos=inputBuffer[3];
    //}

      if(Serial.read()=='x'){
      
      xServo.write(180 - xPos);//CLOCKWISE- Example of how to Reverse rotation of servo motor
      yServo.write(yPos);//COUNTERCLOCKWISE rotation
      zServo.write(zPos);//COUNTERCLOCKWISE rotation
      clawServo.write(clawPos);//COUNTERCLOCKWISE rotation
      }
  }

}
