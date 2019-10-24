import time
import RPi.GPIO as GPIO

test_channel = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(test_channel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def buttonPress(channel):
    print(f"Button Pressed: {channel}")
    
GPIO.add_event_detect(test_channel, GPIO.RISING, callback=buttonPress, bouncetime=1)

GPIO.cleanup()