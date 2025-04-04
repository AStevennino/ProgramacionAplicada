import machine
import time

led_pins = [23,18,13,12,16,17,25,4]  # Ajusta según tu conexión

# Crear una lista de objetos Pin configurados como salida
leds = [machine.Pin(pin, machine.Pin.OUT) for pin in led_pins]

while True:
    # Encender los LEDs en secuencia
    for led in leds:
        led.value(1)
        time.sleep(0.5) 
        led.value(0)
    
    # Apagar los LEDs en secuencia
    for led in reversed (leds):
        led.value(1)  
        time.sleep(0.5)
        led.value(0)
        