import RPi.GPIO as GPIO


def button_pressed(channel):
  print("button pressed")


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(10, GPIO.RISING, callback=button_pressed)

input("press any key to quit")

GPIO.cleanup()


