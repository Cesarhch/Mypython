import uasyncio as asyncio
from machine import Pin
import time
import network
import webrepl

ssid = "ESP32.led"
password = "po12345678"

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=ssid, password=password, authmode=network.AUTH_WPA2_PSK)

while not ap.active():
    pass

# Initialize the built-in LED as an output
led = machine.Pin(14, machine.Pin.OUT)

# Función que se ejecutará en el segundo núcleo
async def second_core():
    while True:
        led.value(1)  # Turn the LED on
        time.sleep(1)  # Wait for a second
        led.value(0)  # Turn the LED off
        time.sleep(1)  # Wait for a second
        print("Función ejecutándose en el segundo núcleo")
        await asyncio.sleep(1)

# Función principal
async def main():
    # Configurar pin LED
    led = Pin(2, Pin.OUT)

    # Ciclo infinito que alterna el estado del LED cada segundo
    while True:
        webrepl.start()
        webrepl.start(password='mypass')
        print("Función ejecutándose en el primer núcleo")
        await asyncio.sleep(1)

# Crear un bucle de eventos y ejecutar las corutinas asincrónicas en paralelo
loop = asyncio.get_event_loop()
loop.create_task(second_core())
loop.run_until_complete(main())
