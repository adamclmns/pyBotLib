#!/usr/bin/env python
# Module: Servo.py
#Created: 10/11/2015
#Author: Adam Clemons
#   github.com/adamclmns
#Version 0.1
#   based on servo.py by Brian D. Wendt (2008-04-02) - http://principialabs.com/ 
#
################################################
'''
Provides a serial connection abstraction layer
for use with Arduino "MultipleSerialServoControl" sketch
and Energia Sketch (for MSP430) "MultipleSerialServoControl"
'''
################################################

import serial
import time
import curses


class ServoController():
    
    def __init__(self, serialPort):
        self.serialPort = serialPort
        # Assign Arduino's serial port address
        #   Windows example
        #     usbport = 'COM6'
        #   Linux example
        #     usbport = '/dev/ttyACM0'
        #   MacOSX example
        #     usbport = '/dev/tty.usbserial-FTALLOK2'
        #usbport = 'COM6'
        # Set up serial baud rate
        self.servoHost = serial.Serial(serialPort, 9600, timeout=1)
        #set initial positions
        self.positions=[4,90,90,90,90]
        self.moveAll(90,90,90,90)
        
        

    def move(self,servo, angle):
        '''Moves the specified servo to the supplied angle.
        Arguments:
            servo
              the servo number to command, an integer from 1-4
            angle
              the desired servo angle, an integer from 0 to 180
        (e.g.) >>> servo.move(2, 90)
               ... # "move servo #2 to 90 degrees"'''

        if (0 <= angle <= 180):
            self.servoHost.write(chr(255))
            self.servoHost.write(chr(servo))
            self.servoHost.write(chr(angle))
            self.positions[servo]=angle
        else:
            print "Servo angle must be an integer between 0 and 180.\n"
   
    #Adding method to move all servos at once
    def moveAll(self, angle1, angle2, angle3, angle4):
        self.move(1, angle1)
        self.move(2, angle2)
        self.move(3, angle3)
        self.move(4, angle4)
        
    def sweepTest(self,servo):
        self.move(servo, 0)
        time.sleep(1)
        self.move(servo, 180)
        time.sleep(1)
        self.move(servo, 90)
	
	def sweepTestAll(self):
		self.sweepTest(1)
		self.sweepTest(2)
		self.sweepTest(3)
		self.clawOpen()
		self.clawClose()
		
	def center(self):
		self.moveAll(90,90,90,90)
		
	def clawOpen(self):
		self.move(4,120)
		
	def clawClose(self):
		self.move(4,179)		
	
class ServoTest():
	def __init__(self):
		print("Creating ServoController Instance...")
		self.host=None
		try:
			self.host=self.configure()
			print("Host Found")
		except:
			print("No Host Found")
		if host != None:
			host.moveAll(90,90,90,90)
		else:
			break
		
	def configureLinux(self):
		print("checking linux comPorts...")
		try:
			host = ServoController('/dev/ttyACM0')
			print("Found host on /dev/ttyACM0")
			return host
		except:
			try:
				host = ServoController('/dev/tty/ACM1')
				print("Found host on /dev/ttyACM1")
			except:
				host=None
				print("could not find serial hosts on linux com Ports")
		return host
	
	def configureWindows(self):
		print("checking Windows com ports...")
		try:
			host = ServoController('COM6')
			print("Found host on COM6")
		except:
			host=None
			print("could not find serial host on Windows Com ports")
		return host
		
	def congigure(self):
		try:
			self.configureLinux()
		except:
			try:
				self.configureWindows()
			except:
				print("Have you plugged it in?")
			
		return
	
	def test(self):
		self.host.move(1,0)
		time.sleep(0.5)
		self.host.move(1,180)
		time.sleep(0.5)
		self.host.move(1,90)
		time.sleep(0.5)
		self.host.move(2,0)
		time.sleep(0.5)
		self.host.move(2,180)
		time.sleep(0.5)
		self.host.move(2,90)
		time.sleep(0.5)
		self.host.move(3,0)
		time.sleep(0.5)
		self.host.move(3,180)
		time.sleep(0.5)
		self.host.move(3,90)
		time.sleep(0.5)
		self.host.move(4,0)
		time.sleep(0.5)
		self.host.move(4,180)
		time.sleep(0.5)
		self.host.move(4,90)
		time.sleep(0.5)
		
