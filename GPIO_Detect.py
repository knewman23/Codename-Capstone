import threading
import time
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print('Error importing RPi.GPIO')

DETECT_PIN = 5

# Cycle time is an estimate of how long the plunger takes to retract
CYCLE_TIME = 3.5

GPIO.setmode(GPIO.BCM)
GPIO.setup(DETECT_PIN, GPIO.IN)

class SendPacketThread(threading.Thread):
    def __init__(self, name, timeStamp):
        threading.Thread.__init__(self)
    def run(self):
        # send off the packet


# Start loop to wait for a trigger
while True:
    if GPIO.input(DETECT_PIN):
        event = SendPacketThread()
        event.start()
        time.sleep(CYCLE_TIME)
