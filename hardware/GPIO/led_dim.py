from gpiozero import LEDBarGraph
from time import sleep

''' LEDBarGraph
Dies ist ein Beispielprogramm für das neue HAT.
VHS Esslingen - raspberry pi Fortgeschrittenen Kurs

Matthias Burger 2018-05
'''
# alle drei LEDs als Einheit ansprechen
graph = LEDBarGraph(5,6,13,pwm=True)

time = 0.5

while(True):
    # Value darf zwischen 0 und 1 sein
    # je nach Wert von value werden die LEDs unterschiedlich hell erleuchtet
    graph.value = 1/10
    sleep(time)
    graph.value = 3/10
    sleep(time)
    graph.value = 5/10
    sleep(time)
    graph.value = 9/10
    sleep(time)
    graph.value = 10/10
    sleep(time)
    
