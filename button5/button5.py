import RPi.GPIO as GPIO
import random


index=0
sequence=random.shuffle(["25", "24", "16"])


def button_25_pressed(channel):
  print("channel: " + channel)
  print("button 25 pressed")


def button_24_pressed(channel):
  print("button 24 pressed")


def button_16_pressed(channel):
  print("button 16 pressed")


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

GPIO.add_event_detect(25, GPIO.RISING, callback=button_25_pressed, bouncetime=500)
GPIO.add_event_detect(24, GPIO.RISING, callback=button_24_pressed, bouncetime=500)
GPIO.add_event_detect(16, GPIO.RISING, callback=button_16_pressed, bouncetime=500)

GPIO.output(18, False)
GPIO.output(23, False)
GPIO.output(12, False)

input("press enter to quit\n\n")

GPIO.cleanup()


