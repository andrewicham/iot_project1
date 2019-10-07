import RPi.GPIO as GPIO
import time

PowerInputPin = 8
LedPinOne = 24
LedPinTwo = 12
BtnOnePin = 18
BtnTwoPin = 26



def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LedPinOne, GPIO.OUT) #sets both Led Pins to output mode
    GPIO.setup(LedPinTwo, GPIO.OUT)

    GPIO.setup(BtnOnePin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    GPIO.output(LedPinOne, GPIO.HIGH)


def loop():
    flashTime = 2
    counter = 0
    buttonToggle = False
    while True:
        
        GPIO.add_event_detect(channel, GPIO.input(BtnOnePin))
        GPIO.output(LedPinOne, GPIO.LOW)
        time.sleep(flashTime)
        GPIO.output(LedPinOne, GPIO.HIGH)
        time.sleep(flashTime)
        #input_state = GPIO.input(BtnOnePin)
        if GPIO.event_detect(channel):
            buttonToggle = not buttonToggle
            print('toggled')
        if buttonToggle == True:
            if counter != 5:
                flashTime = flashTime / 1.5
                counter = counter + 1
            elif counter == 5:
                counter = 0
                flashTime = 2
                
                
        else:
            print('led off')
            GPIO.output(LedPinOne, GPIO.LOW)
            
        

    

def destroy():
    GPIO.output(LedPinOne, GPIO.HIGH)
    GPIO.cleanup()
    
if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
    





