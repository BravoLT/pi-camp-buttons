import RPi.GPIO as GPIO


def button_pressed(channel):
  print("button pressed")


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(25, GPIO.RISING, callback=button_pressed, bouncetime=500)

input("press enter to quit\n\n")

GPIO.cleanup()


