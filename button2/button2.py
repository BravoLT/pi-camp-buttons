import RPi.GPIO as GPIO


light_on=False


def button_pressed(channel):
  light_on=!light_on
  GPIO.output(18, light_on)
  
  if light_on:
    print("light on")
  else:
    print("light off")


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(18, GPIO.OUT)

GPIO.add_event_detect(10, GPIO.RISING, callback=button_pressed)

input("press enter to quit\n\n")

GPIO.cleanup()


