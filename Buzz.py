import time
import board
import digitalio

buzzer = digitalio.DigitalInOut(board.D2)
buzzer.direction = digitalio.Direction.OUTPUT

led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT


while True:
    buzzer.value = True
    led.value = False
    time.sleep(0.75)
    buzzer.value = False
    led.value = True
    time.sleep(0.75)