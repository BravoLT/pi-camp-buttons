import RPi.GPIO as GPIO


light_18_on=True


def button_pressed(channel):
  global light_18_on  

  if light_18_on:
    light_18_on=False
    GPIO.output(18, False)
    GPIO.output(23, True)
    print("light 18 off and light 23 on")
  
  else:
    light_18_on=True
    GPIO.output(18, True)
    GPIO.output(23, False)
    print("light 18 on and light 23 off")


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

GPIO.add_event_detect(25, GPIO.RISING, callback=button_pressed, bouncetime=500)

GPIO.output(18, True)

input("press enter to quit\n\n")

GPIO.cleanup()


