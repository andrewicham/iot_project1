import glob
import time
import RPi.GPIO as GPIO
import threading

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'
LedPinOne = 24

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LedPinOne, GPIO.OUT)

def destroy():
    GPIO.output(LedPinOne, GPIO.LOW)
    GPIO.cleanup()

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')

    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c, temp_f

def listen_for_temp():
    while True:
        celcius, farenheit = read_temp()
        if celcius > 25.00:
            GPIO.output(LedPinOne, GPIO.HIGH) #turn on

        elif celcius <= 25.00:
            GPIO.output(LedPinOne, GPIO.LOW)
             
    time.sleep(1)

if __name__ == '__main__':
    
    setup()

    try:
        listen_for_temp()
    except KeyboardInterrupt:
        destroy()


