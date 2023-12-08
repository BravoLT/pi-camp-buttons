import RPi.GPIO as GPIO


button_to_light_dict={
  25: { "channel": 18, "on": True },
  24: { "channel": 23, "on": True },
  16: { "channel": 12, "on": True }
}


def all_lights(value):
  GPIO.output(18, value)
  GPIO.output(23, value)
  GPIO.output(12, value)


def button_pressed(channel):
  global button_to_light_dict  

  light=button_to_light_dict[channel]
  light_channel=light["channel"]


  if light["on"]:
    light["on"]=False
    GPIO.output(light_channel, False)
    print(f"light {light_channel} off")

  else:
    light["on"]=True
    GPIO.output(light_channel, True)
    print(f"light {light_channel} on")
  

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

all_lights(True)

input("press enter to quit\n\n")

GPIO.cleanup()


