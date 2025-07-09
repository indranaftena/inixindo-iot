from machine import Pin
from time import sleep
p5 = Pin(5, Pin.OUT)

def loop():
  p5.value(0)
  sleep(0.4)
  p5.value(1)
  sleep(0.4)
  print("Hallo poliwangi")
  print("Dari github indra")
  print("Hello dari Pak Arif Fahmi")
