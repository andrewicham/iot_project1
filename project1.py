import RPi.GPIO as GPIO

PowerInputPin = 8
LedPinOne = 14
LedPinTwo = 24
BtnOnePin = 18
BtnTwoPin = 20

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LedPinOne, GPIO.OUT) #sets both Led Pins to output mode
    GPIO.setup(LedPinTwo, GPIO.OUT)

    Gpio.setup(BtnOnePin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    GPIO.output(LedPin, GPIO.HIGH)

def loop():
    while True:
        if GPIO.input(BtnOnePin) == GPIO.LOW:
            print('led on')
            GPIO.output(LedPin, GPIO.LOW)
