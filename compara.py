from prueba import run_micropython_code

port = "/dev/tty.usbserial-0001"  

def comprobar(palabra):
    #Comprobar si reconoce una instruccion
    if palabra == 'apaga el led':
            print('entiendo que apague el led')
            run_micropython_code(port, apagaLed)
    elif palabra == 'enciende el led':
            print('entiendo que encienda el led')
            run_micropython_code(port, enciendeLed)
    elif palabra == 'hola':
            print('entiendo hola')
            run_micropython_code(port, hola)    
    else:
            print('lo siento, no he entendido la instruccion')
        

def apagaLed():
    return '''
from machine import Pin
led=Pin(14, Pin.OUT)
led.off()
'''

def enciendeLed():
    return '''
from machine import Pin
led=Pin(14, Pin.OUT)
led.on()
'''

def hola():
    return '''
print("hola")
'''
