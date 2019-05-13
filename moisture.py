import RPi.GPIO as GPIO
import time
from twilio.rest import Client
GPIO.setmode(GPIO.BCM)
channel = 17
GPIO.setup(channel, GPIO.IN)
client = Client("AC7687daacecb53dc1370a482ceab0b4a7", "d0fe55bb364dc6d703beb1cb$
client.messages.create(body="Green Thumb is active! Water me to begin!", from_=$

while True:
        waterLev = GPIO.input(channel)
        if (waterLev == 0):
                client.messages.create(body="Thank you for watering me!", from_$
                time.sleep(432000)
                client.messages.create(body="I'm thirsty, water me fool!", from$
        time.sleep(2)
