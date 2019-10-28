import RPi.GPIO as gp

gp.setmode(gp.BCM)
gp.setwarnings(True)

gp.setup(23, gp.IN)

try:
    print(not gp.input(23))
    while True:
        if not gp.input(23):
            print("Pressed")
#             pass
except(KeyboardInterrupt):
    gp.cleanup()