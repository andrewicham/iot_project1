import RPi.GPIO as GPIO
import time
import threading

PowerInputPin = 8
LedPinOne = 24
LedPinTwo = 16
BtnOnePin = 18
BtnTwoPin = 22



def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LedPinOne, GPIO.OUT) #sets both Led Pins to output mode
    GPIO.setup(LedPinTwo, GPIO.OUT)

    GPIO.setup(BtnOnePin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(BtnTwoPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(BtnOnePin, GPIO.RISING)
    GPIO.add_event_detect(BtnTwoPin, GPIO.RISING)
    GPIO.output(LedPinOne, GPIO.HIGH)


def lightOne():
    flashTime = 2
    counter = 0
    buttonToggle = True
    buttonToggleTwo = True
    while True:
        GPIO.output(LedPinOne, GPIO.LOW)
        time.sleep(flashTime)
        GPIO.output(LedPinOne, GPIO.HIGH)
        time.sleep(flashTime)

        if GPIO.event_detected(BtnTwoPin):
			buttonToggleTwo = not buttonToggleTwo
			print('button two toggled')
		
        if buttonToggleTwo == True:
			if GPIO.event_detected(BtnOnePin):
				buttonToggle = not buttonToggle
				print('button one toggled')
		
        if buttonToggle == True:
            if counter != 4:
                flashTime = flashTime / 1.7
                counter = counter + 1
            elif counter == 4:
                counter = 0
                flashTime = 2
                
def lightTwo():
	flashTime = 0.5
	counter = 0
	buttonToggle = True
	buttonToggleTwo = False
	while True:
		GPIO.output(LedPinTwo, GPIO.LOW)
		time.sleep(flashTime)
		GPIO.output(LedPinTwo, GPIO.HIGH)
		time.sleep(flashTime)
		
		if GPIO.event_detected(BtnTwoPin):
			buttonToggleTwo = not buttonToggleTwo
			print('button 2 toggled')
		
		if buttonToggleTwo == True:
		    if GPIO.event_detected(BtnOnePin):
			    buttonToggle = not buttonToggle
			    print('button 1 toggled')
        
		if buttonToggle == True:
			if counter != 3:
				flashTime = flashTime * 1.3
				counter = counter + 1
			elif counter == 3:
				counter = 0
				flashTime = 2

    

def destroy():
    GPIO.output(LedPinOne, GPIO.HIGH)
    GPIO.cleanup()
    
if __name__ == '__main__':
    setup()
    try:
		t1 = threading.Thread(target=lightOne)
		t2 = threading.Thread(target=lightTwo)
		t1.start()
		t2.start()
		t1.join()
		t2.join()
    except KeyboardInterrupt:
        destroy()
