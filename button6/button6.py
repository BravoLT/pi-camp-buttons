import RPi.GPIO as GPIO
import random
import time



button_to_light_dict={
  25: { "channel": 18 },
  24: { "channel": 23 },
  16: { "channel": 12 }
}
index=0
sequence=[25, 24, 16]


def all_lights(value):
  GPIO.output(18, value)
  GPIO.output(23, value)
  GPIO.output(12, value)


def button_pressed(channel):
  global button_to_light_dict
  global index
  global sequence  

  expected=sequence[index]
  
  if channel == expected and index == len(sequence) - 1:
    print("you win!")

    for step in range(10):
      all_lights(True)
      time.sleep(0.2)

      all_lights(False)
      time.sleep(0.2)

    print("play again?")
    setup_game()

  elif channel == expected:
    GPIO.output(button_to_light_dict[channel]["channel"], True)
    index += 1
  
  else:
    print("wrong sequence! try again")
    setup_game()


def setup_game():
  global index
  global sequence

  index=0

  random.shuffle(sequence)
  
  all_lights(True)
  time.sleep(0.5)
  
  all_lights(False)


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# buttons
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(25, GPIO.RISING, callback=button_pressed, bouncetime=500)
GPIO.add_event_detect(24, GPIO.RISING, callback=button_pressed, bouncetime=500)
GPIO.add_event_detect(16, GPIO.RISING, callback=button_pressed, bouncetime=500)

# lights
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)

setup_game()

input("press enter to quit\n\n")

GPIO.cleanup()


