import RPi.GPIO as GPIO
import random
import time


index=0
sequence=[25, 24, 16]
button_to_light_dict={
  25: 18,
  24: 23,
  16: 12
}


random.shuffle(sequence)


def all_lights(value):
  GPIO.output(18, value)
  GPIO.output(23, value)
  GPIO.output(12, value)


def button_pressed(channel):
  global index
  global sequence  

  expected=sequence[index]
  
  if channel == expected and index == len(sequence) - 1:
    print("you win!")

    for step in range(5):
      all_lights(True)
      time.sleep(1)

      all_lights(False)
      time.sleep(1)

  elif channel == expected:
    GPIO.output(button_to_light_dict[channel], True)
    index += 1
  
  else:
    print("wrong sequence! try again")
    all_lights(False)
    index = 0
    

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)

GPIO.add_event_detect(25, GPIO.RISING, callback=button_pressed, bouncetime=500)
GPIO.add_event_detect(24, GPIO.RISING, callback=button_pressed, bouncetime=500)
GPIO.add_event_detect(16, GPIO.RISING, callback=button_pressed, bouncetime=500)

all_lights(True)

input("press enter to quit\n\n")

GPIO.cleanup()


