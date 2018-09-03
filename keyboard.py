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

from sys import exit
import time
import pygame
import RPi.GPIO as GPIO

pygame.init()
screen = pygame.display.set_mode((480,480))

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)

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
        pygame.display.flip()
        keystate = pygame.key.get_pressed()

        if keystate[pygame.K_RIGHT]:
                print "right"
                right()

        elif keystate[pygame.K_LEFT]:
                print "left"
                left()

        elif keystate[pygame.K_DOWN]:
                print "back"
                backwards()

        elif keystate[pygame.K_UP]:
                print "up"
                forwards()
        else:
                stop()

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        exit(0)

        time.sleep(0.01)
