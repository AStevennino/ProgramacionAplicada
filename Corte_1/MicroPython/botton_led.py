import time
from machine import Pin



led1 = Pin(19, Pin.OUT)
push_button1 = Pin(13,Pin.IN)
while True:
  logic_state1 = push_button1.value()
  if logic_state1 == True:
    led1.value(1)
  else:
    led1.value(0)
  