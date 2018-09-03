#    Copyright (C) 2018  Chris Rush
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import time

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#GPIO pins connected to the motor controller board SN74
GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)

left = 2 #Left microswitch
right = 3 #Right microswitch

GPIO.setup(left,GPIO.IN)
GPIO.setup(right,GPIO.IN)

#The following functions are used to control the direction of the robot
def forwards():
        GPIO.output(17,1)
        GPIO.output(18,0)
        GPIO.output(22,1)
        GPIO.output(23,0)

def backwards():
        GPIO.output(17,0)
        GPIO.output(18,1)
        GPIO.output(22,0)
        GPIO.output(23,1)

def left():
        GPIO.output(17,0)
        GPIO.output(18,1)
        GPIO.output(22,1)
        GPIO.output(23,0)

def right():
        GPIO.output(17,1)
        GPIO.output(18,0)
        GPIO.output(22,0)
        GPIO.output(23,1)

def stop():
        GPIO.output(17,0)
        GPIO.output(18,0)
        GPIO.output(22,0)
        GPIO.output(23,0)

while True:
    if GPIO.read(left) == 0 and GPIO.read(right) == 0:
        forwards()
    elif GPIO.read(left) == 1:
        stop()
        time.sleep(1)
        backwards()
        time.sleep(2)
        stop()
        time.sleep(1)
        right()
        time.sleep(1)
        stop()
    elif GPIO.read(right) == 1:
        stop()
        time.sleep(1)
        backwards()
        time.sleep(2)
        stop()
        time.sleep(1)
        left()
        time.sleep(1)
        stop()
    elif GPIO.read(right) == 1:
        stop()
        time.sleep(1)
        backwards()
        time.sleep(2)
        stop()
        time.sleep(1)
        left()
        time.sleep(3)
        stop()
    elif GPIO.read(left) == 1 and GPIO.read(right) == 1:
        stop()
        time.sleep(1)
        left()
        time.sleep(4)
        stop()
