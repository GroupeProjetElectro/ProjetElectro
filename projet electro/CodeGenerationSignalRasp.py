import RPi.GPIO as GPIO
from time import sleep

led = 7
attente = 175

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led, GPIO.OUT)

def ecrire_1(pin):
    GPIO.output(pin, False)
    sleep(attente/1000000.0)
    GPIO.output(pin, True)
    sleep(attente/1000000.0)
    
def ecrire_0(pin):
    GPIO.output(pin, True)
    sleep(attente/1000000.0)
    GPIO.output(pin, False)
    sleep(attente/1000000.0)

while True:

    ecrire_1(led);
    ecrire_1(led);
    ecrire_1(led);
    ecrire_1(led);
    ecrire_1(led);
    ecrire_1(led);
    ecrire_1(led);
    ecrire_1(led);
    ecrire_1(led);
    
    # Donnees
    
    # 10
    
    ecrire_1(led);
    ecrire_1(led);
    ecrire_1(led);
    ecrire_1(led);
    ecrire_1(led);
    
    ecrire_0(led);
    ecrire_0(led);
    ecrire_0(led);
    ecrire_0(led);
    ecrire_0(led);
    
    #20
    
    ecrire_1(led);
    ecrire_1(led);
    ecrire_1(led);
    ecrire_1(led);
    ecrire_1(led);
    
    ecrire_0(led);
    ecrire_0(led);
    ecrire_0(led);
    ecrire_0(led);
    ecrire_0(led);

    # 30
    
    ecrire_1(led);
    ecrire_1(led);
    ecrire_1(led);
    ecrire_1(led);
    ecrire_1(led);
    
    ecrire_0(led);
    ecrire_0(led);
    ecrire_0(led);
    ecrire_0(led);
    ecrire_0(led);
    
    # 40
    
    ecrire_1(led);
    ecrire_1(led);
    ecrire_1(led);
    ecrire_1(led);
    ecrire_1(led);
    
    ecrire_0(led);
    ecrire_0(led);
    ecrire_0(led);
    ecrire_0(led);
    ecrire_0(led);
    
    #50
    
    ecrire_1(led);
    ecrire_1(led);
    ecrire_1(led);
    ecrire_1(led);
    ecrire_1(led);
    
    ecrire_0(led);
    ecrire_0(led);
    ecrire_0(led);
    ecrire_0(led);
    ecrire_0(led);
    
    # 55
    
    ecrire_1(led);
    ecrire_1(led);
    ecrire_1(led);
    ecrire_1(led);
    ecrire_0(led);
    
