import RPi.GPIO as GPIO

class ButtonFactory:
    
    def __init__(self, channel, action, BounceTime):
        GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(channel, GPIO.RISING, callback=action, bouncetime=BounceTime)