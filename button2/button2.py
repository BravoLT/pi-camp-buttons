import RPi.GPIO as GPIO


light_on=False


def button_pressed(channel):
  global light_on  

  if light_on:
    light_on=False
    GPIO.output(18, False)
    print("light off")
  
  else:
    light_on=True
    GPIO.output(18, True)
    print("light on")


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(18, GPIO.OUT)

GPIO.add_event_detect(25, GPIO.RISING, callback=button_pressed, bouncetime=500)

input("press enter to quit\n\n")

GPIO.cleanup()


