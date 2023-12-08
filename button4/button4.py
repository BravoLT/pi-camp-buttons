import RPi.GPIO as GPIO


light_18_on=True
light_23_on=True


def button_25_pressed(channel):
  global light_18_on  

  if light_18_on:
    light_18_on=False
    GPIO.output(18, False)
    print("light 18 off")
  
  else:
    light_18_on=True
    GPIO.output(18, True)
    print("light 18 on")


def button_24_pressed(channel):
  global light_23_on  

  if light_23_on:
    light_23_on=False
    GPIO.output(23, False)
    print("light 23 off")
  
  else:
    light_23_on=True
    GPIO.output(23, True)
    print("light 23 on")


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

GPIO.add_event_detect(25, GPIO.RISING, callback=button_25_pressed, bouncetime=500)
GPIO.add_event_detect(24, GPIO.RISING, callback=button_24_pressed, bouncetime=500)

GPIO.output(18, True)
GPIO.output(23, True)

input("press enter to quit\n\n")

GPIO.cleanup()


